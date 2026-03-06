from fastapi import FastAPI

app = FastAPI()

# Product Database (just a Python list for now)

products = [
    {"id": 1, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 120, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": False},
    
#Add 3 More Products
    {"id": 5, "name": "Laptop Stand", "price": 899, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1299, "category": "Electronics", "in_stock": False}
]

#Home 
@app.get("/")
def home():
    return {"message": "Welcome to My E-commerce Store"}

#list products and their numbers
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

# Category Filter Endpoint
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    filtered_products = []

    for product in products:
        if product["category"].lower() == category_name.lower():
            filtered_products.append(product)

    if not filtered_products:
        return {"error": "No products found in this category"}

    return {"products": filtered_products}

# Shows Only In-Stock Products
@app.get("/products/instock")
def get_instock_products():

    instock_products = []

    for product in products:
        if product["in_stock"] == True:
            instock_products.append(product)

    return {
        "in_stock_products": instock_products,
        "count": len(instock_products)
    }

#Store summary endpoint
@app.get("/store/summary")
def store_summary():

    total_products = len(products)

    in_stock = 0
    out_of_stock = 0
    categories = set()

    for product in products:

        if product["in_stock"]:
            in_stock += 1
        else:
            out_of_stock += 1

        categories.add(product["category"])

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": list(categories)
    }

#Search by using keyword/specific name
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    matched_products = []

    for product in products:
        if keyword.lower() in product["name"].lower():
            matched_products.append(product)

    if not matched_products:
        return {"message": "No products matched your search"}

    return {
        "matched_products": matched_products,
        "count": len(matched_products)
    }

#Cheapest & Most Expensive Product
@app.get("/products/deals")
def product_deals():

    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }
