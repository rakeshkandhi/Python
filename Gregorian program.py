#ALGORITHM :-
##If a year is evenly divisible by 4 means having no remainder then go to next step
##If a year is divisible by 4, but not by 100. For example
##If a year is divisible by 100, but not by 400
def CheckLeap(Year): 
  if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):   
    print("Given Year is a leap Year")
  else:  
    print ("Given Year is not a leap Year")
if __name__=="__main__":
    Year = int(input("Enter the number: "))
    CheckLeap(Year)  
