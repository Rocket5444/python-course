# A spam comment is defined as a text containg following keywords.
# 'make a lot of money', 'buy now', 'subscribe this', 'click this'.
# Write a program to detect these spams
p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "click this"

message = input("Enter your comment")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam comment")

else:
    print("Comment is not a spam")