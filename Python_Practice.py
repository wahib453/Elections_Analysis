#counties = ['Arapahoe', 'Denver', 'Jefferson']
#if 'Denver' in counties and 'El Paso' not in counties:
#    print("Only Denver is in the list of counties.")
#else: 
#    print("Denver is in the list of counties and El Paso is not in the list of counties.")
#if 'Arapahoe' in counties:
#    print("Arapahoe is in the list od counties")
#else:
#    print("Arapahoe is not in the list of counties")
#if counties[1] == 'Denver':
#   print(counties[1])
#if counties[3] != 'Jefferson':
#    print(counties[2])
#Temperature = int(input("What is the temperature outside? "))
#if Temperature > 80:
#    print("Turn on the AC.")
#else:
#    print("Open the windows.")
#Grade = int(input("What is your grade? "))
#if Grade >= 90:
#    print("Your grade is an A.")
#elif Grade >= 80:
#    print("Your grade is a B.")
#elif Grade >= 70:
#    print("Your grade is a C.")
#elif Grade >= 60:
#    print("Your grade is a D.")
#else:
 #   print("Your grade is an F. ")
#x = 0
#while x <= 5:
#    print(x)
#    x = x + 1
#count = 7
#while count < 7:
#    print("Hello World!")

#counties = ['Arapahoe', 'Denver', 'Jefferson','El Paso', 'Tarrant', 'Dallas']
#for county in counties:
#    print(county)
#numbers = [0, 1, 2, 3, 4]
#for numbe in numbers:
#    print(numbe)
#for num in range(5):
#    print(num)

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict.values():
#    print(county)

#Original Code
#my_votes = int(input("HOw many votes did you get in the election? "))
#toal_votes = int(input('What is the total votes in the election?'))
#percentage_votes = (my_votes / toal_votes) * 100
#print("I received " + str(percentage_votes) + "% of the total votes.")

#Edited version 
#my_votes = int(input("HOw many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election?"))
#percentage_votes = (my_votes / total_votes) * 100
#print(f"I received {percentage_votes}% of the total votes.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, registered_voters in counties_dict.items():
    #print(county + " county has " + str(registered_voters) + " registered_voters.")
    print(f"{county} county has {registered_voters} registered voters.")

