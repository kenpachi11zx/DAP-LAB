string = input("Enter a string: ")
upper_count = sum(1 for c in string if c.isupper())
lower_count = sum(1 for c in string if c.islower())

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
