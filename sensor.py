import random
from datetime import datetime

## create a class that simulate a sensor (a class that generate a random data), the data should be send with the timestamp
class Sensor:
    
    def __init__(self, min_val , max_val):
        self.min_val = min_val
        self.max_val = max_val
        self.randSensor = random.randint(min_val , max_val)
        
    
    def read_data(self):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        sensorTuple = (timestamp , self.randSensor)
        return sensorTuple

    

    
    
    
    