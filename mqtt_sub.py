from paho.mqtt import client as mqtt

broker = "192.168.11.2"
broker = "10.64.10.97"
port = 1883
topic ="python/mqtt"
client_id = "0"
username = "user"
password = "password"

def connect_mqtt()->mqtt:
    def on_connect(client,ud,flag,rc):
        if rc == 0:
            print("Connected to Mqtt Broker")
        else:
            print("Failed to connect mqtt broker")
    
    client = mqtt.Client()
    client.username_pw_set(username,password)
    client.on_connect = on_connect
    client.connect(broker,port)
    return client

def subscribe(client: mqtt):
    def on_message(client,ud,msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == "__main__":
    run()