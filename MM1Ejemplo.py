import numpy as np
import math
import random
#Inicializar variables

global sig_tipo_evento
global limite_cola

global tiempo
global num_demora_requerido
global num_eventos
global estado_server
global total_de_demoras
global num_cliente_demorados
global mediana_entrearrivos
global mediana_servicio
global tiempo_arrivo
global num_en_cola
global tiempo_proximo_evento
global tiempo_ultimo_evento
global area_num_en_cola
global area_estado_server

def expon(mediana):
    u = np.random.uniform(0, 1)
    valor= mediana*-1 * math.log(u)
    return valor


def inicializar():
    global tiempo
    global tiempo_proximo_evento
    global mediana_entrearrivos
    global estado_server
    global num_en_cola
    global tiempo_ultimo_evento
    global num_cliente_demorados
    global total_de_demoras
    global area_estado_server
    global area_num_en_cola
    #inicializar reloj
    tiempo=0
    #inicializar variables de estado
    estado_server=0
    num_en_cola = 0
    tiempo_ultimo_evento = 0
    #incializar contadores estadisticos
    num_cliente_demorados = 0
    total_de_demoras = 0
    area_num_en_cola = 0
    area_estado_server = 0
    #inicializar lista de eventos
    tiempo_proximo_evento[1]=tiempo+expon(mediana_entrearrivos)
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

def arrivo():
    global tiempo_proximo_evento
    global tiempo
    global mediana_entrearrivos
    global mediana_servicio
    global estado_server
    global num_en_cola
    global limite_cola
    global tiempo_arrivo
    global total_de_demoras
    global num_cliente_demorados
    tiempo_proximo_evento[1]= tiempo+expon(mediana_entrearrivos)
    if (estado_server==1):
        num_en_cola= num_en_cola+1
        if (num_en_cola>limite_cola):
            print("Sobrecarga de limite cola en el tiempo:" + str(tiempo) )
        tiempo_arrivo[num_en_cola]= tiempo
    else:
        demora=0
        total_de_demoras= total_de_demoras+ demora
        num_cliente_demorados= num_cliente_demorados+1
        estado_server=1
        tiempo_proximo_evento[2]= tiempo+ expon(mediana_servicio)

def partida():
    global tiempo
    global num_en_cola
    global tiempo_arrivo
    global estado_server
    global mediana_servicio
    global tiempo_proximo_evento
    global total_de_demoras
    global num_cliente_demorados
    if (num_en_cola==0):
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

def reportaje():
    global total_de_demoras
    global num_cliente_demorados
    global area_num_en_cola
    global area_estado_server
    global tiempo
    print("Promedio de demoras en cola:" + str((total_de_demoras)/ num_cliente_demorados))
    print("Numero promedio de clientes en cola:" + str (area_num_en_cola /tiempo))
    print("Utilizacion del server:" + str(area_estado_server/tiempo))
    print("Tiempo de simulacion termino:" + str(tiempo))

def actualizar_tiempo_promedio_estadisticos():
    global tiempo
    global tiempo_ultimo_evento
    global area_num_en_cola
    global area_estado_server
    global num_en_cola
    global estado_server
    tiempo_desde_ultimo_evento= tiempo - tiempo_ultimo_evento
    tiempo_ultimo_evento= tiempo
    area_num_en_cola = area_num_en_cola + (num_en_cola * tiempo_desde_ultimo_evento)
    area_estado_server = area_estado_server + estado_server * tiempo_desde_ultimo_evento






def main():
    global num_eventos
    global mediana_servicio
    global mediana_entrearrivos
    global num_demora_requerido
    global num_cliente_demorados
    global sig_tipo_evento
    #Especificar el numero de eventos para la funcion timing
    num_eventos = 2
    # Mostrar los parametros iniciales
    print("----------------------------COMIENZO SIMULACION MM1--------------------------")
    print("Tiempo de mediana entre arrivos:" +str(mediana_entrearrivos) + " minutos")
    print("Tiempo de mediana de servicio:" +str(mediana_servicio) + " minutos")
    print("Numero de clientes: " + str(num_demora_requerido))
    #inicializar la simulacion
    inicializar()
    #Correr la simulacion mientras mas numeros de demora sean requeridos
    while (num_cliente_demorados< num_demora_requerido):
        #determinar el siguiente evento
        timing()
        # Actualizar promedioas estadisticos
        actualizar_tiempo_promedio_estadisticos()
        if sig_tipo_evento==1:
            arrivo()
        elif sig_tipo_evento==2:
            partida()
    reportaje()


limite_cola= 100
mediana_entrearrivos=1
num_demora_requerido=1000
mediana_servicio=0.5
tiempo_arrivo=[0] * (limite_cola+1)
tiempo_proximo_evento=[0,0,0]

main()
