# Hello, I'm Rachell and this is my final integration project
# here's everything I've learnt so far

# time.sleep() reference: https://www.geeksforgeeks.org/python/sleep-in-python/

import time

def slope(x_1,y_1,x_2,y_2):
    a = y_2 - y_1
    b = x_2 - x_1
    c = a / b
    return c


def main ():
    name = input('Enter your name: ')
    print(f'Hello, {name}! Welcome to my integration project #3.')
    program_continuation = 'yes'
    while program_continuation == 'yes':
        print('What do you wish to review during this session?')
        print('1. ...')
        print('2. Calculations')
        print('3. ...')
        print('4. Exit program')
        user_choice = int(input())

        if user_choice == 1:
            print('You chose to review ...')
            #revisit

        elif user_choice == 2:
            print('You chose to review Calculations.')
            print('Which calculation do you wish to perform?')
            print('1. Slope')
            print('2. ')
            print('3. ...')
            print('4. ...')
            user_calculation_selection = int(input())
            # add more options...

            if user_calculation_selection == 1:
                retry_slope_calculation = 'yes'
                while retry_slope_calculation == 'yes':
                    print('You chose to calculate slope.')
                    x1 = float(input('Enter the value of the first x-coordinate: '))
                    x2 = float(input('Enter the value of the second x-coordinate: '))
                    y1 = float(input('Enter the value of the first y-coordinate: '))
                    y2 = float(input('Enter the value of the second y-coordinate: '))
                    slope_answer = slope(x1, x2, y1, y2)
                    print('The slope is ', slope_answer)

                    # following variable is for the user to choose if they want to make another slope calculation.
                    user_choice_slope = input('Would you like to calculate slope again? (yes/no): ')
                    if user_choice_slope == 'yes':
                        retry_slope_calculation = 'yes'
                    elif user_choice_slope == 'no':
                        retry_slope_calculation = 'no'

            # revisit this equation asap
            elif user_calculation_selection == 2:
                retry = 'yes'  # placeholder

        elif user_choice == 3:
            print('You chose to review....')
            #revisit

        elif user_choice == 4:
            print(f'Thank you for reviewing my project, {name}.')
            time.sleep(2)
            print('Exiting program...')
            time.sleep(2)
            program_continuation = 'no'

        else:
            print('Invalid choice. Please re-enter your choice.')

if __name__ == "__main__":
    main()
