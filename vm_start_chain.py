"""
Team: Jacob Damasco and Kobe Kodachi
"""
import paho.mqtt.client as mqtt
import time
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    client.subscribe("damasco/pong")


def on_message_receive_back(client, userdata, msg):
    print(msg.payload)
    payload = int(msg.payload) + 1
    time.sleep(1)
    client.publish("damasco/ping", str(payload))


if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    client.on_message = on_message_receive_back
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python. For example:
    
    `client.connect("eclipse.usc.edu", 11000, 60)` 
    
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host="172.20.10.7", port=1883, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1)
    client.publish("damasco/ping", "0")

    while True:
        time.sleep(1)