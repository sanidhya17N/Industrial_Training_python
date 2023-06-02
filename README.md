# Industrial_Training_python
Q1 : For a list L = [10, 20, 30, 40,-1,50,-2,-5] do below task:
       A] : Multiply every elements in list by 2 and save these elements in other list
            L1 using list Comprehension, and print L1
        B]: Multiply every elements in list by 2 and save only elements which are positive in other list L2
           using list Comprehension , and print L2

 Q2 : Write a Lambda function to find multiplication of two number.

 Q3 : A] Write a function FINDMAX(a,b) to  find maximum of given number a and b
      B] Using map function and FINDMAX(a,b) function using find  maximum value in list L = [10, 20, 30, 40,-1,50,-2,-5]

 Q4 : A] Write a function IsPositive(a) which will  take one parameter and return True if number is greater than zero
       Else return False
      B] Using filer function and  IsPositive function find only positive number is list L = [10, 20, 30, 40,-1,50,-2,-5]

Q5  : A] Write a function MUL(a,b) to multiply two given numbers
      B] Using reduce function and MUL(a,b) function find multiplication of all elements of the list

#Level - 2

1.Calculate the factorial of a number by creating a function ‘calFactorial’.


2.Write a function Greet , which should take one argument as language , 
In function body check if language is ‘Hindi’ print ‘Namaskar’  ,else if  language is ‘English’ print ‘Hello’,else print Error message as wrong language.


3.Write a function Calculator, which should take two input from user in1 and in2 and should return addition, subtraction, division and division of two number using only one return statement. Please note: Make In2 as default argument and keep its value as 0.


 
4.The programmer was expecting the following program to print 200. What does it print instead? Why does it print what it does? Change code to change print 200
def proc(x):
    x = 2*x*x
    return x

def main():
    num = 10
    proc(num)
    print num

main()

5.Create a function AddList , which should take two argument as two Lists L1 and L2; add the corresponding elements of the list and save result in L3 and return the list L3. 
Assume, L1 = [1,2,3,4] ,  L2 = [10,20,30,40]
Hint: Use append function to extend new list.

6.Write a function named print_big_enough that accepts two parameters, a list of numbers L and a number x . The function should print, all the elements in the list that are at least as large as the second parameter.
