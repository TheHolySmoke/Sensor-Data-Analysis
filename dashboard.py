from pickle import FALSE
import random
from datetime import datetime

class Dashboard:
    def display_data(self, data):
        
        result = "\n\nTimestamp             Sensor Data \n ________________________________\n"
        for e in data:
            result += f"{e[0]}       {e[1]}\n"
        return result
        
# compelet this function to display the data

    def display_analytics(self, analytics):
        result = "Analytics Results \n ________________________________\n"
        result += f" Average: {analytics[0]}\n Minimum: {analytics[1]}\n Maximum: {analytics[2]}"
        return result
    
# complete this function to find the max, min , average of the red data



## Bonos!
# you can also generate some figures using the data and python modules like matplotlib, etc
# if simple GUI can be used. Hint: you can use django
# any extra flavor that you think it can add to the task. Hint(use your imagination and skills)
