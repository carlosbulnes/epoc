#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias de ROS
import rospy
import numpy as np
import roslib; roslib.load_manifest('epoc')
from epoc.msg import Frecuencias

# Librerias de Emokit
from emotiv import Emotiv
import platform
if platform.system() == "Windows":
    import socket  # Needed to prevent gevent crashing on Windows. (surfly / gevent issue #459)
import gevent

def obtenerDatos(datos):
    """ Obtiene los datos leidos por el Emotiv Epoc y los almacena y retorna en la lista datos[] """
    
    # Obtiene el paquete del Epoc
    packet = headset.dequeue()
    
    # Obtiene los datos que vienen como parte del paquete obtenido
    datos.append(packet.sensors['F3']['value'])
    datos.append(packet.sensors['FC5']['value'])
    datos.append(packet.sensors['AF3']['value'])
    datos.append(packet.sensors['F7']['value'])
    datos.append(packet.sensors['T7']['value'])
    datos.append(packet.sensors['P7']['value'])
    datos.append(packet.sensors['O1']['value'])
    datos.append(packet.sensors['O2']['value'])
    datos.append(packet.sensors['P8']['value'])
    datos.append(packet.sensors['T8']['value'])
    datos.append(packet.sensors['F8']['value'])
    datos.append(packet.sensors['AF4']['value'])
    datos.append(packet.sensors['FC6']['value'])
    datos.append(packet.sensors['F4']['value'])
    print datos
    gevent.sleep(0)    

def talker():
    """ Funcion para publicar los mensajes en ROS """
    
    # Configura la funcion para que publique los mensajes.
    # El primer parametro es el nombre para identificar el mensaje, 
    # el segundo es el nombre del mensaje definido en la carpeta msg del proyecto
    pub = rospy.Publisher('mensaje', Frecuencias)
    rospy.init_node('talker', anonymous=True, disable_signals=False) # Inicializa el nodo
    rate = rospy.Rate(10) # 10hz # Define la velocidad de publicacion en ROS

    # Publicara los mensajes mientras que no se apague la comunicacion
    while not rospy.is_shutdown():
        datos = []
        hello_str = "%s" % rospy.get_time()
        rospy.loginfo(hello_str)
        
        obtenerDatos(datos) # Obtiene los datos del Epoc
        
        pub.publish(datos) # Publica el mensaje en ROS, el parametro debe ser del mismo tipo definido en el archivo de mensaje
        rate.sleep()

        
if __name__ == '__main__':
    
    # Inicia la comunicacion con el Epoc por medio del Emokit
    headset = Emotiv() 
    gevent.spawn(headset.setup)
    gevent.sleep(0)    
    
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        headset.close()
    finally:
        headset.close()    