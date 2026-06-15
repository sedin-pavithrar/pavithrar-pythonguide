# HashMap (Python dict) caching computed fares keyed by route string. First lookup = MISS (compute+ store).
#  Subsequent = HIT (instant O(1) return).
#  Tracks search frequency per route. This is the 
# exact caching pattern used by Ola and Uber to avoid recomputing surge prices.
# Problem
# Fare caching by route. MISS calculates and saves. HIT returns instantly. 
# Track frequency, show top 3 routes.
# Example
# Input / Code Output
# fc = FareCache()
# fc.search("Pune->Mumbai")
# fc.search("Pune->Mumbai")
# MISS -- Rs.1,776 [saved]
# HIT -- Rs.1,776 (instant)
# Constraints
# Route not found -> "Route not found"
# top_routes sorted by frequency desc
# clear_cache() preserves frequency data



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

def top_routes(n=3):
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
     print(clear_cache())

    


if __name__ == "__main__":
     main()
     



     
     
     

    
    

    
    
    
