import paho.mqtt.client as mqtt
import ssl
import json
import logging

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Define the MQTT client
client = mqtt.Client()

# Define the callback for when a message is received
def on_message(client, userdata, message):
    payload = json.loads(message.payload)
    action = payload.get('action')
    if action == "open_door":
        # Perform the hardware action here
        print("Opening the door")
    elif action == "close_door":
        # Perform the hardware action here
        print("Closing the door")

# Set the callback for message reception
client.on_message = on_message

# Define the callback for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        client.subscribe("pi_tasks")
    else:
        print(f"Connection failed with code {rc}")

# Set the callback for connection
client.on_connect = on_connect

# Configure the client with the AWS IoT Core endpoint and certificates
client.tls_set(ca_certs="root-CA.crt",
               certfile="takemyjunk_thing.cert.pem",
               keyfile="takemyjunk_thing.private.key",
               tls_version=ssl.PROTOCOL_TLSv1_2,
               ciphers=None)

# Connect to the AWS IoT Core endpoint
print("Connecting to AWS IoT Core endpoint...")
client.connect("at6fo26c2tah4-ats.iot.us-east-1.amazonaws.com", port=8883)

# Start the MQTT client
print("Starting MQTT client loop...")
client.loop_forever()