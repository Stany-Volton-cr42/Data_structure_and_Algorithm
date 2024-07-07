"FINDING COMPLEXITY OF THE ALGORITHM"

""" 
1. O(1) ---> Constant
2. O(n) ---> Linear
3. O(n^2) ---> Quadratic
4. O(log n) ---> Logarithmic
5. O(n log n) ---> Log Linear
6. O(n!) ---> Factorial
"""

# for loop in pythons

# What is the complexity of this algorithm


i = 1                           # Statement excute 1 times

for i in range(11):                 # O(n) ->  O(1) ---> Constant (n)
                                # this Statement excute 10 times
    print(i,"hello world") 


# O(n) =  O(1)

# Because of the each time the loop run have the complexity of O(n)

"""Finding the time complexity of an algorithm means, finding that part 
    of algorithm which is consusming maximum time"""


# Two biggest time complexity
"1. Loop.       2. Recursition"



"""
When User give the input in the algorithm
"""

# What is the Complexity of this algorithm
n = int(input("Enter the number"))

for i in range(n):
                                    # the complexity is O(n) because it takes n times
    print(i,"hello world")          # and it's excute n times based on user input



# What is the Complexity of this algorithm?

n = int(input("Enter the number"))

for i in range(n):
    print(i,"hello world")         # the complexity is O(n) because it takes n times

for i in range(n):                          # n * n = n^2
    for j in range(n): 
        print(i,"hi")     # the complexity is O(n^2) because it is nested loops


"""So final complexity is O(n^2) because,

==>  Finding the time complexity of an algorithm means, finding that part 
    of algorithm which is consusming maximum time"""


n = int(input("Enter the number"))

for i in range(1,n + 1,2):
    print(i,"hello Chacha! How is your chachi")
    
# The complexity of the algorithm is O(n/2) because it's skiping the 2 at the time

"And remember that the 2 is constant so the algorithm complexity is O(n) Ultimately"