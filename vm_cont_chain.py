import paho.mqtt.client as mqtt
import time
import socket

def on_connect(client, userdata, flags, rc):
    """Once our client has successfully connected, it makes sense to subscribe to
    all the topics of interest. Also, subscribing in on_connect() means that, 
    if we lose the connection and the library reconnects for us, this callback
    will be called again thus renewing the subscriptions"""

    print("Connected to server (i.e., broker) with result code "+str(rc))
    #replace user with your USC username in all subscriptions
    client.subscribe("damasco/ping")


def on_message_receive(client, userdata, message):
    print(message.payload)
    payload = int(message.payload) + 1
    time.sleep(1)
    client.publish("damasco/pong", str(payload))

if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    client.on_message = on_message_receive
    #attach a default callback which we defined above for incoming mqtt messages

    client.connect(host="172.20.10.7", port=1883, keepalive=60)
    client.loop_start()

    while True:
        client.on_message = on_message_receive