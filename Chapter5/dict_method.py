# Items method
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Kunal"
}

# d = {} #Empty dictionary.

print(marks.items())

# .keys method
print(marks.keys())

# .values method
print(marks.values())

# .update method
marks.update({"Harry": 99, "Renuka": 100})

# .get method
print(marks.get("Harry")) # Prints none
print(marks["harry"]) # prints keyerror

# .copy method
print(marks.copy("Harry"))