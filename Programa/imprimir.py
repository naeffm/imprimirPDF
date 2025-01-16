import os
import time
import subprocess
import pyautogui
import tkinter as tk
from tkinter import messagebox, filedialog

#Funçao para imprimir os PDFs de uma pasta escolhida
def imprimir_pdfs(pasta_pdf):
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  #Caminho do MS Edge
    
    arquivos = os.listdir(pasta_pdf)  #Lista todos os arquivos na pasta
    pdfs = [f for f in arquivos if f.lower().endswith(".pdf")]  #Filtra apenas arquivos com a extensao .pdf
    
    pdfs = sorted(pdfs, key=lambda f: os.path.getctime(os.path.join(pasta_pdf, f)))  #Ordena por data de criaçao
    
    for pdf in pdfs:
        caminho_pdf = os.path.join(pasta_pdf, pdf)
        try:
            print(f"Imprimindo: {caminho_pdf}")
            
            #Comando para abrir o Microsoft Edge e o PDF
            subprocess.run([edge_path, caminho_pdf], check=True)
            
            #Aguarda um tempo para o Edge abrir o PDF e carregar
            time.sleep(3)
            
            #Simula pressionar as teclas necessarias para imprimir automaticamente
            pyautogui.hotkey('ctrl', 'p')  # Simula CTRL+P para abrir a caixa de diálogo de impressao
            
            #Aguarda um tempo para a caixa de dialogo de impressao abrir
            time.sleep(3)
            
            #Simula pressionar o botao "Imprimir" na caixa de dialogo de impressao
            pyautogui.press('enter')  # Pressiona Enter para confirmar a impressao
            
            print(f"PDF {pdf} enviado para impressão.")
            
            #Aguarda o tempo suficiente para garantir que a impressao aconteça
            time.sleep(5)
        
        except Exception as e:
            print(f"Erro ao imprimir {pdf}: {e}")
    
    #Exibe uma mensagem quando a impressao for concluída
    messagebox.showinfo("Impressão concluída", "Todos os PDFs foram enviados para a impressão.")

#Funçao para iniciar o processo de impressao
def iniciar_impressao():
    pasta_pdf = filedialog.askdirectory(title="Escolha a pasta com os PDFs")  
    if pasta_pdf:  
        try:
            imprimir_pdfs(pasta_pdf)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    else:
        messagebox.showwarning("Aviso", "Nenhuma pasta foi selecionada!")

#Configuraçao da interface grafica
root = tk.Tk()
root.title("Impressão de PDFs")

#Definindo tamanho da janela
root.geometry("300x150")

#Criando botao para iniciar o processo de impressao
botao_impressao = tk.Button(root, text="Imprimir PDFs", command=iniciar_impressao, width=20, height=2)
botao_impressao.pack(pady=30)

#Inicia a interface grafica
root.mainloop()
