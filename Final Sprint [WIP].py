# Hello, I'm Rachell and this is my final integration project
# here's everything I've learnt so far
# math.pi reference: https://www.w3schools.com/python/ref_math_pi.asp
# time.sleep() reference: https://www.geeksforgeeks.org/python/sleep-in-python/

import time
import math

def valid_argument(user_input): #find a way to use this for every choice involving numbers
    valid_input = False
    if valid_imput == True
    try:
        user_input_choice = int(input())
    except ValueError:
        print('Invalid selection.')

def slope(x_1,y_1,x_2,y_2):
    a = y_2 - y_1
    b = x_2 - x_1
    c = a / b
    return

def volume_rectangular_prism(l,w,h):
    volume_for_rectangular_prism = l*w*h
    return 

def volume_cylinder(r,h):
    volume_for_cylinder = math.pi * r**2 * h
    return 

def volume_pyramid(l,w,h):
    base = l*w*h
    volume_for_pyramid = base/3
    return 

def circle_area(r):
    area_for_circle = math.pi* r**2
    return 

def triangle_area(h,b):
    height_and_base_multipication = h*b
    area_for_triangle = height_and_base_multipication/2
    return

def main():
    name = input('Enter your name: ')
    print(f'Hello, {name}! Welcome to my integration project #3.')
    program_continuation = 'yes'
    while program_continuation == 'yes':
        print('Select what you wish to do')
        print('1. Calculations')
        print('2. Exit program')
        user_choice = int(input())

        if user_choice == 1:
            print('You chose to review Calculations.')
            print('Which calculation do you wish to perform?')
            print('1. Slope')
            print('2. Volume ')
            print('3. Area')
            print('4. Exit')
            user_calculation_selection = int(input())

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
                    
                    # following variable is for the user to choose 
                    # if they want to make another slope calculation.
                    user_choice_slope = input('Would you like to calculate slope again? ')
                    retry_slope = user_choice_slope.lower() #turn input to lowercase
                    if retry_slope == 'yes':
                        retry_slope_calculation = 'yes'
                    elif retry_slope == 'no':
                        retry_slope_calculation = 'no'

            elif user_calculation_selection == 2:
                retry_volumes = 'yes'
                while retry_volumes == 'yes':
                    print('Which of the following volumes do you want to calculate?')
                    print('1. Rectangular Prism')
                    print('2. Cylinder')
                    print('3. Pyramid')
                    print('4. Exit')
                    user_volume_selection = int(input())
                    if user_volume_selection == 1:
                        print('You chose to calculate volume for a rectangular prism')
                        rectangle_length = int(
                            input('Enter the length of the rectangular prism: '))
                        rectangle_width = int(
                            input('Enter the width of the rectangular prism: '))
                        rectangle_height = int(
                            input('Enter the height of the rectangular prism: '))
                        answer_volume_rectangular = volume_rectangular_prism(rectangle_length, 
                                                                                   rectangle_width, rectangle_height)
                        print('The volume for your rectangular prism is ',
                              answer_volume_rectangular)
                        
                        user_retry_volume_choice = input('Do you want to calculating volumes again? ')
                        retry_volumes_choice = user_retry_volume_choice.lower() #turn input to lowercase
                        if retry_volumes_choice == 'yes':
                            retry_volumes = 'yes'
                        elif retry_volumes_choice == 'no':
                            retry_volume = 'no'
                            
                    elif user_volume_selection == 2:
                        print('You chose to calculate volume for a cylinder')
                        cylinder_radius = int(input('Enter the radius of the cylinder: '))
                        cylinder_height = int(input('Enter the height of the cylinder: '))
                        answer_volume_cylinder = volume_cylinder(cylinder_radius, cylinder_height)
                        print('The volume for your cylinder is ', answer_volume_cylinder)
                        
                        user_retry_volume_choice = input('Do you want to calculating volumes again? ')
                        retry_volumes = user_retry_volume_choice.lower() #turn input to lowercase
                        if retry_volumes_choice == 'yes':
                            retry_volumes = 'yes'
                        elif retry_volumes_choice == 'no':
                            retry_volume = 'no'
                    
                    elif user_volume_selection == 3:
                        print('You chose to calculate volume for a Pyramid')
                        pyramid_length = int(input('Enter the length of the pyramid: ')
                        pyramid_width = int(input('Enter the width of the pyramid: ')
                        pyramid_height = int(input('Enter the height of the pyramid: ')
                        answer_volume_pyramid = volume_pyramid(l,w,h)
                        print('The volume for your pyramid is', answer_volume_pyramid)
                        
                        user_retry_volume_choice = input('Do you want to calculating volumes again? ')
                        retry_volumes = user_retry_volume_choice.lower() #turn input to lowercase
                        if retry_volumes_choice == 'yes':
                            retry_volumes = 'yes'
                        elif retry_volumes_choice == 'no':
                            retry_volume = 'no'
                    
                    elif user_volume_selection == 4:
                        retry_volume = 'no'

            elif user_calculation_selection == 3:
                retry_areas = 'yes'
                while retry_areas == 'yes':
                    print('Which of the following areas do you want to calculate?')
                    print('1. Circle')
                    print('2. Triangle')
                    print('3. Rectangle')
                    print('4. Exit')
                    user_area_selection = int(input())
                    
                    if user_area_selection == 1:
                        print('You chose to calculate the area of a circle.')
                        circle_radius =
                        circle_area_answer = circle_area(circle_radius)
                        print('The area for your circle is', circle_area_answer)
                        
                        user_retry_area_choice = input('Do you want to calculating volumes again? ')
                        retry_areas_choice = user_retry_area_choice.lower() #turn input to lowercase
                        if retry_areas_choice == 'yes':
                            retry_areas = 'yes'
                        elif retry_areas_choice == 'no':
                            retry_areas = 'no'
                    
                    elif user_area_selection == 2:
                        print('You chose to calculate the area of a triangle.')
                        triangle_height = int(input('Enter height of the triangle: '))
                        triangle_base = int(input('Enter base of the triangle: '))
                        triangle_area_answer = triangle_area(h,b)
                        print('The area for your triangle is', triangle_area_answer)
                        
                        user_retry_area_choice = input('Do you want to calculating volumes again? ')
                        retry_areas_choice = user_retry_area_choice.lower() #turn input to lowercase
                        if retry_areas_choice == 'yes':
                            retry_areas = 'yes'
                        elif retry_areas_choice == 'no':
                            retry_areas = 'no'

                    elif user_area_selection == 3:
                        print('You chose to calculate the area of a rectangle.')
                        rectangle_length = int(input('Enter length of rectangle: ')
                        rectangle_height = int(input('Enter height of rectangle: ')
                        rectangle_area_answer = rectangle_length * rectangle_height
                        print('The area for your rectangle is', rectangle_area_answer)
                        
                        user_retry_area_choice = input('Do you want to calculating volumes again? ')
                        retry_areas_choice = user_retry_area_choice.lower() #turn input to lowercase
                        if retry_areas_choice == 'yes':
                            retry_areas = 'yes'
                        elif retry_areas_choice == 'no':
                            retry_areas = 'no'
                    elif user_area_selection == 4:
                        retry_areas = 'no'
        
        elif user_choice == 2:
            print(f'Thank you for reviewing my project, {name}.')
            time.sleep(2)
            print('Exiting program...')
            time.sleep(2)
            program_continuation = 'no'

        else:
            print('Invalid choice. Please re-enter your choice.')

if __name__ == "__main__":
    main()
