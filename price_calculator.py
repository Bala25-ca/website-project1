def calculate_price(original_price, discount_rate):
    discount_amount = original_price * (discount_rate / 100)
    final_price = original_price - discount_amount
    return final_price
calculated_price = calculate_price(100, 10)
print(f"The final price after discount is: ${calculated_price:.2f}")
