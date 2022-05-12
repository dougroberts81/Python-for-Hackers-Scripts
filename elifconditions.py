# we are using the elif statement to use multiple conditions

# prompt user for name
print('what is your name?')
name=input()

# prompt user for age
print('what is your age?')
age=input()

#check if user name is Doug
if name =='Doug':
   print('Hi Doug')

# check is age is under 40
elif int(age) < 40:
   print('you are obviously not Doug or are lying!')

#check if age is over 150
elif int(age) > 150:
   print('you must be zombie or alien')

#check is age is over 100
elif int(age) > 100:
   print('Are you future Doug?')
   

