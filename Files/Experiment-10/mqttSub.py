import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connect with result code "+str(rc))
	client.subscribe("test")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org",1883,60)

client.loop_forever()
