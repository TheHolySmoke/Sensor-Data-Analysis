# generate a class that takes the data from the sensor, does something with the data. Hint the timestamp needs to be addressed  as well
import statistics
from sensor import Sensor

class DataProcessor:
    
    def toInt(self, inpData):
        data = []
        for x in inpData:
            data.append(x[1])
        return data
                    

    def calculate_average(self , data):
        return statistics.mean(self.toInt(data))
    
    def calculate_min(self , data):
        return min(self.toInt(data))
    
    def calculate_max(self , data):
        return max(self.toInt(data))
        