# Data Pipeline with Lambdas 
# Real-world app: E-commerce — Amazon / Flipkart  
# Problem 
# You are given a list of product dictionaries from an e-commerce platform. 
# Use lambda functions with map(), filter(), and sorted() to build a data processing pipeline. No for loops allowed for the transformations.
# Apply discounts, filter by rating, sort by price, and format output.  

products = [ 

  {"name": "iPhone 15",      "price": 79999,  "category": "Electronics", "rating": 4.5}, 

  {"name": "Nike Shoes",     "price": 8999,   "category": "Fashion",     "rating": 4.2}, 

  {"name": "MacBook Pro",    "price": 149999, "category": "Electronics", "rating": 4.8}, 

  {"name": "Levi Jeans",     "price": 3499,   "category": "Fashion",     "rating": 3.9}, 

  {"name": "Sony Headphones","price": 12999,  "category": "Electronics", "rating": 4.6}, 

  {"name": "Kurta Set",      "price": 1299,   "category": "Fashion",     "rating": 4.1}, 

] 

# Step 1: Apply 10% discount
discounted = map(
    lambda p: {
        **p,
        "discounted_price": round(p["price"] * 0.90, 2)
    },
    products
)

# Filter products with rating >= 4.2
filtered = filter(
    lambda p: p["rating"] >= 4.2,
    discounted
)

# Sort by discounted price
sorted_products = sorted(
    filtered,
    key=lambda p: p["discounted_price"]
)

formatted = map(
    lambda p: (
        f'{p["name"]} | '
        f'{p["category"]} | '
        f'Rating: {p["rating"]} | '
        f'₹{p["discounted_price"]:.2f}'
    ),
    sorted_products
)

print(*formatted, sep="\n")