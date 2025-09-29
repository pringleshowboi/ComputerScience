# Get package weight from user
weight = float(input("Enter the weight of your package (in pounds): "))

# Ground Shipping
ground_flat = 20.00

if weight <= 2:
    ground_cost = weight * 1.50 + ground_flat
elif weight <= 6:
    ground_cost = weight * 3.00 + ground_flat
elif weight <= 10:
    ground_cost = weight * 4.00 + ground_flat
else:
    ground_cost = weight * 4.75 + ground_flat

print(f"Ground Shipping: ${ground_cost:.2f}")

# Ground Shipping Premium (flat rate)
premium_ground_cost = 125.00
print(f"Ground Shipping Premium: ${premium_ground_cost:.2f}")

# Drone Shipping
# No flat rate
if weight <= 2:
    drone_cost = weight * 4.50
elif weight <= 6:
    drone_cost = weight * 9.00
elif weight <= 10:
    drone_cost = weight * 12.00
else:
    drone_cost = weight * 14.25

print(f"Drone Shipping: ${drone_cost:.2f}")

# Determine the cheapest method
if ground_cost < premium_ground_cost and ground_cost < drone_cost:
    cheapest_method = "Ground Shipping"
    cheapest_cost = ground_cost
elif premium_ground_cost < drone_cost:
    cheapest_method = "Ground Shipping Premium"
    cheapest_cost = premium_ground_cost
else:
    cheapest_method = "Drone Shipping"
    cheapest_cost = drone_cost

print(f"\nThe cheapest option is {cheapest_method} at ${cheapest_cost:.2f}")
