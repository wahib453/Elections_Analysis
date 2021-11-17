from typing_extensions import IntVar


print("Hello world")
Add = 5 + 2 * 3
print(Add)

# Determine if the second counties in the list is Denver. If it's, print to the screen.
counties = ['Arapahoes', 'Denver', 'Jefferson']
if counties[1] == 'Denver':
    print(counties[1])

# Determine the temperature outside
temperature = int(input('what is the temperature outside'))


if temperature > 80: # the temperature is in degree Fahrenheit.
    print('Turn on the AC.')

else:
    print('Open the window.')

# Determine your grade using if-else statement
score = int(input('What is your grade?'))
if score >= 90:
    print('your grade is an A.')

else:
    if score >= 80:
        print("Your grade is a B.")
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is F.') 

# Rewrite the above statement using if-elif-else
score = int(input('What is your grade?'))
if score >= 90:
    print('your grade is an A.')

elif score >= 80:
    print("Your grade is a B.")

elif score >= 70:
    print('Your grade is a C.')
        
elif score >= 60:
    print('Your grade is a D.')
            
else:
    print('Your grade is F.')

# Determine if El Paso is in the counties list.
counties = ['Arapahoes', 'Denver', 'Jefferson']
if 'El Paso' in counties:
    print('El Paso is in the list of counties.')
else:
    print('El Paso is not in the list of counties.')
    
# Practice on logical operators: 'and', 'or', 'not'
# practice on logical operator: and
x = 5 
y = 5    

if x == 5 and y == 5:
    print('turn')
else:
    print('false')

# practice on logical operator: or
if x == 3 or y == 5:
    print('true')    
else:
    print('false')

# practice on logical operator: not
if not (x > y):
    print('true')
else:
    print('false')
