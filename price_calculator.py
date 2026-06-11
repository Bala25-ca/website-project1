original_price = int(input("Enter the original price: "))
discount_rate = float(input("Enter the discount rate (in percentage): "))
def calculate_price(original_price, discount_rate):
    discount_amount = original_price * (discount_rate / 100)
    final_price = original_price - discount_amount
    return final_price
#calculated_price = calculate_price(100, 10)
calculated_price = calculate_price(original_price, discount_rate)
print(f"The final price after discount is: ${calculated_price:.2f}")

#GPS coordinates tracker with tuples
destination = ("34.0522","-118.2437")
latitude = destination[0]
longitude = destination[1]
print(f"Latitude: {latitude}, Longitude: {longitude}")

#GPS coordinates tracker with function
def destination(latitude, longitude):
    latitude = float(latitude)
    longitude = float(longitude)
    return f"Destination coordinates: Latitude {latitude}, Longitude {longitude}"
print(destination(latitude, longitude))
destination("34.0522","-118.2437")
