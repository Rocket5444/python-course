# Can you change the value inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1,2]}

# NO we cannot update it in fact you cannot even have a list as an element in a set 
# because sets in python require all their elements to be immutable and hashable.