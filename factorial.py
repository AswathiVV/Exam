# e=int(input("Enter a no :"))
# fact=0
# while e:
#     fact*=e
# print(fact)    


# i=1
# e=int(input("Enter Value :"))
# Factorial=1
# while i<=e:
#     Factorial*=i
#     i+=1
# print(Factorial)
'''
Enter Value :5
120
'''
def fact():
    a=int(input("Enter Value :"))
    Factorial=1
    for i in range(1,a+1):
         Factorial*=i
         print(Factorial)
fact()