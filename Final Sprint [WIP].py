# Hello, I'm Rachell and this is my final integration project
# This program performs the calculation of volumes
# and areas listed the selection menu.


# math.pi reference: https://www.w3schools.com/python/ref_math_pi.asp
# time.sleep() reference: https://www.geeksforgeeks.org/python/sleep-in-python/

import time
import math


def volume_rectangular_prism(l, w, h):
    volume_for_rectangular_prism = l * w * h
    return volume_for_rectangular_prism


def volume_cylinder(r, h):
    volume_for_cylinder = math.pi * r ** 2 * h
    return volume_for_cylinder


def volume_pyramid(l, w, h):
    base = l * w * h
    volume_for_pyramid = base / 3
    return volume_for_pyramid


def circle_area(r):
    area_for_circle = math.pi * r ** 2
    return area_for_circle


def triangle_area(h, b):
    height_and_base_multiplication = h * b
    area_for_triangle = height_and_base_multiplication / 2
    return area_for_triangle


def main():
    name = input('Enter your name: ')
    print(f'Hello, {name}! Welcome to my integration project #3.')
    user_input = False
    while not user_input:
        try:
            program_continuation = 'yes'
            while program_continuation == 'yes':
                print('Select what you wish to do.')
                print('1. Calculations')
                print('2. Exit program')
                user_choice = int(input())
                user_input = True

                if user_choice == 1:
                    program_calculations = 'yes'
                    while program_calculations == 'yes':
                        print('You chose to review Calculations.')
                        print('Which calculation do you wish to perform?')
                        print('1. Volume ')
                        print('2. Area')
                        print('3. Exit')
                        user_calculation_selection = int(input())

                        if user_calculation_selection == 1:
                            print('Which of the following volumes do you want to calculate?')
                            retry_volumes = 'yes'
                            while retry_volumes == 'yes':
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
                                    
                                    user_retry_volume_choice = input(
                                        'Do you want to calculate volumes again? ')
                                    retry_volumes = user_retry_volume_choice.lower()
                                    if retry_volumes == 'yes':
                                        retry_volumes = 'yes'
                                    elif retry_volumes == 'no':
                                        retry_volumes = 'no'

                                elif user_volume_selection == 2:
                                    print('You chose to calculate volume for a cylinder')
                                    cylinder_radius = int(
                                        input('Enter the radius of the cylinder: '))
                                    cylinder_height = int(
                                        input('Enter the height of the cylinder: '))
                                    answer_volume_cylinder = volume_cylinder(cylinder_radius,
                                                                             cylinder_height)
                                    print('The volume for your cylinder is {:.2f}'
                                          .format(answer_volume_cylinder))

                                    user_retry_volume_choice = input(
                                        'Do you want to calculate volumes again? ')
                                    retry_volumes = user_retry_volume_choice.lower()
                                    if retry_volumes == 'yes':
                                        retry_volumes = 'yes'
                                    elif retry_volumes == 'no':
                                        retry_volumes = 'no'

                                elif user_volume_selection == 3:
                                    print('You chose to calculate volume for a Pyramid')
                                    pyramid_length = int(
                                        input('Enter the length of the pyramid: '))
                                    pyramid_width = int(
                                        input('Enter the width of the pyramid: '))
                                    pyramid_height = int(
                                        input('Enter the height of the pyramid: '))
                                    answer_volume_pyramid = volume_pyramid(pyramid_length,
                                                                           pyramid_width, pyramid_height)
                                    print('The volume for your pyramid is {:.2f}'
                                          .format(answer_volume_pyramid))

                                    user_retry_volume_choice = input(
                                        'Do you want to calculate volumes again? ')
                                    retry_volumes = user_retry_volume_choice.lower()
                                    if retry_volumes == 'yes':
                                        retry_volumes = 'yes'
                                    elif retry_volumes == 'no':
                                        retry_volumes = 'no'

                                elif user_volume_selection == 4:
                                    retry_volumes = 'no'

                                else:
                                    print('Invalid selection. Please re-enter your choice.')


                        elif user_calculation_selection == 2:
                            print('Which of the following areas do you want to calculate?')
                            retry_areas = 'yes'
                            while retry_areas == 'yes':
                                print('1. Circle')
                                print('2. Triangle')
                                print('3. Rectangle')
                                print('4. Exit')
                                user_area_selection = int(input())

                                if user_area_selection == 1:
                                    print('You chose to calculate the area of a circle.')
                                    circle_radius = int(
                                        input('Enter radius of the circle: '))
                                    circle_area_answer = circle_area(circle_radius)
                                    print('The area for your circle is {:.2f}'
                                          .format(circle_area_answer))

                                    user_retry_area_choice = input(
                                        'Do you want to calculate areas again? ')
                                    retry_areas_choice = user_retry_area_choice.lower()
                                    if retry_areas_choice == 'yes':
                                        retry_areas = 'yes'
                                    elif retry_areas_choice == 'no':
                                        retry_areas = 'no'

                                elif user_area_selection == 2:
                                    print('You chose to calculate the area of a triangle.')
                                    triangle_height = int(
                                        input('Enter height of the triangle: '))
                                    triangle_base = int(
                                        input('Enter base of the triangle: '))
                                    triangle_area_answer = triangle_area(triangle_height,
                                                                         triangle_base)
                                    print('The area for your triangle is', triangle_area_answer)

                                    user_retry_area_choice = input(
                                        'Do you want to calculate areas again? ')
                                    retry_areas_choice = user_retry_area_choice.lower()
                                    if retry_areas_choice == 'yes':
                                        retry_areas = 'yes'
                                    elif retry_areas_choice == 'no':
                                        retry_areas = 'no'

                                elif user_area_selection == 3:
                                    print('You chose to calculate the area of a rectangle.')
                                    rectangle_length = int(
                                        input('Enter length of rectangle: '))
                                    rectangle_height = int(
                                        input('Enter height of rectangle: '))
                                    rectangle_area_answer = rectangle_length * rectangle_height
                                    print('The area for your rectangle is', rectangle_area_answer)

                                    user_retry_area_choice = input(
                                        'Do you want to calculate areas again? ')
                                    retry_areas_choice = user_retry_area_choice.lower()
                                    if retry_areas_choice == 'yes':
                                        retry_areas = 'yes'
                                    elif retry_areas_choice == 'no':
                                        retry_areas = 'no'

                                elif user_area_selection == 4:
                                    retry_areas = 'no'

                                else:
                                    print('Invalid selection. Please re-enter your choice.')

                        elif user_calculation_selection == 3:
                            program_calculations = 'no'

                        else:
                            print('Invalid selection. Please re-enter your choice.')

                elif user_choice == 2:
                    print(f'Thank you for reviewing my project, {name}.')
                    time.sleep(2)
                    print('Exiting program...')
                    time.sleep(2)
                    program_continuation = 'no'

                else:
                    print('Invalid selection. Please re-enter your choice.')

        except ValueError:
            print('Invalid input. Please enter an integer.')

if __name__ == "__main__":
    main()
