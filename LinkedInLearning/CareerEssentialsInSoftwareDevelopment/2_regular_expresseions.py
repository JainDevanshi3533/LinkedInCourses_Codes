import re  # importing module for regular expression

five_digit_zipcode = '98989'
nine_digit_zipcode = '98922-0003'
phone_number1 = '883-999-3939'
phone_number2 = '999-33-32313'

#creating a regular expression (regex) to find if the string contains five continous numbers
five_digit_expression = r'\d{5}'      # r means to include any backslash if there is any

#re.search function to search the regular expression in the given string
print(re.search(five_digit_expression, five_digit_zipcode))
print(re.search(five_digit_expression, nine_digit_zipcode))
print(re.search(five_digit_expression, phone_number1))
print(re.search(five_digit_expression, phone_number2))



############## miles to kilometers #############

miles = float(input('Enter a distance in mile: '))

#kilometer = 1.6 * milesValue

kilometers= 1.6 * miles
print(kilometers)
