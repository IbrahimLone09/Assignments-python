def iterative_function(n):
    fact = 1
    for i in range(1 , n + 1):
        fact *= i
    return fact
    
def recursive_function(n):
    if n == 1:
     return 1
    return n * recursive_function(n - 1)

def gp_term(a ,r ,n):
   return a * (r ** n)

def sum_of_squares(n):
   squares = 0
   for i in range(1 , n + 1):
      squares += i ** 2
   return squares


def sum_of_powers(x , n):
   sum = 0
   for i in range(1 , n + 1):
      sum += (x ** i) / i
   return sum

n = int(input("Enter n: "))
x = int(input("Enter x: "))
a = int(input("Enter a: "))
r = int(input("Enter r: "))


print("iterative function:" , iterative_function(n))
print("recursive function:" , recursive_function(n))
print("GP term:" , gp_term(a ,r ,n))
print("sum of squares:" , sum_of_squares(n))
print("sum of powers:" , sum_of_powers(x , n))

if iterative_function(n) == recursive_function(n):
   print("Both iterative and recursive results are equal:")

else:
   print("Results differ:")
