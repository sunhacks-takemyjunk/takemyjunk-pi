import paho.mqtt.client as mqtt
import ssl
import json

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

# Set the callback
client.on_message = on_message

# Configure the client with the AWS IoT Core endpoint and certificates
client.tls_set(ca_certs="root-CA.crt",
               certfile="certificate.pem.crt",
               keyfile="private.pem.key",
               tls_version=ssl.PROTOCOL_TLSv1_2,
               ciphers=None)

# Connect to the AWS IoT Core endpoint
client.connect("your-iot-endpoint.amazonaws.com", port=8883)

# Subscribe to the IoT topic
client.subscribe("your/iot/topic")

# Start the MQTT client
client.loop_forever()