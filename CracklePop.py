'''
Author: Natalie Ho
Date: February 20, 2025
Purpose: CracklePop
'''

'''
Write a program that prints out the numbers 1 to 100 (inclusive). 

If the number is divisible by 3, print Crackle instead of the number. 

If it's divisible by 5, print Pop.

If it's divisible by both 3 and 5, print CracklePop.
'''
def CracklePop():

  for i in range(1, 101): 
    # if divisible by 15, print CracklePop
    # Ex: given 15, I don't want the program to print "Crackle", so I put this condition first
    if i % 15 == 0:
      print("CracklePop")
    # if divisible by 3, print Crackle 
    elif i % 3 == 0:
      print("Crackle")
    # if divisible by 5, print Pop 
    elif i % 5 == 0:
      print("Pop")
    # for all other numbers, just print 
    else:
      print(i)

CracklePop()
