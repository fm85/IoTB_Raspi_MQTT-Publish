#!/usr/bin/env python3

"""
------------------------------------------------------------------
Projekt:         MQTT Client Beispiel
Beschreibung:    Publiziert exemlarisch einen Sensorwert über MQTT
Abhängigkeiten:  paho-mqtt (vorher mit pip3 installieren)
Institution:     GBS
Verfasser:       F.Reifler
Datum:           27.08.2020
------------------------------------------------------------------
"""

import paho.mqtt.client as mqtt
import Adafruit_DHT
import socket
import sys
import time

myClient = mqtt.Client()
mySensorType = 11
mySensorPin = 4

def on_connect(client, userdata, flags, rc):
    print("Connected with result code" + str(rc))

def initMQTTClient():
    myClient.on_connect = on_connect
    keepalive = 60
    myClient.connect("172.20.1.31",1883,keepalive)
    myClient.loop_start()

def getHostname():
    return socket.gethostname()

def start():
    try:
        initMQTTClient()
        topic = getHostname() + "/temperature"
        print("Publishing with the following Topic:" + topic)
        while(True):
            time.sleep(2)
            humidity, temperature = Adafruit_DHT.read_retry(mySensorType, mySensorPin)
            message = temperature
            myClient.publish(topic,message)
    except (KeyboardInterrupt, SystemExit):
        print("Interrupted")
        sys.exit(1)

start()
