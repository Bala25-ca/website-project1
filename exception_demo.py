def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Both arguments must be numbers!"
    else:
        return result
    finally:
        print("Division attempt completed.")
# Test the function with different inputs
print(safe_divide(10, 2))  # Should return 5.0
print(safe_divide(10, 0))  # Should return "Cannot divide by zero!"
print(safe_divide("10", 2))  # Should return "Both arguments must be numbers!"  
