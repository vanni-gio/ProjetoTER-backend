import ssl
import paho.mqtt.client as mqtt
TLS_CERT_PATH = '/etc/mosquitto/certs/server.crt'
#Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))

# Message receiving callback
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()

# Specify callback function
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("giovanni", "geladeira0")

# Establish a connection
# client.tls_set(ca_certs=TLS_CERT_PATH, cert_reqs=ssl.CERT_REQUIRED,
#                             tls_version=ssl.PROTOCOL_TLSv1_2)
# client.tls_insecure_set(False)
client.connect('127.0.0.1', 1883)
# Publish a message
client.subscribe('emqtt')
print('Inscrito em emqtt')
client.loop_forever()