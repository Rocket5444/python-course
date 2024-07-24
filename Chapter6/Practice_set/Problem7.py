# Write a program to find out whether a given post is talking about "Harry" or not.

post = input("Enter your post: ")

if("Harry".lower() in post.lower()):  
    print("Yes, this post is talking about Harry")

else:
    print("No, this post is not talking about Harry")