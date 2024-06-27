# Write a program to fill in a letter template given below with name and date.
# letter = ''' 
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

name = input("Enter your Name")
date = input("Enter the date")

letter = (f'''Dear {name},
You are selected!
{date}''')

print(letter)

# Now using replacement function

letter = ''' 
 Dear <|Name|>,
 You are selected!
 <|Date|>
 '''

print(letter.replace("<|Name|>", "Kunal").replace("<|Date|>", "26 octomber 2050"))
 