import os
import time
import subprocess
import pyautogui # type: ignore


#Caminho para a pasta onde estão os arquivos PDF
pasta_pdf = "C:\\Users\\Fina3\\Documents\\teste"

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" 

#Lista todos os arquivos na pasta
arquivos = os.listdir(pasta_pdf)

#Filtra apenas os arquivos com extensão .pdf
pdfs = [f for f in arquivos if f.lower().endswith(".pdf")]

#Ordena os arquivos pela data de criação 
pdfs = sorted(pdfs, key=lambda f: os.path.getctime(os.path.join(pasta_pdf, f)))

#Para cada arquivo PDF encontrado, envia para a impressora
for pdf in pdfs:
    caminho_pdf = os.path.join(pasta_pdf, pdf)
    try:
        print(f"Imprimindo: {caminho_pdf}")
        
        #Comando para abrir o Microsoft Edge e o PDF
        subprocess.run([edge_path, caminho_pdf], check=True)

        #Aguarda um tempo para o Edge abrir o PDF e carregar
        time.sleep(3)

        #Simula pressionar as teclas necessárias para imprimir automaticamente
        #A sequência de teclas pode variar dependendo da versão do Edge e do sistema, então ajuste conforme necessário
        pyautogui.hotkey('ctrl', 'p')  # Simula CTRL+P para abrir a caixa de diálogo de impressão

        #Aguarda um tempo para a caixa de diálogo de impressão abrir
        time.sleep(3)

        #Simula pressionar o botão "Imprimir" na caixa de diálogo de impressão
        pyautogui.press('enter')  # Pressiona Enter para confirmar a impressão

        print(f"PDF {pdf} enviado para impressão.")

        #Aguarda o tempo suficiente para garantir que a impressão aconteça
        time.sleep(5)

    except Exception as e:
        print(f"Erro ao imprimir {pdf}: {e}")