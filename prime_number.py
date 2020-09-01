n = int(input("enter a number to check if it is a pime or not : "))

count = 0

for i in range(1, n+1) :
  if not(n % i) : count +=1

if (n == 0) or (n ==1) or (count >=3) : print(n, "is not a prime number.")
else : print(n, "is a prime number")


n = int(input("Enter the limit number: "))

prime = []

for num in range(2, n+1) :
  status = True
  for i in range (2, num) :
    if num % i == 0:
      status = False
  if status:
    prime.append(num)

print(prime)