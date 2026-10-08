# PYTHON CONDITIONAL STATEMENTS AND LOOPS

age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

score = 75
if score >= 80:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")

category = "vegetables"
price = 5000
if category == "vegetables":
    if price > 10000:
        print("Expensive vegetable")
    else:
        print("Affordable vegetable")

products = ["Tomatoes", "Matooke", "Fish"]
for product in products:
    print(product)

stock = 50
while stock > 0:
    print(f"Stock remaining: {stock}")
    stock -= 10

print("Done")
