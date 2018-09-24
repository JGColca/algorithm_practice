def ask_user_for_number():
    while True:
        try:
            input_number = int(input("Enter a number between 1 and 100 to get descriptive number: "))
            if input_number > 100 or input_number < 1:
                print("******** Please enter a number between 1 and 100 ********")
                input_number = int(input("Enter a number between 1 and 100 to get descriptive number: "))
        except ValueError:
            print("********  Please enter a number between 1 and 100. ********")
            input_number = int(input("Enter a number between 1 and 100 to get descriptive number: "))
        return input_number

number = str(ask_user_for_number())

def add_placeholders(number):
    if len(number) == 1:
        number = f'00{number}'
    elif len(number) == 2:
        number = f'0{number}'
    return number

number = add_placeholders(number)

def ones(number):
    digit_ones = ""
    if number[2] == "1":
        digit_ones = ("one")
    elif number[2] == "2":
        digit_ones = ("two")
    elif number[2] == "3":
        digit_ones = ("three")
    elif number[2] == "4":
        digit_ones = ("four")
    elif number[2] == "5":
        digit_ones = ("five")
    elif number[2] == "6":
        digit_ones = ("six")
    elif number[2] == "7":
        digit_ones = ("seven")
    elif number[2] == "8":
        digit_ones = ("eight")
    elif number[2] == "9":
        digit_ones = ("nine")
    return digit_ones


def tens(number):
    digit_tens = ""
    if number[1] == "2":
        digit_tens = ("twenty-")
    elif number[1] == "3":
        digit_tens = ("thirty-")
    elif number[1] == "4":
        digit_tens = ("fourty-")
    elif number[1] == "5":
        digit_tens = ("fifty-")
    elif number[1] == "6":
        digit_tens = ("sixty-")
    elif number[1] == "7":
        digit_tens = ("seventy-")
    elif number[1] == "8":
        digit_tens = ("eighty-")
    elif number[1] == "9":
        digit_tens = ("ninety-")
    return digit_tens

def teens(number):
    digit_teens = ""
    if number[2] == "1":
        digit_teens = ("eleven")
    elif number[2] == "2":
        digit_teens = ("twelve")
    elif number[2] == "3":
        digit_teens = ("thriteen")
    elif number[2] == "4":
        digit_teens = ("fourteen")
    elif number[2] == "5":
        digit_teens = ("fifteen")
    elif number[2] == "6":
        digit_teens = ("sixteen")
    elif number[2] == "7":
        digit_teens = ("seventeen")
    elif number[2] == "8":
        digit_teens = ("eighteen")
    elif number[2] == "9":
        digit_teens = ("nineteen")
    return digit_teens
    
def hundreds(number):
    digit_hundreds = ""
    if number[0] == "1":
        digit_hundreds = ("one-hundred")
    return digit_hundreds





def descriptive_number(number):
    if number[0] == "0" and number[1] == "0":
        des_number = f'{ones(number)}'
    if number[0] == "0" and ("0" and "1" not in number[1]):
        des_number = f'{tens(number)}{ones(number)}'
    if number[1] == "1":
        des_number = f'{teens(number)}'
    else:
        des_number = f'{hundreds(number)}{tens(number)}{ones(number)}'
    return des_number

print(descriptive_number(number))

while True:
  try:
      choice = input('Do you wish to convert another number to text?  Press Y to continue or any other character to quit: ')

      if (choice != "Y" and choice != "y"):
        break
      else: 
        number = str(ask_user_for_number())
        number = add_placeholders(number)
        print(descriptive_number(number))
  except ValueError:    
    print("Try again")

print("Thank you for using number to text converter.")

