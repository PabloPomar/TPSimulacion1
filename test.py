import numpy as np
import math
import random
import matplotlib.pyplot as plt

global media_entrearrivos
media_entrearrivos = 1/10
global media_servicio1_A
media_servicio1_A = 1/7
global media_servicio1_B
media_servicio1_B = 1/5
global media_servicio2_A
media_servicio2_A = 1/5
global media_servicio2_B
media_servicio2_B = 1/5
global media_servicio2_C
media_servicio2_C = 1/6
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
global tiempo_arrivo1_A
global tiempo_arrivo1_B
global tiempo_arrivo2
global num_en_cola
global num_en_cola1_A
global num_en_cola1_B
global num_en_cola2
global num_en_cola2_A
global num_en_cola2_B
global num_en_cola2_C
global tiempo_proximo_evento
global tiempo_ultimo_evento
global area_num_en_cola
global area_num_en_cola1_A
global area_num_en_cola1_B
global area_num_en_cola2
global area_estado_server1_A
global area_estado_server1_B
global area_estado_server2_A
global area_estado_server2_B
global area_estado_server2_C
global tiempo_proximo_evento
global sig_tipo_evento
#Eventos Arribo a la cola1, partido del server 1_A, partida del server1_B , partida del server 2_A, partida del server 2_B, partida del server 2_C
tiempo_proximo_evento=[0, 0, 0, 0, 0, 0, 0]
num_eventos = 6

tiempo_arrivo1_A=[0] * (limite_cola+1)
tiempo_arrivo1_B=[0] * (limite_cola+1)
tiempo_arrivo2=[0] * (limite_cola+1)


global plotDemora
global plotClientesDem
plotDemora = []
plotClientesDem = []

global plotTiempo1A
global plotTiempo1B
global plotTiempo2
global plotCola1A
global plotCola1B
global plotCola2

plotTiempo1A = []
plotTiempo1B = []
plotTiempo2 = []
plotCola1A = []
plotCola1B = []
plotCola2 = []


global plotServ1A
global plotServ1B
global plotServ2A
global plotServ2B
global plotServ2C

plotServ1A = []
plotServ1B = []
plotServ2A = []
plotServ2B = []
plotServ2C = []


global plotDemoraProm
global plotCola1AProm
global plotCola1BProm
global plotCola2Prom
global plotServ1AProm
global plotServ1BProm
global plotServ2AProm
global plotServ2BProm
global plotServ2CProm

plotDemoraProm = []
plotCola1AProm = []
plotCola1BProm = []
plotCola2Prom = []
plotServ1AProm = []
plotServ1BProm = []
plotServ2AProm = []
plotServ2BProm = []
plotServ2CProm = []

def expon(mediana):
    u = np.random.uniform(0, 1)
    valor= mediana*-1 * math.log(u)
    return valor

