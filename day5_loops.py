#Udemy --Loops
#1 adding of numbers from 1 to 100
print('a'+'b')
sum = 0
for i in range(0,101):
    sum +=i
print(sum)

#2 FizzBuzz

for i in range (1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)


