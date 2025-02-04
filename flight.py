class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]

    def add_passengers(self,name):
        if not self.openseats:
          return False
        else:
           self.passengers.append(name)
           return True
       
    def openseats(self):
        return self.capacity-len(self.passengers)
        

n=int(input('what is the max capacity:'))
flight=Flight(n)
people=[]
while True:
    person=input("enter person name (or enter 'done' to finish):")
    people.append(person)
    if person.lower()=='done':
        break
people.sort()
for person in people:
    if flight.add_passengers(person):
        print(f"the person {person} has successfully booked ticket")
    else:
        print(f"the person {person} has no confirmed seat")

