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

# practice with membership and logical operators
if 'Arapahoes' in counties and 'El Paso' in counties:
    print('Arapahoes and El Paso are in the list of counties.')
else:
    print('Arapahoes or El Paso is not in the list of counties.')

# practice with logical operator: or 
counties = ['Arapahoes', 'Denver', 'Jefferson']
if 'Arapahoes' in counties or 'El Paso' in counties:
    print('Arapahoes or El Paso are in the list of counties.')
else:
    print('Arapahoes and El Paso are not in the list of counties.')

# practice using WHILE loop
x = 0
while x <= 5:
    print(x)
    x = x + 1

# practice using FOR loop
for county in counties:
    print(county)

# practice using the built-in function, range(), with FOR loop
numbers = [0,1,2,3,4,5]
for num in numbers:
    print(num)

# First alternatively
for num in range(5):
    print(num)

# Second alternative
for i in range(len(counties)):
    print(counties[i])

# practice using for loop to iterate through a dictionary.
counties_dic = {'Arapahoes': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county in counties_dic:
    print(county)

# Alternatively
counties_dic = {'Arapahoes': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county in counties_dic.keys():
    print(county)

# get the values
counties_dic = {'Arapahoes': 422829, 'Denver': 463353, 'Jefferson': 432438}
for value in counties_dic.values():
    print(value)

# Alternatively
counties_dic = {'Arapahoes': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county in counties_dic:
    print(counties_dic[county])

# Skill drill
counties_dic = {'Arapahoes': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county, voters in counties_dic.items():
    print(county + ' County has ' + str(voters) + ' registered voters. ')

# Alternatively using the f-string formatted print statement
counties_dic = {'Arapahoes': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county, voters in counties_dic.items():
    print(f'{county} County has {voters} registered voters. ')

# Get Each Dictionary in a List of Dictionaries
voting_data = [{'county':'Arapahoes', 'registered_voters': 422829}, 
                {'county':'Denver', 'registered_voters':463353}, 
                {'county':'Jefferson', 'registered_voters':432438}]

for county_dict in voting_data:
    print(counties_dic)

# Multiline F-Strings practice
candidate_votes = int(input('how many votes did the candidate get in hte election? '))
total_votes = int(input('what is the total number of votes in the election? '))
message_to_candidate = (
    f'You received {candidate_votes} number of votes.'
    f'The total number of votes in the election was {total_votes}.'
    f'You received {candidate_votes / total_votes * 100} % of the total votes.'
)
print(message_to_candidate)