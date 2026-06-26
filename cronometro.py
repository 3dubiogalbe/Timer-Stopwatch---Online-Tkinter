import tkinter as tk
import threading
import time

janela = tk.Tk()
janela.title("Cronometro")
janela.geometry("1000x500")
janela.config(background="#414141")
janela.iconbitmap(r"C:\Users\Eduardo\Desktop\Coursera\img\relogio.ico")

rodando = False
tempo = 0
decimo_atual = 0

def contar_tempo():

    global tempo
    global decimo_atual 

    while rodando:
        for i in range(10):
            time.sleep(0.1)  
            decimo_atual = i
            if rodando == False:
                break
            
            if i == 9:
                tempo += 1

def atualizar_label():
    minutos = tempo // 60
    segundos = tempo % 60
    label_timer.config(
        text=f"{minutos:02}:{segundos:02}:{decimo_atual:02}"
        )
    janela.after(100, atualizar_label) # Significa: "Depois de você executar sua própria função, espere 0.1 segundo e execute novamente, atualizando o label"

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
    global decimo_atual
    tempo = 0
    decimo_atual = 0
    rodando = False    

frame = tk.Frame(
    janela, 
    background="#414141"
    )

frame.pack()

label_timer = tk.Label(
    janela, 
    text="00:00:00", 
    font=("Consolas", 24), 
    background="#414141", 
    foreground="#FFFFFF"
    )

label_timer.pack(
    pady=100, 
    side="top"
    )

btn_start = tk.Button(
    frame, 
    text="Começar cronometro", 
    command= iniciar, 
    font=("Consolas", 12), 
    background="#414141", 
    foreground="#FFFFFF"
    )

btn_start.pack(
    side="right", 
    padx= 5
    )
 
btn_pause = tk.Button(
    frame, 
    text="Pausar cronometro", 
    command= pausar, 
    font=("Consolas", 12), 
    background="#414141", 
    foreground="#FFFFFF"
    )

btn_pause.pack(
    side="right", 
    padx= 5
    )

btn_reset = tk.Button(
    frame, 
    text="Resetar cronometro", 
    command=resetar, 
    font=("Consolas", 12), 
    background="#414141", 
    foreground="#FFFFFF"
    )

btn_reset.pack(
    side="right", 
    padx= 5
    )

janela.after(
    100, 
    atualizar_label
    ) # Significa: "Daqui a 0.1 segundo, rode a função atualizar_label"

tk.Label(
    janela, 
    text="Por: Eduardo Bio", 
    font=("Consolas", 12), 
    background="#414141", 
    foreground="#FFFFFF"
    ).pack()

tk.Label(
    janela, 
    text="Versão 1.2 ## Finalizado!", 
    font=("Consolas", 9), 
    background="#414141", 
    foreground="#FFFFFF"
    ).pack()

janela.mainloop()

# Última modificação: 26/06/2026 - 20:23 {Projeto finalizado!  :D }



