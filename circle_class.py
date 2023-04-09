import math as m  # Import math module as 'm'

class Circle:  # Define 'Circle' class
    def __init__(self,radius):  # Constructor method with 'radius' parameter
        self.radius = radius  # Initialize instance variable 'radius' with the given parameter
    
    def area(self):  # Method to calculate the area of the circle
        return m.pi*self.radius**2  # Return the area of the circle using 'pi' constant and 'radius' squared
    
    def circum(self):  # Method to calculate the circumference of the circle
         return 2*m.pi*self.radius  # Return the circumference of the circle using 'pi' constant and 'radius' multiplied by 2
    
    def change_radius(self,new_radius):  # Method to change the radius of the circle
        self.radius = new_radius  # Set the instance variable 'radius' to the new value given as parameter

circle = Circle(1)  # Create an instance of 'Circle' class with radius=1
while True:  # Start an infinite loop
    radius = float(input("Enter radius : "))  # Prompt user to enter new radius
    circle.change_radius(radius)  # Call the method to change the radius of the circle with the new value entered
    print('Area : ', circle.area())  # Print the updated area of the circle
    print('Circumference : ', circle.circum())  # Print the updated circumference of the circle

    
    
