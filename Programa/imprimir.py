import os
import time
import subprocess
import pyautogui  # type: ignore

#Obtem o caminho para a pasta onde o script esta sendo executado
pasta_programa = os.path.dirname(os.path.abspath(__file__))

#Caminho para a pasta onde estao os arquivos PDF (agora sera a pasta onde o script esta)
pasta_pdf = pasta_programa  

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

#Lista todos os arquivos na pasta
arquivos = os.listdir(pasta_pdf)

#Filtra apenas os arquivos com extensao .pdf
pdfs = [f for f in arquivos if f.lower().endswith(".pdf")]

#Ordena os arquivos pela data de criaçao
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

        #Simula pressionar as teclas necessarias para imprimir automaticamente
        #A sequencia de teclas pode variar dependendo da versao do Edge e do sistema, então ajuste conforme necessario
        pyautogui.hotkey('ctrl', 'p')  # Simula CTRL+P para abrir a caixa de dialogo de impressao

        #Aguarda um tempo para a caixa de dialogo de impressao abrir
        time.sleep(3)

        #Simula pressionar o botão "Imprimir" na caixa de dialogo de impressao
        pyautogui.press('enter')  # Pressiona Enter para confirmar a impressao

        print(f"PDF {pdf} enviado para impressão.")

        #Aguarda o tempo suficiente para garantir que a impressao aconteça
        time.sleep(5)

    except Exception as e:
        print(f"Erro ao imprimir {pdf}: {e}")
