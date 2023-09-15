import random
from datetime import datetime

# explain the code in comments
from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from device import Device
from dashboard import Dashboard

def main():
    sensor = Sensor(0, 100)
    data_processor = DataProcessor()
    communication = Communication("https://central-server.example.com")
    
    
    device = Device(sensor, data_processor, communication)
    dashboard = Dashboard()

    device.collect_data(10)
    processed_data = device.process_data()
    print ('Dolfi', processed_data)
    device.send_data_to_server(processed_data)
    device.receive_data_from_server()

    print(dashboard.display_data(device.data))
    print(dashboard.display_analytics(processed_data))

if __name__ == "__main__": #this define whats the main program in our case is function main , but for example if the main program is a module that is imported here like "Device"
                            #and we call that module here then our main program will be Device and it will execute first
    main()

