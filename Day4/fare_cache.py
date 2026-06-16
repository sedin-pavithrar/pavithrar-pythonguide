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

class Fare_Price:
    RATE_PER_KM = 12

    distances = {
        "pune<->mumbai": 148,
        "mumbai<->goa": 590,
        "delhi<->agra": 233,
        "bangalore<->mysore": 145
    }

    def __init__(self):
        self.cache = {}
        self.frequency = {}

    def search(self, source, destination):

        route = f"{source.strip().lower()}<->{destination.strip().lower()}"

        if route not in self.distances:
            reverse_route = f"{destination.strip().lower()}<->{source.strip().lower()}"

            if reverse_route in self.distances:
                route = reverse_route
            else:
                return "Route not found"

        self.frequency[route] = self.frequency.get(route, 0) + 1

        if route in self.cache:
            fare = self.cache[route]
            return f"HIT -- Rs.{fare:.2f}"

        fare = self.distances[route] * self.RATE_PER_KM
        self.cache[route] = fare
        return f"MISS -- Rs.{fare:.2f} saved"

    def top_routes(self, n=3):

        if not self.frequency:
            return "Empty"

        sorted_routes = sorted(
            self.frequency.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_routes[:n]

    def clear_cache(self):
        self.cache.clear()
        return "Cache Cleared"


def main():
    fc = Fare_Price()

    while True:
        source = input("\nEnter source city (or 'exit'): ")
        if source.lower() == "exit":
            break

        destination = input("Enter destination city: ")
        print(fc.search(source, destination))

    print("\nTop Routes:", fc.top_routes(3))
    print(fc.clear_cache())


if __name__ == "__main__":
    main()
     
     
     

    
    

    
    
    
