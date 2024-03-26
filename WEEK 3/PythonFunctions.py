def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Args:
        price (float): The original price.
        discount_percent (float): The discount percentage.

    Returns:
        float: The discounted price if discount is 20% or higher, else the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate and print final price
final_price = calculate_discount(original_price, discount_percentage)
print(f"Final price after applying the discount: ${final_price:.2f}")
