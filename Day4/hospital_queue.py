# Min-heap via heapq where tuple order is (severity, arrival_counter, name, age). 
# Lower severity = higher priority. 
# Same-severity patients served in arrival order via the counter tie-breaker.
# This  models real ICU triage systems and is the same algorithm behind printer job schedulers and OS task managers.
# Problem
# Patients treated by severity (1=critical) not arrival order. Always treat most critical first using heapq
#Constraints
#  Same severity -> first admitted (FIFO via counter)
#  Heap tuple: (severity, arrival_order, name, age)
# Bonus: Add bump_priority(name) that worsens a severity by 1.

import heapq

class Hospital_Emergency:

    def __init__ (self):
        self.counter = 0
        self.patients = []

    def admit(self, name, age, severity):
        heapq.heappush(self.patients,(severity,self.counter,name,age))
        self.counter+=1

        print(f"Admitted: {name} | Age: {age} |  Severity: {severity}")

    def treat_next(self):
        if self.heap_empty():
            return 
        
        severity,_,name,age = heapq.heappop(self.patients)

        print(f"Treating :{name} | Age: {age} | Severity:{severity}")
        
    def show_waiting(self):
        if self.heap_empty():
            return
       
        print("\n Waiting Patients:")

        for severity,_,name,age in sorted(self.patients):
            print(f"Name:{name} | Age:{age} | Severity:{severity}")

    def heap_empty(self):
        if not self.patients:
            print("No patients waiting")
            return 


def main():

    ward = Hospital_Emergency()
    ward.admit("Priya", 30, 3)
    ward.admit("Rahul", 45, 1)
    ward.admit("Anita", 25, 2)
    ward.admit("John", 50, 1)

    ward.show_waiting()

    print("\n--- Treating Patients ---")

    ward.treat_next()
    ward.treat_next()

    ward.show_waiting()
    
if __name__ == "__main__":
    main()

