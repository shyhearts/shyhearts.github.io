# Hello, I'm Rachell and this is my integration project #2
# here's everything I've learnt so far

def rectangle_area(l,w):
    area = l * w
    return area

def rectangle_volume(l,w, h):
    volume = l * w * h
    return volume

def average(sum_of_numbers, amount_of_numbers):
    average_calculation = sum_of_numbers / amount_of_numbers
    return average_calculation

def main():
    print('Hello, welcome to my integration project #2')
    program_continuation = True
    while program_continuation == True:
        print('What would you like to do from the given selection?')
        print ('1. quiz minigame')
        print('2. calculations')
        print ('3. Exit program')
        user_input = int(input())

        if user_input == 1:
            option_1_continuation = True
            while option_1_continuation == True:
                print('You selected to do a quiz minigame.')
                print('Welcome to the quiz minigame. \nYou will be asked three questions.')
                print('By the end of the quiz, you may select if you wish to continue the program.')
                user_quiz_choice = input('Do you wish to proceed? ')
                if user_quiz_choice == 'yes' or user_quiz_choice == 'Yes':
                    print('Quiz Topic: Logic Gates')
                    print('1. Which logic gate inverts the input?')
                    user_quiz_answer1 = input()
                    if user_quiz_answer1 == 'NOT gate':
                        print('Correct!')
                    else:
                        print('Incorrect. The correct answer is NOT gate.')
                    print('2. Which logic gate outputs 0 when both input are 1?')
                    user_quiz_answer2 = input()
                    if user_quiz_answer2 == 'NAND gate':
                        print('Correct!')
                    else:
                        print('Incorrect. The correct answer is NAND gate.')
                    print('3. Which logic gate outputs 1 when the input includes at least one 1?')
                    user_quiz_answer3 = input()
                    if user_quiz_answer3 == 'OR gate':
                        print('Correct!')
                    else:
                        print('Incorrect. The correct answer is OR gate.')
                    print('Would you wish to try again?')
                    user_answer = input()
                    if user_answer == 'yes':
                        option_1_continuation = True
                    else:
                        option_1_continuation = False

                elif user_quiz_choice == 'no':
                    option_1_continuation = False
                else:
                    print('Invalid choice. Please try again.')

        elif user_input == 2:
            option_2_continuation = True
            while option_2_continuation == True:
                print('You selected to do a calculations.')
                print('What type of calculation would you like to do?')
                print('1. Rectangle area')
                print('2. Rectangle Volume')
                print('3. Average')
                print('4. Exit')
                user_calculation_choice = int(input())
                if user_calculation_choice == 1:
                    print("You selected to do a calculation of a rectangle's area.")
                    rectangle_length = int(input('Enter length of rectangle: '))
                    rectangle_width = int(input('Enter width of rectangle: '))
                    area = rectangle_area(rectangle_length, rectangle_width)
                    print('The area of the rectangle is ' + str(area))

                    print('Would you wish to calculate again?')
                    user_answer = input()
                    if user_answer == 'yes':
                        option_2_continuation = True
                    else:
                        option_2_continuation = False
                elif user_calculation_choice == 2:
                    print("You selected to do a calculation of a rectangle's volume.")
                    rectangle_length = int(input('Enter length of rectangle: '))
                    rectangle_width = int(input('Enter width of rectangle: '))
                    rectangle_height = int(input('Enter height of rectangle: '))
                    volume = rectangle_volume(rectangle_length, rectangle_width, rectangle_height)
                    print('The volume of the rectangle is ' + str(volume))
                    print('Would you wish to calculate again?')
                    user_answer = input()
                    if user_answer == 'yes':
                        option_2_continuation = True
                    else:
                        option_2_continuation = False
                elif user_calculation_choice == 3:
                    print('You selected to do a calculation of the average.')
                    average_calculation_type = input('Do you know the range of your list? ')
                    if average_calculation_type == 'yes':
                        amount_of_numbers = int(input('Enter your range: '))
                        sum_of_numbers = 0
                        number = 0
                        for x in range(amount_of_numbers):
                            sum_of_numbers += number
                            number = int(input('Enter a number: '))
                            avg = average(sum_of_numbers, amount_of_numbers)
                        print('The average of the numbers is ' + str(avg))

                        print('Would you wish to calculate again?')
                        user_answer = input()
                        if user_answer == 'yes':
                            option_2_continuation = True
                        else:
                            option_2_continuation = False
                    elif average_calculation_type == 'no':
                        print('To end your list, enter a negative number.')

                        amount_of_numbers = 0
                        sum_of_numbers = 0
                        number = int(input())
                        while number > -1:
                            sum_of_numbers += number
                            amount_of_numbers += 1
                            number = int(input() )
                        avg = average(sum_of_numbers, amount_of_numbers)
                        print('The average of the numbers is ' + str(avg))

                        print('Would you wish to calculate again?')
                        user_answer = input()
                        if user_answer == 'yes':
                            option_2_continuation = True
                        else:
                            option_2_continuation = False

                elif user_calculation_choice == 4:
                    print('You selected to exit the calculations selection.')
                    option_2_continuation = False
                else:
                    print('Invalid choice. Please try again.')

        elif user_input == 3:
            program_continuation = False

        else:
            print('Invalid choice. Please try again.')

    print('Program ended.')

main()
