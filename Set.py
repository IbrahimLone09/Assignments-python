primes = {2,3,5,7,11,13}   # Defining the set as prime numbers

for i in primes:
    print(i)              #printing all elements of set one by one


odds = {1,3,5,7,9,11,13,15}  # Another set as odd numbers

primeodds = primes.intersection(odds)   #taking intersection between set prime and set odd with intersection function
print(primeodds)

all = primes.union(odds)    #taking union between set prime and set odd with union function
print(all)