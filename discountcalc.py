import sys

def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount.

    Args:
        price (float): The original price of an item.
        discount_percent (float): The discount percentage as a float between 0 and 100.

    Returns:
        float: The final price after applying the discount.
    """
    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price

# Prompt the user for input
price_input = input("Enter the original price of an item: ")
price = float(price_input)

discount_input = input("Enter the discount percentage: ")
discount_percent = float(discount_input)

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"The final price is {final_price:.2f}")