import paho.mqtt.client as mqtt
#pip3 install paho-mqtt

payload="Hello"
topic="IOT/test"
client = mqtt.Client()
client.connect('http://34.100.205.14/',1883,60)
(rc,mid)=client.publish(topic,payload);
client.disconnect();
