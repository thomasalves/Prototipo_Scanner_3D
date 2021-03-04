# -*- coding: utf-8 -*-
from tkinter import *
import serial

fila = [0]

# porta = "COM3"
# velocidade = 9600
# conexao = serial.Serial(porta, velocidade)

portaUSB = 0

def create_porta():
    global portaUSB
    aux = temp.get()
    portaUSB = serial.Serial(aux, 9600)
    print(portaUSB.portstr)
    print("porta conectada")
    #print(portaUSB)

def send_command(cod):
    aux = str(cod)
    portaUSB.write(aux.encode())
    leitura_serial = portaUSB.readline()
    print("Arduino diz: ", leitura_serial)
  

def comando():
    
    
    graus = int(entrada.get())

   
    graus_memoria = fila.pop(0)
    if graus > graus_memoria:
        print( "valor maior é:",graus)

        grausIn = graus - graus_memoria
        print(" valor GrausIN", grausIn)

        
               
        passo =( ((2050 * (grausIn))/ 360));
        inteiro_graus = int(grausIn)
        String_graus = str(inteiro_graus)
        
        print(" quantidade de passos", passo)
        send_command(String_graus)
        fila.append(graus)       
        print(" String_passo: " , String_graus)

    else:
        
 
        print("graus memoria", graus_memoria)
        print("valor menor")
        
        grausIn = graus_memoria - graus
        print("valor GrausIN -", grausIn)
        graus_memoria = graus  
        passo =( ((2050 * (-grausIn))/ 360));
        
        inteiro_graus = int(-grausIn)
        String_graus = str(inteiro_graus)
        send_command(String_graus)
        
        print(" quantidade de passos", passo)
        print(" valor graus_memoria", graus_memoria)
        fila.append(graus)

    print("enviando valor em Graus", graus)



   

janela = Tk()

janela.title('Scanner 3D')

janela.geometry('450x450')

port = Label(text= "Informe a porta: ").place(x = 30, y = 60)
temp = StringVar()
porta_ar = Entry(janela, textvariable = temp).place(x =155, y = 60)
botao_port = Button(text = "OK", command = create_porta).place(x= 285, y = 55)


texto1 = Label(text='Insira a grau desejado:')
texto1.place(x = 30, y = 100)

entrada = Entry(janela, bd = 2)
entrada.place(x = 155, y = 102)

botao1 = Button(text = 'OK!', command = comando).place(x = 285, y = 95)



janela.mainloop()

 
