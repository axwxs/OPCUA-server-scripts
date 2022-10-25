import datetime
import time
from threading import Thread
from opcua import ua, uamethod, Server

server = Server()
url = "opc.tcp://localhost:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_variable(addspace, "SensorValue", 8)
DI1 = node.add_variable(addspace, "DI_1", 1)
DI2 = node.add_variable(addspace, "DI_2", 0)

Param = node.add_object(addspace, "Stuff")
Time = Param.add_variable(addspace, "Time", 0)

Time.set_writable()

server.start()
print(f"Server started at {url}")

while True:
    TIME = datetime.datetime.now()
    print(TIME)
    Time.set_value(TIME)
    time.sleep(10)
    

