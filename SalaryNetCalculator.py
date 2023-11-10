# Prompt the user to enter the salary as an integer
salary = int(input('Enter the salary: '))

# Prompt the user to enter the tax rate as a decimal (e.g., 27.5)
tax = float(input('Enter the Tax in % (e.g., 27.5): '))

# Calculate the net salary by subtracting the tax from the gross salary
net_salary = salary - (salary * (tax * 0.01))

# Display the calculated net salary on the screen
print("The net salary is: {0}".format(net_salary))