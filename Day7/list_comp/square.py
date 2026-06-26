# Rewrites 5 common for-loop patterns as comprehensions: even squares, 2D flatten, email filter, dict 
# comprehension with discount, and a generator expression for 1M item sum. sys.getsizeof 
# comparison shows generator uses ~7700x less RAM. This is the first performance optimisation 
# every Python data engineer learns.
# Problem
# Rewrite 5 data tasks with comprehensions instead of for loops. Compare memory: list vs 
# generator on 100,000 items

# 1: Squares of even numbers 1-100
import sys

class Pipelines:

    def normal_square():
        square_list = []
        for x in range(2,101,2):
                square_list.append(x**2)
        print(square_list)

    def comp_square():
        print("Squares of even numbers 1-100")
        squares  = [x**2 for x in range(2,101,2)]
        print(squares)

    def flat_list_comp():
        flat     = [n for row in [[1,2],[3,4],[5,6]] for n in row]
        print(flat)

    def flat_list_normal():
         flat =[]
         sample_list = [[1,2],[3,4],[5,6]]
         for row in sample_list:
              for n in row:
                   flat.append(n)
         print (flat)
            
    def filter_email_comp():
         data = ["pavi@gmail.com","john@gmail.com" , "stack","list","queue"]
         emails = [s for s in data if "@" in s and "." in s]
         print(f"The entered mail id valid:{emails}")

    def gen():
         generator = (x**2 for x in range(2,50,2))
         peek = next(generator)
         print(peek)
         total = sum(generator)
         print(f"Sum {total}")

    def memory_comparison():
         generator = (x**2 for x in range(2,50,2))
         list_comp = [x**2 for x in range(2,50,2)]
         print("List Size",sys.getsizeof(generator))
         print("Gen Size",sys.getsizeof(list_comp))

    def apply_discount():
        prices = {
            "Laptop": 65000,
            "Mouse": 1200,
            "Keyboard": 2500,
            "Monitor": 18000
        }
        # discount = {k:round(v*0.8,2) for k,v in prices.items()}

        discount = {
        k: round(v - (v * 20 / 100), 2)
        for k, v in prices.items()
    }
        print(discount)
        


def main():
    print()
    print("---Even Numbers Normal for loop ---")
    Pipelines.normal_square()
    print()
    print("---Even Numbers List Comprehension ---")
    Pipelines.comp_square()
    print()
    print("---Flat 2d list comprehension---")
    Pipelines.flat_list_comp()
    print()
    print("---Flat 2d list normal--- ")
    Pipelines.flat_list_normal()
    print()
    print("---Filtered emails---")
    Pipelines.filter_email_comp()
    print()
    print("---Generator EXpression---")
    Pipelines.gen()
    print()
    print("---Memory Comparison---")
    Pipelines.memory_comparison()
    print()
    print("---Apply Discount---")
    Pipelines.apply_discount()









if __name__ == "__main__":
    main()

    


     



    

