import numpy as np
import math
import random

global media_entrearrivos
media_entrearrivos = 10
global media_servicio1_A
media_servicio1_A = 7
global media_servicio1_B
media_servicio1_B = 5
global media_servicio2_A
media_servicio2_A = 5
global media_servicio2_B
media_servicio2_B = 5
global media_servicio2_C
media_servicio2_C = 6
global tiempo
global limite_cola
limite_cola= 100
global num_demora_requerido
num_demora_requerido=1000
global num_eventos
global estado_server1_A
global estado_server1_B
global estado_server2_A
global estado_server2_B
global estado_server2_C
global total_de_demoras
global num_cliente_demorados
global tiempo_arrivo
global num_en_cola
global num_en_cola1_A
global num_en_cola1_B
global num_en_cola2_A
global num_en_cola2_B
global num_en_cola2_C
global tiempo_proximo_evento
global tiempo_ultimo_evento
global area_num_en_cola
global area_estado_server1_A
global area_estado_server1_B
global area_estado_server2_A
global area_estado_server2_B
global area_estado_server2_C



def expon(mediana):
    u = np.random.uniform(0, 1)
    valor= mediana*-1 * math.log(u)
    return valor

def inicializar():
    global tiempo
    global tiempo_proximo_evento
    global mediana_entrearrivos
    global estado_server
    global num_en_cola1
    global num_en_cola2
    global num_en_cola3
    global num_en_cola4
    global num_en_cola5
    global tiempo_ultimo_evento
    global num_cliente_demorados
    global total_de_demoras
    global area_estado_server
    global area_num_en_cola
    #inicializar reloj
    tiempo=0
    #inicializar variables de estado
    estado_server=0
    num_en_cola1 = 0
    num_en_cola2 = 0
    num_en_cola3 = 0
    num_en_cola4 = 0
    num_en_cola5 = 0
    tiempo_ultimo_evento = 0
    #incializar contadores estadisticos
    num_cliente_demorados = 0
    total_de_demoras = 0
    area_num_en_cola = 0
    area_estado_server = 0
    #inicializar lista de eventos
    tiempo_proximo_evento[1]=tiempo+expon(media_entrearrivos)
    tiempo_proximo_evento[2]=1000000000000000000000

def timing():
    global tiempo
    global tiempo_proximo_evento
    global sig_tipo_evento
    global num_eventos
    tiempo_min_proximo_evento=  1000000000000000
    sig_tipo_evento=0

    for i in range(1, num_eventos+1):
        if(tiempo_proximo_evento[i]< tiempo_min_proximo_evento):
            tiempo_min_proximo_evento= tiempo_proximo_evento[i]
            sig_tipo_evento=i

    if(sig_tipo_evento==0):
        print("Se termina la cola en el tiempo:" + str(tiempo))

    tiempo= tiempo_min_proximo_evento

def arrivo1_A():
    global tiempo_proximo_evento
    global tiempo
    global media_entrearrivos
    global media_servicio1_A
    global estado_server1_A
    global num_en_cola1_A
    global num_en_cola
    global limite_cola
    global tiempo_arrivo
    global total_de_demoras
    global num_cliente_demorados
    tiempo_proximo_evento[1]= tiempo+expon(media_entrearrivos)
    if (estado_server1_A==1):
        num_en_cola1_A= num_en_cola1_A+1
        num_en_cola = num_en_cola + 1
        if (num_en_cola1_A>limite_cola):
            print("Sobrecarga de limite cola en el tiempo:" + str(tiempo) )
        tiempo_arrivo[num_en_cola]= tiempo
    else:
        demora=0
        total_de_demoras= total_de_demoras+ demora
        num_cliente_demorados= num_cliente_demorados+1
        estado_server1_A=1
        tiempo_proximo_evento[2]= tiempo+ expon(media_servicio1_A)

def arrivo1_B():
    global tiempo_proximo_evento
    global tiempo
    global media_entrearrivos
    global media_servicio1_B
    global estado_server1_B
    global num_en_cola1_B
    global num_en_cola
    global limite_cola
    global tiempo_arrivo
    global total_de_demoras
    global num_cliente_demorados
    tiempo_proximo_evento[1]= tiempo+expon(media_entrearrivos)
    if (estado_server1_B==1):
        num_en_cola1_B= num_en_cola1_B+1
        num_en_cola = num_en_cola + 1
        if (num_en_cola1_B>limite_cola):
            print("Sobrecarga de limite cola en el tiempo:" + str(tiempo) )
        tiempo_arrivo[num_en_cola]= tiempo
    else:
        demora=0
        total_de_demoras= total_de_demoras+ demora
        num_cliente_demorados= num_cliente_demorados+1
        estado_server1_B=1
        tiempo_proximo_evento[2]= tiempo+ expon(media_servicio1_B)


def partida1_A():
    global tiempo
    global num_en_cola1_A
    global tiempo_arrivo
    global estado_server1_A
    global mediana_servicio
    global tiempo_proximo_evento
    global total_de_demoras
    global num_cliente_demorados
    if (num_en_cola1_A==0):
        estado_server=0
        tiempo_proximo_evento[2]= 1000000000000000000000
    else:
        num_en_cola=num_en_cola-1
        demora = tiempo - tiempo_arrivo[1]
        total_de_demoras = total_de_demoras + demora
        num_cliente_demorados= num_cliente_demorados+1
        tiempo_proximo_evento[2]= tiempo + expon(mediana_servicio)
        for i in range (1, num_en_cola+1 ):
            tiempo_arrivo[i] = tiempo_arrivo[i+1]