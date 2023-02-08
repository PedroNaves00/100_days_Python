#Write your code below this line 👇
def prime_checker(number):
    primo = True
    for x in range(2, number-1):
        if number % x == 0:
            primo = False
    if primo == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

        


    





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
