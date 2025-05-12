# how to check the given number is armstrong num :
# 1. take an input from user.
# 2. initialize sum = 0 .
# 3. find the sum of each digit .
# 4. using while loop .
# 5. take each digit as an modulus operator of a num 
# 6. then cube of each digit and sum of it.
# 7. then divide it by 10 .
# 8. then display it if num==sum .

# ************************************************************* #

num = int (input("Enter num : "))
order=len(str(num))

sum=0

temp=num
while temp>0:
    digit =temp % 10
    sum += digit**order
    temp//=10

if num==sum:
    print("It is an Armstrong number :",num)
else:
    print("It is Not an Armstrong number :",num)
