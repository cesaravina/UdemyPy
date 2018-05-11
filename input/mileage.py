# Ask user for km input, and convert it to miles

print("how many kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
print("Ok, you said {}  miles".format(round(miles, 3)))

# .format inserts the miles variable into the brackets {}, round() returns the rounded result to 3 digits