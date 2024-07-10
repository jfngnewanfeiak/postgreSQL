from paho.mqtt import client as mqtt

class MQTT:
    def __init__(self) -> None:
        self.broker = ""
        self.port = 1883 #default settings
        self.topic = ""
        self.username = "user"
        self.password = "password"

    
    def borker_setter(self,broker_ip:str):
        self.broker = broker_ip
    
    def topic_setter(self,topic_name):
        self.topic = topic_name
    
    def connect_mqtt(self)->mqtt:
        def __on_connect(client,ud,flag,rc):
            if rc == 0:
                print("Connected to Mqtt Broker")
            else:
                print("Failed to connect mqtt broker")
        
        client = mqtt.Client()
        client.username_pw_set(self.username,self.password)
        client.on_connect = __on_connect
        client.connect(self.broker,self.port)
        return client


    def subscribe(self,client:mqtt):
        def __on_message(client,ud,msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
        client.subscribe(self.topic)
        client.on_message = __on_message
        
            