def inicializar():
    global tiempo
    global tiempo_proximo_evento
    global estado_server1_A
    global estado_server1_B
    global estado_server2_A
    global estado_server2_B
    global estado_server2_C
    global num_en_cola1_A
    global num_en_cola1_B
    global num_en_cola2
    global num_en_cola
    global tiempo_ultimo_evento
    global num_cliente_demorados
    global total_de_demoras
    global area_num_en_cola1_A
    global area_num_en_cola1_B
    global area_num_en_cola2
    global area_estado_server1_A
    global area_estado_server1_B
    global area_estado_server2_A
    global area_estado_server2_B
    global area_estado_server2_C
    global plotDemora
    global plotClientesDem
    global plotTiempo1A
    global plotTiempo1B
    global plotTiempo2
    global plotCola1A
    global plotCola1B
    global plotCola2
    global plotServ1A
    global plotServ1B
    global plotServ2A
    global plotServ2B
    global plotServ2C
    global plotDemoraProm
    global plotCola1AProm
    global plotCola1BProm
    global plotCola2Prom
    global plotServ1AProm
    global plotServ1BProm
    global plotServ2AProm
    global plotServ2BProm
    global plotServ2CProm


    plotDemora.clear()
    plotClientesDem.clear()
    plotTiempo1A.clear()
    plotTiempo1B.clear()
    plotTiempo2.clear()
    plotCola1A.clear()
    plotCola1B.clear()
    plotCola2.clear()
    plotServ1A.clear()
    plotServ1B.clear()
    plotServ2A.clear()
    plotServ2B.clear()
    plotServ2C.clear()
    plotDemoraProm.clear()
    plotCola1AProm.clear()
    plotCola1BProm.clear()
    plotCola2Prom.clear()
    plotServ1AProm.clear()
    plotServ1BProm.clear()
    plotServ2AProm.clear()
    plotServ2BProm.clear()
    plotServ2CProm.clear()

    #inicializar reloj
    tiempo=0
    plotTiempo1A.append(tiempo)
    plotTiempo1B.append(tiempo)
    plotTiempo2.append(tiempo)
    #inicializar variables de estado
    estado_server1_A = 0
    estado_server1_B = 0
    estado_server2_A = 0
    estado_server2_B = 0
    estado_server2_C = 0
    plotServ1A.append(estado_server1_A)
    plotServ1B.append(estado_server1_B)
    plotServ2A.append(estado_server2_A)
    plotServ2B.append(estado_server2_B)
    plotServ2C.append(estado_server2_C)
    num_en_cola1_A = 0
    plotCola1A.append(num_en_cola1_A)
    plotCola1AProm.append(num_en_cola1_A)
    num_en_cola1_B = 0
    plotCola1B.append(num_en_cola1_B)
    plotCola1BProm.append(num_en_cola1_B)
    num_en_cola2 = 0
    plotCola2.append(num_en_cola2)
    plotCola2Prom.append(num_en_cola2)
    num_en_cola = 0
    tiempo_ultimo_evento = 0
    #incializar contadores estadisticos
    num_cliente_demorados = 0
    plotClientesDem.append(num_cliente_demorados)
    total_de_demoras = 0
    plotDemora.append(total_de_demoras)
    plotDemoraProm.append(total_de_demoras)
    area_num_en_cola1_A = 0
    area_num_en_cola1_B = 0
    area_num_en_cola2 = 0
    area_estado_server1_A = 0
    area_estado_server1_B = 0
    area_estado_server2_A = 0
    area_estado_server2_B = 0
    area_estado_server2_C = 0
    plotServ1AProm.append(area_estado_server1_A)
    plotServ1BProm.append(area_estado_server1_B)
    plotServ2AProm.append(area_estado_server2_A)
    plotServ2BProm.append(area_estado_server2_B)
    plotServ2CProm.append(area_estado_server2_C)
    #inicializar lista de eventos
    tiempo_proximo_evento[1] = tiempo+expon(media_entrearrivos)
    tiempo_proximo_evento[2] = 1000000000000000000000
    tiempo_proximo_evento[3] = 1000000000000000000000
    tiempo_proximo_evento[4] = 1000000000000000000000
    tiempo_proximo_evento[5] = 1000000000000000000000
    tiempo_proximo_evento[6] = 1000000000000000000000

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


def servers1ocupados():
    global estado_server1_A
    global estado_server1_B
    if estado_server1_A == 1 and estado_server1_B == 1:
        return 1
    elif estado_server1_A == 1 and estado_server1_B == 0:
        return 2
    elif estado_server1_A == 0 and estado_server1_B == 1:
        return 3
    elif estado_server1_A == 0 and estado_server1_B == 0:
        return 4

