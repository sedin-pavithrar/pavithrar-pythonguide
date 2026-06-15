RATE_PER_KM = 12

distances = {
    "pune<->mumbai": 148,
    "mumbai<->goa": 590,
    "delhi<->agra": 233,
    "bangalore<->mysore": 145
}

cache = {}
frequency = {}

def search(source,destination):
     route = f"{source.strip().lower()}<->{destination.strip().lower()}"

     if route not in distances:
          reverse_route = (f"{destination.strip().lower()}<->"f"{source.strip().lower()}")
          if reverse_route in distances:
               route = reverse_route
          else:
               return "Route not found"
    
     frequency[route] = frequency.get(route,0)+1
    
     if route in cache:
          fare = cache[route]
          return f"HIT -- Rs.{fare:.2f}"
     
     fare = distances[route]* RATE_PER_KM
     cache[route] = fare
     return f"MISS -- Rs.{fare:.2f} saved"

def top_routes(n):
          if cache:
               sorted_route = sorted(frequency.items(),key= lambda item:item[1] , reverse = True)
               return sorted_route[:n]
          else:
               return " Empty"

def clear_cache():
        if cache:
          cache.clear()
          return "Cache Cleared" 
        else:
             return "Route Empty"

def main():
     while True:
          source = input("\nEnter source city (or 'exit'): ")
          if source.lower() == "exit":
              break
          
          destination = input("Enter destination city: ")
          print(search(source, destination))
 
     
     print("Top Routes are ",top_routes(2))
    #  isclearcache = int(input("You really want to clear catch? \n Enter 1 if you want to or else enter 0: "))
    #  if isclearcache:
     print(clear_cache())
    #  else:
    #       print("Cache not cleared")
    


if __name__ == "__main__":
     main()
     



     
     
     

    
    

    
    
    
