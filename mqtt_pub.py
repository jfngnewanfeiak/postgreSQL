from paho.mqtt import client as mqtt

import time

broker = "192.168.11.2"
broker = "10.64.10.97"
port = 1883
topic ="python/mqtt"
client_id = "0"
username = "user"
password = "password"

def connect_mqtt()->mqtt:
    def on_connect(client,userdata,flag,rc):
        if rc == 0:
            print("Connected to Mqtt Broker")
        else:
            print("Failed to connect mqtt broker")
    
    client = mqtt.Client()
    client.username_pw_set(username,password)
    client.on_connect = on_connect
    client.connect(broker,port)
    return client

def publish(client):
    msg_cnt = 0
    while True:
        time.sleep(1)
        msg = f"msgs: {msg_cnt}"
        result = client.publish(topic,msg)

        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send msg to topic {topic}")
        msg_cnt += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ =="__main__":
    run()