def arrivo1():
    global tiempo_proximo_evento
    global tiempo
    global media_entrearrivos
    global media_servicio1_A
    global estado_server1_A
    global num_en_cola1_A
    global num_en_cola
    global limite_cola
    global tiempo_arrivo1_A
    global total_de_demoras
    global num_cliente_demorados
    global media_servicio1_B
    global estado_server1_B
    global num_en_cola1_B
    global tiempo_arrivo1_B
    global plotDemora
    global plotClientesDem
    global plotDemoraProm
    tiempo_proximo_evento[1] = tiempo + expon(media_entrearrivos)
    estado = servers1ocupados()
    if estado == 1:
        if num_en_cola1_A <=num_en_cola1_B:
            num_en_cola1_A = num_en_cola1_A + 1
            num_en_cola = num_en_cola + 1
            if (num_en_cola1_A > limite_cola):
                print("Sobrecarga de limite cola en el tiempo:" + str(tiempo))
            tiempo_arrivo1_A[num_en_cola1_A] = tiempo
        else:
            num_en_cola1_B = num_en_cola1_B + 1
            num_en_cola = num_en_cola + 1
            if (num_en_cola1_B > limite_cola):
                print("Sobrecarga de limite cola en el tiempo:" + str(tiempo))
            tiempo_arrivo1_B[num_en_cola1_B] = tiempo
    elif estado == 2:
        demora=0
        total_de_demoras= total_de_demoras+ demora
        num_cliente_demorados= num_cliente_demorados+1
        plotDemora.append(demora)
        plotDemoraProm.append(np.mean(plotDemora))
        plotClientesDem.append(num_cliente_demorados)
        estado_server1_B=1
        tiempo_proximo_evento[3]= tiempo+ expon(media_servicio1_B)
    elif estado == 3:
        demora=0
        total_de_demoras= total_de_demoras+ demora
        num_cliente_demorados= num_cliente_demorados+1
        plotDemora.append(demora)
        plotDemoraProm.append(np.mean(plotDemora))
        plotClientesDem.append(num_cliente_demorados)
        estado_server1_A=1
        tiempo_proximo_evento[2]= tiempo+ expon(media_servicio1_A)
    elif estado == 4:
        demora=0
        total_de_demoras= total_de_demoras+ demora
        num_cliente_demorados= num_cliente_demorados+1
        plotDemora.append(demora)
        plotDemoraProm.append(np.mean(plotDemora))
        plotClientesDem.append(num_cliente_demorados)
        estado_server1_A=1
        tiempo_proximo_evento[2]= tiempo+ expon(media_servicio1_A)





def partida1_A():
    global tiempo
    global num_en_cola1_A
    global tiempo_arrivo1_A
    global estado_server1_A
    global media_servicio1_A
    global tiempo_proximo_evento
    global total_de_demoras
    global num_cliente_demorados
    global plotDemora
    global plotClientesDem
    global plotDemoraProm
    if (num_en_cola1_A==0):
        estado_server1_A=0
        tiempo_proximo_evento[2]= 1000000000000000000000
    else:
        num_en_cola1_A=num_en_cola1_A-1
        demora = tiempo - tiempo_arrivo1_A[1]
        total_de_demoras = total_de_demoras + demora
        num_cliente_demorados= num_cliente_demorados+1
        plotDemora.append(demora)
        plotDemoraProm.append(np.mean(plotDemora))
        plotClientesDem.append(num_cliente_demorados)
        tiempo_proximo_evento[2]= tiempo + expon(media_servicio1_A)
        if num_en_cola1_A==0:
            tiempo_arrivo1_A[1] = 0
        for i in range (1, num_en_cola1_A+1):
            tiempo_arrivo1_A[i] = tiempo_arrivo1_A[i+1]

def partida1_B():
    global tiempo
    global num_en_cola1_B
    global tiempo_arrivo1_B
    global estado_server1_B
    global media_servicio1_B
    global tiempo_proximo_evento
    global total_de_demoras
    global num_cliente_demorados
    global plotDemora
    global plotClientesDem
    global plotDemoraProm
    if (num_en_cola1_B==0):
        estado_server1_B=0
        tiempo_proximo_evento[3]= 1000000000000000000000
    else:
        num_en_cola1_B=num_en_cola1_B-1
        demora = tiempo - tiempo_arrivo1_B[1]
        total_de_demoras = total_de_demoras + demora
        num_cliente_demorados= num_cliente_demorados+1
        plotDemora.append(demora)
        plotDemoraProm.append(np.mean(plotDemora))
        plotClientesDem.append(num_cliente_demorados)
        tiempo_proximo_evento[3] = tiempo + expon(media_servicio1_B)
        if num_en_cola1_B==0:
            tiempo_arrivo1_B[1] = 0
        for i in range (1, num_en_cola1_B+1 ):
            tiempo_arrivo1_B[i] = tiempo_arrivo1_B[i+1]


