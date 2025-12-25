# LC 258
# Problem Link: https://leetcode.com/problems/add-digits

num = int(input("Enter any integer: "))

# if len(str(num)) == 1:
#     print(num)
    
def add_digits(num):
    num_str = str(num)
    digit_sum = sum(int(digit) for digit in num_str)

    if len(str(digit_sum)) == 1:
        return digit_sum
    else:
        return add_digits(digit_sum)

print(add_digits(num))
