'''
Write a recursive function to calculate the sum of first n natural numbers.
'''
# def sum_of_natural_numbers(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_of_natural_numbers(n - 1)

# # Example usage:
# n = int(input("Enter number: "))
# result = sum_of_natural_numbers(n)
# print(f"The sum of the first {n} natural numbers is {result}.")

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4... n
'''

def sum(n):
    # n = int(input("Enter number: "))
    if(n==1):
        return 1
    return sum(n-1) + n
    
print(sum(5))