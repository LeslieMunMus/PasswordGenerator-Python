import random

"""
THESE ARE THE MOST COMMON RANDOM METHODS USED IN MOST PROJECTS ALBEIT THERE ARE MORE:

random.random() - The results are in a form of float. It returns a random float number in the range [0.0, 1.0]
                eg. print(random.random()) --> this gets you different random floats

random.randint() - It requires 2 pars; start range (a) and stop range (b). Both a and b are included in the range
                   It works well when creating an OTP or short code.
                eg. print(random.randint(1, 99)) --> this picks a random integer between 0 and 100

random.choice() - Useful when working with automation or even general function 
                eg. names = ['Leslie', 'Prudy', 'Hailey', 'Munya', 'Mmawaja', 'Thea']
                    print(random.choice(names)) --> This will randomly pick a name from the list

"""

"""
__________________________________________PASSWORD GENERATOR_________________________________________________

The password should follow the following criteria:
1. At least 8 characters long
2. At least 1 upper character
3. At least 1 lower character
4. At least 1 numeric digit
5. At least 1 special symbol

"""

# First we need lists of these characters that we are going to use
# For the purpose of the example, we will only use 10 letters and a few special characters

upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

passwd = random.choice(upper_char) + random.choice(lower_char) + random.choice(num) + random.choice(special_char) + \
         random.choice(upper_char) + random.choice(lower_char) + random.choice(num) + random.choice(special_char)
print(passwd)
