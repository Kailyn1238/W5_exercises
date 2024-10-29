 # Define known values
interest_rate = 6.0  # Example interest rate

# Calculate years to double using the Rule of 72
years_to_double = 72 / interest_rate

# Calculate the doubled balance
initial_balance = 1000  # Example initial balance
doubled_balance = initial_balance * 2

# Display the results with formatting
print("At a {:.0f}% interest rate, your savings account will be worth ${:.2f} in {:.1f} years".format(interest_rate, doubled_balance, years_to_double))