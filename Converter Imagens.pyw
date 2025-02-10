import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os

# Função para converter a imagem
def converter_imagem():
    # Pega o arquivo ou pasta selecionada
    caminho = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Imagem", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.webp")])
    if caminho:
        # Abre a imagem selecionada
        try:
            img = Image.open(caminho)
            # Obtém o formato de saída selecionado
            formato_saida = formato_var.get()
            if formato_saida:
                # Define o novo caminho de saída
                novo_caminho = caminho.rsplit('.', 1)[0] + f"_convertido.{formato_saida}"
                # Salva a imagem no novo formato
                img.save(novo_caminho, formato_saida.upper())
                messagebox.showinfo("Sucesso", f"Imagem convertida e salva como {novo_caminho}")
            else:
                messagebox.showwarning("Aviso", "Selecione o formato de saída")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao converter a imagem: {e}")
    else:
        messagebox.showwarning("Aviso", "Selecione uma imagem")

# Função para selecionar a pasta e converter múltiplas imagens
def converter_pasta():
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    if pasta:
        formato_saida = formato_var.get()
        if not formato_saida:
            messagebox.showwarning("Aviso", "Selecione o formato de saída")
            return

        # Percorre todas as imagens na pasta e converte
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
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Conversor de Imagens")

root.geometry("400x500")
root.resizable(False, False)

frame = ctk.CTkFrame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

formato_var = tk.StringVar(value="jpeg")  # Valor padrão

formatos = ["jpeg", "png", "bmp", "gif", "tiff", "webp"]

formato_label = ctk.CTkLabel(frame, text="Selecione o formato para conversão:", font=("Arial", 12))
formato_label.pack(pady=10)

for formato in formatos:
    formato_rb = ctk.CTkRadioButton(frame, text=formato.upper(), variable=formato_var, value=formato)
    formato_rb.pack(anchor="w", padx=20, pady=10)

label = ctk.CTkLabel(frame, text="Selecione a imagem ou pasta para converter:", font=("Arial", 14))
label.pack(pady=10)

btn_arquivo = ctk.CTkButton(frame, text="Selecionar Arquivo", command=converter_imagem)
btn_arquivo.pack(pady=10)

btn_pasta = ctk.CTkButton(frame, text="Selecionar Pasta", command=converter_pasta)
btn_pasta.pack(pady=10)

root.mainloop()
