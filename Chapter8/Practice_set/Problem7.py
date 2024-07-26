'''
Write a python function to remove a given word from a list ad strip it at the same time.
'''
l = ["harry", "Rohan", "Shubham", "an"]

def rem(l, word):
    for item in l:
        l.remove(word)
        return l
    
print(rem(l, "an"))
