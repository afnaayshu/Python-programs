class Elevator:
    # Set occupancy limit to 8
    occupancy_limit = 8
    
    # Initialize Elevator with occupants and floor
    def __init__(self, occupants=0, floor=0):
        self.floor = floor
        # Check if occupants exceed occupancy limit
        if occupants <= Elevator.occupancy_limit:
            self.occupants = occupants
        else:
            self.occupants = Elevator.occupancy_limit
            # Print error message for excess occupants
            print("Too many occupants, {0} left outside.".format(occupants - Elevator.occupancy_limit))
    
    # Method to add occupants
    def add_occupants(self, num):
        # Add number of occupants
        self.occupants += num
        # Check if occupants exceed occupancy limit
        if self.occupants > Elevator.occupancy_limit:
            # Print error message for excess occupants
            print("Too many occupants, {0} left outside.".format(self.occupants - Elevator.occupancy_limit))
            self.occupants = Elevator.occupancy_limit
            
    # Method to remove occupants
    def sub_occupants(self, num):
        # Check if occupants to be removed is valid
        if self.occupants - num >= 0:
            self.occupants -= num
        else:
            # Print error message if occupants to be removed exceed current occupants
            print("Elevator empty")
            self.occupants = 0
           
    # Method to go to a specified floor
    def goto_floor(self, floor):
        # Check if floor is valid
        if floor < -5 or floor > 50:
            # Print error message for invalid floor
            print('Floor {0} does not exist.'.format(floor))
        else:
            self.floor = floor
            
# Create Elevator instances and test their methods
elevator1 = Elevator(6)
elevator1.add_occupants(7)
elevator2 = Elevator(11)
elevator1.goto_floor(20)
elevator1.sub_occupants(8)
elevator2.goto_floor(99)

# Print the current state of the elevators
print(elevator1.__dict__)
print(elevator2.__dict__)