def todosOcupados():
    global estado_server2_A
    global estado_server2_B
    global estado_server2_C
    if estado_server2_A == 1 and estado_server2_B == 1 and estado_server2_C == 1:
        return 1
    else:
        return 0


def cualDesocupado():
    global estado_server2_A
    global estado_server2_B
    global estado_server2_C
    if estado_server2_A == 0:
        return 1
    elif estado_server2_B == 0:
        return 2
    elif estado_server2_C == 0:
        return 3
    else:
        return 0

def arrivo2():
    global tiempo
    global media_entrearrivos
    global media_servicio2_A
    global media_servicio2_B
    global media_servicio2_C
    global estado_server2_A
    global estado_server2_B
    global estado_server2_C
    global num_en_cola2
    global num_en_cola
    global limite_cola
    global tiempo_arrivo2
    global total_de_demoras
    global num_cliente_demorados
    global plotDemora
    global plotClientesDem
    global plotDemoraProm
    servers = todosOcupados()
    if (servers==1):
        num_en_cola2= num_en_cola2+1
        num_en_cola = num_en_cola + 1
        if (num_en_cola2>limite_cola):
            print("Sobrecarga de limite cola en el tiempo:" + str(tiempo) )
        tiempo_arrivo2[num_en_cola2]= tiempo
    else:
        desocupado = cualDesocupado()
        demora=0
        total_de_demoras= total_de_demoras+ demora
        plotDemora.append(demora)
        plotDemoraProm.append(np.mean(plotDemora))
        if desocupado == 1:
            num_cliente_demorados= num_cliente_demorados+1
            plotClientesDem.append(num_cliente_demorados)
            estado_server2_A=1
            tiempo_proximo_evento[4]= tiempo+ expon(media_servicio2_A)
        elif desocupado == 2:
            num_cliente_demorados= num_cliente_demorados+1
            plotClientesDem.append(num_cliente_demorados)
            estado_server2_B=1
            tiempo_proximo_evento[5]= tiempo+ expon(media_servicio2_B)
        elif desocupado == 3:
            num_cliente_demorados= num_cliente_demorados+1
            plotClientesDem.append(num_cliente_demorados)
            estado_server2_C=1
            tiempo_proximo_evento[6]= tiempo+ expon(media_servicio2_B)


def partida2_A():
    global tiempo
    global num_en_cola2
    global tiempo_arrivo2
    global estado_server2_A
    global media_servicio2_A
    global tiempo_proximo_evento
    global total_de_demoras
    global num_cliente_demorados
    global plotDemora
    global plotClientesDem
    global plotDemoraProm
    if (num_en_cola2==0):
        estado_server2_A=0
        tiempo_proximo_evento[4]= 1000000000000000000000
    else:
        num_en_cola2=num_en_cola2-1
        demora = tiempo - tiempo_arrivo2[1]
        total_de_demoras = total_de_demoras + demora
        num_cliente_demorados= num_cliente_demorados+1
        plotDemora.append(demora)
        plotDemoraProm.append(np.mean(plotDemora))
        plotClientesDem.append(num_cliente_demorados)
        tiempo_proximo_evento[4]= tiempo + expon(media_servicio2_A)
        if num_en_cola2==0:
            tiempo_arrivo2[1] = 0
        for i in range (1, num_en_cola2+1 ):
            tiempo_arrivo2[i] = tiempo_arrivo2[i+1]


def partida2_B():
    global tiempo
    global num_en_cola2
    global tiempo_arrivo2
    global estado_server2_B
    global media_servicio2_B
    global tiempo_proximo_evento
    global total_de_demoras
    global num_cliente_demorados
    global plotDemora
    global plotClientesDem
    global plotDemoraProm
    if (num_en_cola2==0):
        estado_server2_B=0
        tiempo_proximo_evento[5]= 1000000000000000000000
    else:
        num_en_cola2=num_en_cola2-1
        demora = tiempo - tiempo_arrivo2[1]
        total_de_demoras = total_de_demoras + demora
        num_cliente_demorados= num_cliente_demorados+1
        plotDemora.append(demora)
        plotDemoraProm.append(np.mean(plotDemora))
        plotClientesDem.append(num_cliente_demorados)
        tiempo_proximo_evento[5]= tiempo + expon(media_servicio2_B)
        if num_en_cola2==0:
            tiempo_arrivo2[1] = 0
        for i in range (1, num_en_cola2+1 ):
            tiempo_arrivo2[i] = tiempo_arrivo2[i+1]


