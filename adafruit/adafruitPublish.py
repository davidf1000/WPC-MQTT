import paho.mqtt.client as mqtt #import the client1
import time
broker_address="io.adafruit.com"

#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("hai") #create new instance
client.username_pw_set("davidfauzi", "0f7873c4c7bf48bb95e79d4112889e8e")
client.connect(broker_address) #connect to broker
i=0
while True:
    client.publish("davidfauzi/feeds/sensorsuhu",i)#publish
    i+=1
    time.sleep(5)