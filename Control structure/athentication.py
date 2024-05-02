'This program will identify gender and validation '
gender = input('Pls enter your gender ')
age = int(input('PLs enter your age '))
if gender == 'male' and age >= 18:
    print(' you are a man ')
elif gender== 'female' and age >= 18:
    print('you are a female')
else:
    print('You are a minor')