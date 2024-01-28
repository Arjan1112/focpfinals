def get_valid_input(prompt, valid_options):
    """Asks the user for input until a valid option is provided."""
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_options:
            return user_input == 'Y'
        print("Please answer 'Y' or 'N'.")

while True:
    try:
        num_pizzas = int(input("How many pizzas ordered? "))
        if num_pizzas <= 0:
            raise ValueError("Please enter a positive number of pizzas.")
        break
    except ValueError:
        print("Please enter a valid positive integer!")

delivery_required = get_valid_input("Is delivery required? (Y/N) ", ('Y', 'N'))
is_tuesday = get_valid_input("Is it Tuesday? (Y/N) ", ('Y', 'N'))
used_app = get_valid_input("Did the customer use the app? (Y/N) ", ('Y', 'N'))

# Constants for pricing and discounts
PIZZA_PRICE = 12.00
DISCOUNT_TUESDAY = 0.5
DISCOUNT_APP = 0.25
DELIVERY_FEE = 2.50
MIN_DELIVERY_ORDER = 5

# Calculate total price with discounts and delivery fee
total_price = num_pizzas * PIZZA_PRICE

if delivery_required and num_pizzas < MIN_DELIVERY_ORDER:
    total_price += DELIVERY_FEE

if is_tuesday:
    total_price *= (1 - DISCOUNT_TUESDAY)

if used_app:
    total_price *= (1 - DISCOUNT_APP)

# Display summary of order and total price
print("\nBPP Pizza Price Calculator")
print("==========================\n")
print(f"How many pizzas ordered? {num_pizzas}")
print(f"Is delivery required? {delivery_required}")
print(f"Is it Tuesday? {is_tuesday}")
print(f"Did the customer use the app? {used_app}\n")
print(f"Total Price: £{total_price:.2f}.")