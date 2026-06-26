import tkinter as tk
import threading
import time

janela = tk.Tk()
janela.title("Cronometro")
janela.geometry("1000x500")

rodando = False
tempo = 0
global thread
global decimo

def contar_tempo():
    global tempo
          
    while rodando:
        for i in range(10):
            time.sleep(0.1)  

            if rodando == False:
                break
            
            if i == 9:
                tempo += 1

        
        

def atualizar_label():
    label_timer.config(text=f"{tempo}")
    janela.after(1000, atualizar_label) # Significa: "Depois de você executar sua própria função, espere um segundo e execute novamente, atualizando o label"

def iniciar():
    global rodando
    rodando = True 
    thread = threading.Thread(target=contar_tempo)
    thread.start()

def pausar():
    global rodando
    rodando = False

def resetar():
    global tempo
    global rodando
    tempo = 0
    rodando = False    

frame = tk.Frame(janela)
frame.pack()

label_timer = tk.Label(janela, text="00:00:00")
label_timer.pack(pady=100, side="top")

btn_start = tk.Button(frame, text="Começar cronometro", command= iniciar)
btn_start.pack(side="right", padx= 5)
 
btn_pause = tk.Button(frame, text="Pausar cronometro", command= pausar)
btn_pause.pack(side="right", padx= 5)

btn_reset = tk.Button(frame, text="Resetar cronometro", command=resetar)
btn_reset.pack(side="right", padx= 5)

janela.after(1000, atualizar_label) # Significa: "Daqui a 1 segundo, rode a função atualizar_label"

tk.Label(janela, text="Por: Eduardo Bio").pack()
tk.Label(janela, text="Versão 1.0 ## Ainda em desenvolvimento").pack()

janela.mainloop()

# Última modificação: 25/06/2026



