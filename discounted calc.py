#prompt the user to enter the price of the selected item.
price = int(input("Enter price: "))
discount = float(input("Enter discount: "))

# Ensure the discount is not more than 20%
if discount <=0.2*price:
    # Calculate the discounted price
    discounted_price = price - discount
    print(f"Discounted Price: {discounted_price:.2f}")
else:
    # No additional discount applied
    print("original price",price)
