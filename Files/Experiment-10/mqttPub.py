import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("192.168.225.77",1883,60)

while True:
	x = input("Enter string to publish : ")
	client.publish("test", x, qos=0, retain=False)