def partida2_C():
    global tiempo
    global num_en_cola2
    global tiempo_arrivo2
    global estado_server2_C
    global media_servicio2_C
    global tiempo_proximo_evento
    global total_de_demoras
    global num_cliente_demorados
    global plotDemora
    global plotClientesDem
    global plotDemoraProm
    if (num_en_cola2==0):
        estado_server2_C=0
        tiempo_proximo_evento[6]= 1000000000000000000000
    else:
        num_en_cola2=num_en_cola2-1
        demora = tiempo - tiempo_arrivo2[1]
        total_de_demoras = total_de_demoras + demora
        num_cliente_demorados= num_cliente_demorados+1
        plotDemora.append(demora)
        plotDemoraProm.append(np.mean(plotDemora))
        plotClientesDem.append(num_cliente_demorados)
        tiempo_proximo_evento[6]= tiempo + expon(media_servicio2_C)
        if num_en_cola2==0:
            tiempo_arrivo2[1] = 0
        for i in range (1, num_en_cola2+1 ):
            tiempo_arrivo2[i] = tiempo_arrivo2[i+1]

def actualizar_estadisticos():
    global tiempo
    global tiempo_ultimo_evento
    global area_num_en_cola1_A
    global area_num_en_cola1_B
    global area_num_en_cola2
    global area_estado_server1_A
    global area_estado_server1_B
    global area_estado_server2_A
    global area_estado_server2_B
    global area_estado_server2_C
    global num_en_cola
    global num_en_cola1_A
    global num_en_cola1_B
    global num_en_cola2
    global estado_server1_A
    global estado_server1_B
    global estado_server2_A
    global estado_server2_B
    global estado_server2_C
    global plotTiempo1A
    global plotTiempo1B
    global plotTiempo2
    global plotCola1A
    global plotCola1B
    global plotCola2
    global plotServ1A
    global plotServ1B
    global plotServ2A
    global plotServ2B
    global plotServ2C
    global plotCola1AProm
    global plotCola1BProm
    global plotCola2Prom
    global plotServ1AProm
    global plotServ1BProm
    global plotServ2AProm
    global plotServ2BProm
    global plotServ2CProm
    tiempo_desde_ultimo_evento= tiempo - tiempo_ultimo_evento
    tiempo_ultimo_evento= tiempo
    plotTiempo1A.append(tiempo)
    plotTiempo1B.append(tiempo)
    plotTiempo2.append(tiempo)
    plotCola1A.append(num_en_cola1_A)
    plotCola1B.append(num_en_cola1_B)
    plotCola2.append(num_en_cola2)
    plotCola2Prom.append(np.mean(plotCola2))
    plotCola1AProm.append(np.sum(plotCola1A)/len(plotCola1A))
    plotCola1BProm.append(np.mean(plotCola1B))
    plotServ1A.append(estado_server1_A)
    plotServ1B.append(estado_server1_B)
    plotServ2A.append(estado_server2_A)
    plotServ2B.append(estado_server2_B)
    plotServ2C.append(estado_server2_C)
    plotServ1AProm.append(np.mean(plotServ1A))
    plotServ1BProm.append(np.mean(plotServ1B))
    plotServ2AProm.append(np.mean(plotServ2A))
    plotServ2BProm.append(np.mean(plotServ2B))
    plotServ2CProm.append(np.mean(plotServ2C))
    area_num_en_cola1_A = area_num_en_cola1_A + (num_en_cola1_A * tiempo_desde_ultimo_evento)
    area_num_en_cola1_B = area_num_en_cola1_B + (num_en_cola1_B * tiempo_desde_ultimo_evento)
    area_num_en_cola2 = area_num_en_cola2 + (num_en_cola2 * tiempo_desde_ultimo_evento)
    area_estado_server1_A = area_estado_server1_A + estado_server1_A * tiempo_desde_ultimo_evento
    area_estado_server1_B = area_estado_server1_B + estado_server1_B * tiempo_desde_ultimo_evento
    area_estado_server2_A = area_estado_server2_A + estado_server2_A * tiempo_desde_ultimo_evento
    area_estado_server2_B = area_estado_server2_B + estado_server2_B * tiempo_desde_ultimo_evento
    area_estado_server2_C = area_estado_server2_C + estado_server2_C * tiempo_desde_ultimo_evento


