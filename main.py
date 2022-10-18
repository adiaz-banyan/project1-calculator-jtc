import math
# Created separate funcs to help me write less code. I don't think it did this time but it would've maybe if i had a larger project. then i could reuse these functions separately.


def calc_tip(percent_tip, total_amount):
    if percent_tip != '':
        decimal_tip = float(percent_tip)/100
        tip = float(total_amount) * decimal_tip
        return tip
    else:
        return ''

# first i had kept the numbers as they were but i kept getting an answer that was either too manyh decimal so i rounded up. again wasn't what we were looking for so i rounded down. seemed to work.


def round_down_float_to_2_decimals(num):
    return math.floor(num * 100) / 100


def calc_total_amount(num_people, tip, food_cost, tax):
    # when paying with tip and splitting.
    if num_people != '' and tip != '':
        what_to_pay_for = tip + float(food_cost) + tax
        split_the_bill = what_to_pay_for/float(num_people)

        print(
            f'Total Bill: ${round_down_float_to_2_decimals(what_to_pay_for)}\nEach person should pay ${round_down_float_to_2_decimals(split_the_bill)}')
    # No tip no people
    elif tip == '' and num_people == '':

        what_to_pay_for = float(food_cost) + tax
        print(
            f'Total Bill: ${round_down_float_to_2_decimals(what_to_pay_for)}')
    # tip no people
    elif tip != '' and num_people == '':
        what_to_pay_for = float(food_cost) + tax + tip
        print(
            f'Total Bill: ${round_down_float_to_2_decimals(what_to_pay_for)}')

    elif tip == '' and num_people != '':
        what_to_pay_for = float(food_cost) + tax
        split_the_bill_with_no_tip = what_to_pay_for/float(num_people)
        print(
            f'Total Bill: ${round_down_float_to_2_decimals(what_to_pay_for)}\nEach person should pay ${(round_down_float_to_2_decimals(split_the_bill_with_no_tip))}')

    runningProgram()

# I tried using multiple try and excepts but it sort of hard to understand their behaviors and when to use them and when not to.


def calculate_func():
    food_cost = input('Enter the bill for food: ')
    try:
        sales_tax = float(food_cost) * .1
        make_sure_people = input(
            'If you are splitting the bill enter the amount of people the bill will be split by, if not leave blank: ')
        make_sure_tip = input(
            'If you are getting a tip, enter the percentage if not leave blank: ')

        if make_sure_people != '' or make_sure_tip != '':
            tip = calc_tip((make_sure_tip), food_cost)
            return calc_total_amount(make_sure_people, tip,
                                     food_cost, sales_tax)
        else:
            total_no_split_no_tip = float(food_cost) + sales_tax
            print(
                f'Total Bill: ${round_down_float_to_2_decimals(total_no_split_no_tip)}')
        runningProgram()
    except TypeError:
        print('Please enter a valid number.')
        calculate_func()
    except ValueError:
        print('Please enter a valid number')
        calculate_func()

# simple program to run something infinitely until the user literally does not want to anymore.


def runningProgram():
    run = input(
        "Calculate another Bill? If so enter y or yes, or leave blank if you're done: ")
    while run != '':
        calc_total_amount()


calculate_func()


# It's in my opinion that tests usually do more harm than good.
# I'm reading the docs and it still doesn't make sense as to why we need them. You guys ofc do to make sure we do things right. But for testing and quality assurance this is completely unnecessary.
