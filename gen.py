def P_generator(): #using generator function
    prime = [] #empty list
    n = 2
    while True: #prime no code
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(n)
            yield n  
        n += 1

g = P_generator()
for _ in range(10):
    print(next(g))

''' 
Generator are function that return an iterator using the yeild function but whenever it generates a value
it uses yeild instead of return. here we are creating a function called P_generator , creating a empty list to 
keep the prime number .
Where n =2 while loop is used its true when is_prime is true from the range 2 to n if n is divisible by it will return zero which means it checks if
it has factors , so if it is divisible by i then it will return is_prime as false and break the loop
and if is_prime is true then it will append it in the empty list created.
'''

    