def reportaje():
    global total_de_demoras
    global num_cliente_demorados
    global area_num_en_cola1_A
    global area_num_en_cola1_B
    global area_num_en_cola2
    global area_estado_server1_A
    global area_estado_server1_B
    global area_estado_server2_A
    global area_estado_server2_B
    global area_estado_server2_C
    global tiempo
    global plotDemora
    global plotClientesDem
    global plotTiempo1A
    global plotTiempo1B
    global plotTiempo2
    global plotCola1A
    global plotCola1B
    global plotCola2
    global plotServ1A
    global plotServ1B
    global plotServ2A
    global plotServ2B
    global plotServ2C
    print("Promedio de demoras en cola:" + str((total_de_demoras)/ (num_cliente_demorados)) + "Horas")
    print("Numero promedio de clientes en cola 1 A:" + str (area_num_en_cola1_A /tiempo))
    print("Numero promedio de clientes en cola 1 B:" + str (area_num_en_cola1_B /tiempo))
    print("Numero promedio de clientes en cola 2:" + str (area_num_en_cola2 /tiempo))
    print("Utilizacion del server 1 A:" + str(area_estado_server1_A/tiempo))
    print("Utilizacion del server 1 B:" + str(area_estado_server1_B/tiempo))
    print("Utilizacion del server 2 A:" + str(area_estado_server2_A/tiempo))
    print("Utilizacion del server 2 B:" + str(area_estado_server2_B / tiempo))
    print("Utilizacion del server 2 C:" + str(area_estado_server2_C / tiempo))
    print("Tiempo de simulacion termino:" + str(tiempo))

    plt.plot(plotClientesDem, plotDemora, 1)
    plt.ylabel("Total de demoras")
    plt.xlabel("Numero de clientes que completaron su demora")
    plt.show()

    plt.plot(plotTiempo1A, plotCola1A, 2)
    plt.ylabel("Numero de clientes en cola 1 A")
    plt.xlabel("Tiempo")
    plt.show()

    plt.plot(plotTiempo1B, plotCola1B, 3)
    plt.ylabel("Numero de clientes en cola 1 B")
    plt.xlabel("Tiempo")
    plt.show()

    plt.plot(plotTiempo2, plotCola2, 4)
    plt.ylabel("Numero de clientes en cola 2")
    plt.xlabel("Tiempo")
    plt.show()

    plt.plot(plotTiempo2, plotServ1A, 5)
    plt.ylabel("Uso del servidor 1 A ")
    plt.xlabel("Tiempo")
    plt.show()

    plt.plot(plotTiempo2, plotServ1B, 6)
    plt.ylabel("Uso del servidor 1 B ")
    plt.xlabel("Tiempo")
    plt.show()

    plt.plot(plotTiempo2, plotServ2A, 7)
    plt.ylabel("Uso del servidor 2 A ")
    plt.xlabel("Tiempo")
    plt.show()

    plt.plot(plotTiempo2, plotServ2B, 8)
    plt.ylabel("Uso del servidor 2 B ")
    plt.xlabel("Tiempo")
    plt.show()

    plt.plot(plotTiempo2, plotServ2C, 9)
    plt.ylabel("Uso del servidor 2 C ")
    plt.xlabel("Tiempo")
    plt.show()


