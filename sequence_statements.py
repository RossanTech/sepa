# Numbers that are divisible by both 7 and 3
finalnumber = 100

a = []

for num in range(1,finalnumber):
  if num % 3== 0 and num % 7 == 0:
    a.append(num)

print("Numbers that are divisible by both 7 and 3 in the range of 1 to 100 are: " + str(a))

# Numbers that are divisible by 7 but not 3
b = []

for num in range(1,finalnumber):
  if num % 3 and num % 7 == 0:
    b.append(num)

print("Numbers that are divisible by 7 but not 3 in the range of 1 to 100 are: " + str(b))


# ODD numbers divisible by 7 but not 3
c = []

for num in range(1,finalnumber):
  if num % 2 == 1:
    if num % 7 == 0 and num % 3:
      c.append(num)
      
print('ODD numbers that are divisible by 7 but not 3 in the range of 1 to 100 are: ' + str(c))
      
# Numbers that are divisible by the sum of its digits
d = []


for num in range(1, finalnumber):
    sum_of_num = 0

    string_number = str(num)
    for i in string_number:
        sum_of_num += int(i)

    if num % sum_of_num == 0:
        d.append(num)

print('The numbers that are divisible by the sum of its digits are: ' + str(d))


# Numbers that are equal to the square of the sum of its digits
e = []

if num == (sum_of_num * sum_of_num):
  e.append(num)
  
print('The numbers that are equal to the square of the sum of its digits in the range of 1 to 100 are: ' + str(e))