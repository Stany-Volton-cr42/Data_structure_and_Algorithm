# Tell me the complexity of the algorithm

# n = int(input("Enter the number"))

# i = 1
# while i <= n:
#     print("hi")
#     i= i * 2

# """The complexity of the algorithm is O(log n).
#     you can make as the thumb rule that if there is the
#     multiplication and devision then the complexity is log n"""

# for i in range(1,n+1):    #"<<=== So this is the first loop and the complexity is O(n)"
#     j = 1
#     while j <= n:           #"<<=== And the second loop starts here with multiplication which means0 log(n)"
#         print("hello")
#         j = j * 2               #So the whole complexity is O(n_log_n)


# one more loop
n = int(input("Number"))

i = 2
while i <= n:
    print("hello")
    i = i**2

"""The complexity of the above algorithm is O(log.log(n)).
    Trick:- whenever you see the squire or the power 
    and the underRoot the complexity would be O(log.log(n))
    
    SEE EXPLAINTION IN COMPATIBILITY.MD"""


while i>= n:
    print("hello")
    i = i // i**2   # the complexity would be O(log.log(n))