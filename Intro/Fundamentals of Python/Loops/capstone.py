# Lists of hairstyles, their prices, and last week's sales
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew cut", 
              "bowl cut", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1. Calculate total price
total_price = 0

for price in prices:
    total_price += price

# 2. Calculate average price
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

# 3. Create new_prices list with each price - 5
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

# 4. Calculate total revenue
total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue:", total_revenue)

# 5. Calculate average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

# 6. Create list of cuts under $30 using new prices
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Haircuts Under $30:", cuts_under_30)