def main():
    global num_eventos
    global mediana_servicio
    global mediana_entrearrivos
    global num_demora_requerido
    global num_cliente_demorados
    global sig_tipo_evento
    #Especificar el numero de eventos para la funcion timing
    num_eventos = 6
    # Mostrar los parametros iniciales
    print("----------------------------COMIENZO SIMULACION MM2MM3--------------------------")
    print("Tiempo de mediana entre arrivos:" +str(media_entrearrivos) + " Horas")
    print("Tiempo de mediana de servicio server 1_A:" +str(media_servicio1_A) + " Horas")
    print("Tiempo de mediana de servicio server 1_B:" + str(media_servicio1_B) + " Horas")
    print("Tiempo de mediana de servicio server 2_A:" + str(media_servicio2_A) + " Horas")
    print("Tiempo de mediana de servicio server 2_B:" + str(media_servicio2_B) + " Horas")
    print("Tiempo de mediana de servicio server 2_C:" + str(media_servicio2_C) + " Horas")
    print("Numero de clientes: " + str(num_demora_requerido))
    #inicializar la simulacion
    inicializar()
    #Correr la simulacion mientras mas numeros de demora sean requeridos
    while (num_cliente_demorados< num_demora_requerido):
        #determinar el siguiente evento
        timing()
        # Actualizar promedioas estadisticos
        actualizar_estadisticos()
        if sig_tipo_evento == 1:
            arrivo1()
        elif sig_tipo_evento == 2:
            partida1_A()
            arrivo2()
        elif sig_tipo_evento == 3:
            partida1_B()
            arrivo2()
        elif sig_tipo_evento == 4:
            partida2_A()
        elif sig_tipo_evento == 5:
            partida2_B()
        elif sig_tipo_evento == 6:
            partida2_C()
        else:
            print("Error al detectar tipo de evento")
    reportaje()


global promDemTotal
promDemTotal = 0
global num_prom_cola1_ATotal
num_prom_cola1_ATotal = 0
global num_prom_cola1_BTotal
num_prom_cola1_BTotal = 0
global num_prom_cola2Total
num_prom_cola2Total = 0
global utilizacionServer1_Atotal
utilizacionServer1_Atotal =0
global utilizacionServer1_Btotal
utilizacionServer1_Btotal = 0
global utilizacionServer2_Atotal
utilizacionServer2_Atotal = 0
global utilizacionServer2_Btotal
utilizacionServer2_Btotal = 0
global utilizacionServer2_Ctotal
utilizacionServer2_Ctotal = 0

def salvarEstadisticos():
    global total_de_demoras
    global num_cliente_demorados
    global area_num_en_cola1_A
    global area_num_en_cola1_B
    global area_num_en_cola2
    global area_estado_server1_A
    global area_estado_server1_B
    global area_estado_server2_A
    global area_estado_server2_B
    global area_estado_server2_C
    global tiempo
    global promDemTotal
    global num_prom_cola1_ATotal
    global num_prom_cola1_BTotal
    global num_prom_cola2Total
    global utilizacionServer1_Atotal
    global utilizacionServer1_Btotal
    global utilizacionServer2_Atotal
    global utilizacionServer2_Btotal
    global utilizacionServer2_Ctotal
    global plotDemoraProm
    global plotClientesDem
    global plotCola1AProm
    global plotTiempo1A
    global plotTiempo1B
    global plotTiempo2
    global plotCola1AProm
    global plotCola1BProm
    global plotCola2Prom
    global plotServ1AProm
    global plotServ1BProm
    global plotServ2AProm
    global plotServ2BProm
    global plotServ2CProm
    promDemTotal = promDemTotal + total_de_demoras/num_cliente_demorados
    num_prom_cola1_ATotal = num_prom_cola1_ATotal + area_num_en_cola1_A /tiempo
    num_prom_cola1_BTotal = num_prom_cola1_BTotal + area_num_en_cola1_B /tiempo
    num_prom_cola2Total = num_prom_cola2Total + area_num_en_cola2 /tiempo
    utilizacionServer1_Atotal = utilizacionServer1_Atotal + area_estado_server1_A/tiempo
    utilizacionServer1_Btotal = utilizacionServer1_Btotal + area_estado_server1_B / tiempo
    utilizacionServer2_Atotal = utilizacionServer2_Atotal + area_estado_server2_A/tiempo
    utilizacionServer2_Btotal = utilizacionServer2_Btotal + area_estado_server2_B / tiempo
    utilizacionServer2_Ctotal = utilizacionServer2_Ctotal + area_estado_server2_C / tiempo

    #plt.plot(plotClientesDem, plotDemoraProm, 1)
    #plt.ylabel("Promedio de demoras")
    #plt.xlabel("Numero de clientes que completaron su demora")

    #plt.plot(plotTiempo1A, plotCola1AProm, 1)
    #plt.ylabel("Numero de clientes en cola 1 A")
    #plt.xlabel("Tiempo")
    #plt.ylim(0, 20)


    #plt.plot(plotTiempo1A , plotCola1BProm, 1)
    #plt.ylabel("Numero de clientes en cola 1 B")
    #plt.xlabel("Tiempo")
    #plt.ylim(0, 20)

    #plt.plot(plotTiempo1A, plotCola2Prom, 1)
    #plt.ylabel("Numero de clientes en cola 2")
    #plt.xlabel("Tiempo")
    #plt.ylim(0, 20)

    #plt.plot(plotTiempo1A, plotServ1AProm, 1)
    #plt.ylabel("uso del servidor 1 A")
    #plt.xlabel("Tiempo")

    #plt.plot(plotTiempo1B, plotServ1BProm)
    #plt.ylabel("uso del servidor 1 B")
    #plt.xlabel("Tiempo")

    #plt.plot(plotTiempo1A, plotServ2AProm, 1)
    #plt.ylabel("uso del servidor 2 A")
    #plt.xlabel("Tiempo")

    #plt.plot(plotTiempo1A, plotServ2BProm, 1)
    #plt.ylabel("uso del servidor 2 B")
    #plt.xlabel("Tiempo")

    #plt.plot(plotTiempo1A, plotServ2CProm, 1)
    #plt.ylabel("uso del servidor 2 C")
    #plt.xlabel("Tiempo")



