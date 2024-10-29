# Define known values
bill_amount = 75  # Example bill amount
tip_percentage = 20  # Example tip percentage

# Calculate tip amount
tip_amount = bill_amount * (tip_percentage / 100)

# Display the results with formatting
print("The tip on a ${:.2f} restaurant bill is ${:.2f}".format(bill_amount, tip_amount))