

#Brighlee Reynoso
#Modules and Libraries
#10/13/2026

square_feet = int(input("Enter the square feet of wall space to be painted: "))
price_per_gallon = float(input("Enter the price of the paint per gallon: "))

gallons_required = square_feet / 112
hours_required = gallons_required * 8

def cost_of_labor(hours):
    labor_rate = 35.00
    return hours * labor_rate
def cost_of_paint(gallons, price_per_gallon):
    return gallons * price_per_gallon
def total_cost():
    return cost_of_labor(hours_required) + cost_of_paint(gallons_required, price_per_gallon)

print(f"Hours of labor required: {hours_required:.2f}")
print(f"Cost of paint: ${cost_of_paint(gallons_required, price_per_gallon):.2f}")
print(f"Labor charges: ${cost_of_labor(hours_required):.2f}")
print(f"Total cost of the paint job: ${total_cost():.2f}")

