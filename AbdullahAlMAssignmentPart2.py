# Simple Shopping Cart

customer = input("Please enter customer's name: ")

print("Please enter three products:")
p1 = input("Product 1 name: ")
c1 = float(input("Product 1 price: "))
p2 = input("Product 2 name: ")
c2 = float(input("Product 2 price: "))
p3 = input("Product 3 name: ")
c3 = float(input("Product 3 price: "))

subtotal = c1 + c2 + c3

if subtotal >= 5000:
    discount = 20
elif subtotal >= 3000:
    discount = 10
elif subtotal >= 1000:
    discount = 5
else:
    discount = 0

discount_amount = subtotal * discount / 100
final_total = subtotal - discount_amount

print(f"\nCustomer: {customer}")
print(f"Products: {p1}, {p2}, {p3}")
print(f"Subtotal: ${subtotal:.2f}")

print(f"Discount: {discount}%")
print(f"Final Total: ${final_total:.2f}")