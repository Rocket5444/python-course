friends = [ "Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)

# Append Method
# Append is the function which inserts the new value in the list at the last

friends.append("Kuanl")

print(friends)

# Sort Methods
# Sort is the function which sorts the list in the ascending order

l1 = [1, 34, 62, 2, 6, 11]
l1.sort()
print(l1)

# Reverse Method
# Reverse is the function which reverses the list
l1.reverse()
print(l1)

# Insert Method
# Insert is the function which inserts the new value in the list at the specified index
l1.insert(2, 100) # Insert 100 such that its index in the list is 2
print(l1)

# Pop Method
# Pop is the function which removes the last element from the list
value = l1.pop(3)
print(value)
print(l1)

# Remove Method
# Remove is the function which removes the specified value from the list
l1.remove(100)
print(l1)