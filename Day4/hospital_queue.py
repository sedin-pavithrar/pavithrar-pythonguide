import heapq

class Hospital_Emergency:

    def __init__ (self):
        self.counter = 0
        self.heap = []

    def admit(self, name, age, severity):
        heapq.heappush(self.heap,(severity,self.counter,name,age))
        self.counter+=1

        print(f"Admitted: {name} | Age: {age} |  Severity: {severity}")

    def treat_next(self):
        if not self.heap:
            print("No patients waiting")
            return 
        
        severity,_,name,age = heapq.heappop(self.heap)

        print(f"Treating :{name} | Age: {age} | Severity:{severity}")
        
    def show_waiting(self):
        if not self.heap:
            print("No patients waiting")
            return
        print("\n Waiting Patients:")

        for severity,order,name,age in sorted(self.heap):
            print(f"Name:{name} | Age:{age} | Severity:{severity}")
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

    # print("\n--- Condition Worsened ---")
    # ward.bump_priority("Priya")
    ward.show_waiting()
    
if __name__ == "__main__":
    main()

