import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def converter_imagem():
    caminho = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Imagem", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.webp")])
    if caminho:
        try:
            img = Image.open(caminho)
            formato_saida = formato_var.get()
            if formato_saida:
                novo_caminho = caminho.rsplit('.', 1)[0] + f"_convertido.{formato_saida}"
                img.save(novo_caminho, formato_saida.upper())
                messagebox.showinfo("Sucesso", f"Imagem convertida e salva como {novo_caminho}")
            else:
                messagebox.showwarning("Aviso", "Selecione o formato de saída")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao converter a imagem: {e}")
    else:
        messagebox.showwarning("Aviso", "Selecione uma imagem")

def converter_pasta():
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    if pasta:
        formato_saida = formato_var.get()
        if not formato_saida:
            messagebox.showwarning("Aviso", "Selecione o formato de saída")
            return

        for arquivo in os.listdir(pasta):
            if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
                caminho_imagem = os.path.join(pasta, arquivo)
                try:
                    img = Image.open(caminho_imagem)
                    novo_caminho = os.path.splitext(caminho_imagem)[0] + f"_convertido.{formato_saida}"
                    img.save(novo_caminho, formato_saida.upper())
                except Exception as e:
                    print(f"Erro ao converter {arquivo}: {e}")
        messagebox.showinfo("Sucesso", "Imagens da pasta convertidas com sucesso")


# Interface

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Conversor de Imagens")
root.iconbitmap("./imagem.ico")

root.geometry("400x500")
root.resizable(False, False)

formato_var = tk.StringVar(value="jpeg")

formatos = ["jpeg", "png", "bmp", "gif", "tiff", "webp"]

formato_label = ctk.CTkLabel(root, text="Selecione o formato para conversão:", font=("Inter", 12))
formato_label.pack(pady=10)

for formato in formatos:
    formato_rb = ctk.CTkRadioButton(root, text=formato.upper(), variable=formato_var, value=formato,border_color="#111111", hover_color='#212121', border_width_checked=2)
    formato_rb.pack(anchor="w", padx=155, pady=10)

label = ctk.CTkLabel(root, text="Selecione a imagem ou pasta para converter:", font=("Inter", 12))
label.pack(pady=10)

btn_arquivo = ctk.CTkButton(root, text="Selecionar Arquivo", command=converter_imagem, fg_color='black', hover_color='#616161')
btn_arquivo.pack(pady=10)

btn_pasta = ctk.CTkButton(root, text="Selecionar Pasta", command=converter_pasta, fg_color='black', hover_color='#616161')
btn_pasta.pack(pady=10)

root.mainloop()
