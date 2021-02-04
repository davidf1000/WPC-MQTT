import paho.mqtt.client as mqtt #import the client1
import time
broker_address="wpcmqtt.cloud.shiftr.io"

#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("DAVID") #create new instance
client.username_pw_set("wpcmqtt", "GW5bGhof1lmPNScl")
client.connect(broker_address,1883) #connect to broker
i=0
while True:
    client.publish("WPC/iot",i)#publish
    i+=1
    time.sleep(1)