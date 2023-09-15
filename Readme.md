# Package Explanation

- Sensor class: This class simulates a sensor that generates random data within a specified range. The `read_data` method returns a tuple containing the current timestamp and a randomly generated data point.

- DataProcessor class: This class processes the data collected from the Sensor class. It calculates the average, minimum, and maximum values from a list of data points.

- Communication class: This class simulates the communication between the IoT device and a central server. The `send_data` method takes a data payload as input and simulates sending the data to the server. The `receive_data` method simulates receiving data from the server. 

- Device class: This class represents an IoT device. It has a Sensor, DataProcessor, and Communication instance as its attributes. The `collect_data` method reads data from the Sensor instance and stores it in a list. The `process_data` method processes the collected data using the DataProcessor instance and sends the results to the central server using the Communication instance. 

- Dashboard class: This class represents a monitoring dashboard for displaying sensor data and analytics results. The `display_data` method takes a list of data points and displays them in a formatted manner. The `display_analytics` method takes the average, minimum, and maximum values calculated by the DataProcessor and displays them.

- Unit tests: The provided test suite covers each class and its methods. It checks the functionality of the Sensor, DataProcessor, Communication, Device, and Dashboard classes. 

- Main.py file: This is the main script that ties everything together. It creates instances of the Sensor, DataProcessor, Communication, Device, and Dashboard classes, and then simulates the operation of an IoT device by collecting data, processing it, sending it to the central server, and displaying it on the dashboard.