def mainCorrida():
    global num_eventos
    global mediana_servicio
    global mediana_entrearrivos
    global num_demora_requerido
    global num_cliente_demorados
    global sig_tipo_evento
    num_eventos = 6
    inicializar()
    while (num_cliente_demorados< num_demora_requerido):
        timing()
        actualizar_estadisticos()
        if sig_tipo_evento == 1:
            arrivo1()
        elif sig_tipo_evento == 2:
            partida1_A()
            arrivo2()
        elif sig_tipo_evento == 3:
            partida1_B()
            arrivo2()
        elif sig_tipo_evento == 4:
            partida2_A()
        elif sig_tipo_evento == 5:
            partida2_B()
        elif sig_tipo_evento == 6:
            partida2_C()
        else:
            print("Error al detectar tipo de evento")
    salvarEstadisticos()

def reportajeCorrida(n):
    global promDemTotal
    global num_prom_cola1_ATotal
    global num_prom_cola1_BTotal
    global num_prom_cola2Total
    global utilizacionServer1_Atotal
    global utilizacionServer1_Btotal
    global utilizacionServer2_Atotal
    global utilizacionServer2_Btotal
    global utilizacionServer2_Ctotal
    plt.show()
    print("Promedio de demoras total en cola:" + str(promDemTotal/n) + " horas")
    print("Numero promedio de clientes en cola 1 A Total:" + str (num_prom_cola1_ATotal/n))
    print("Numero promedio de clientes en cola 1 B Total:" + str ( num_prom_cola1_BTotal /n))
    print("Numero promedio de clientes en cola 2 Total:" + str ( num_prom_cola2Total/n))
    print("Utilizacion del server 1 A Total:" + str(utilizacionServer1_Atotal/n))
    print("Utilizacion del server 1 B Total:" + str(utilizacionServer1_Btotal/n))
    print("Utilizacion del server 2 A Total:" + str(utilizacionServer2_Atotal/n))
    print("Utilizacion del server 2 B Total:" + str(utilizacionServer2_Btotal/n))
    print("Utilizacion del server 2 C Total:" + str(utilizacionServer2_Ctotal/n))



def corrida():
    for c in range(0, 4):
        mainCorrida()
    reportajeCorrida(4)

corrida()

#main()