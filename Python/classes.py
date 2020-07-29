class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

p=Point(2,8)
##print(p.x)
##print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity=capacity
        self.passangers=[]

    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passangers)

Flight=Flight(3)

people=['Harry','Ron','Hermione','Ginny']
for person in people:
    success=Flight.add_passanger(person)
    if success:
        print(f'Added {person} to flight successfully.')
    else:
        print(f'No available seats for {person}.')
        
