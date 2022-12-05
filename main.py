# Import statements
import RPi.GPIO as GPIO
from time import sleep, time
import random

GPIO.setmode(GPIO.BOARD)

DATA = 37
LATCH = 35
CLOCK = 33
BUTTON_1 = 40
BUTTON_2 = 38

GPIO.setup((DATA, LATCH, CLOCK), GPIO.OUT)
GPIO.setup((BUTTON_1, BUTTON_2), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output((CLOCK, LATCH), 0)

CHARACTER = {
    "P": [0, 0, 0, 0, 0, 0, 0, 0],
    "1": [0, 0, 0, 0, 0, 1, 1, 0],
    "2": [0, 1, 0, 1, 1, 0, 1, 1],
    "3": [0, 1, 0, 0, 1, 1, 1, 1],
    "4": [0, 1, 1, 0, 0, 1, 1, 0],
    "5": [0, 1, 1, 0, 1, 1, 0, 1],
    "6": [0, 1, 1, 1, 1, 1, 0, 1],
    "7": [0, 0, 0, 0, 0, 1, 1, 1],
    "8": [0, 1, 1, 1, 1, 1, 1, 1],
    "9": [0, 1, 1, 0, 1, 1, 1, 1],
    "0": [0, 0, 1, 1, 1, 1, 1, 1],
    "A": [0, 1, 1, 1, 0, 1, 1, 1],
    "B": [0, 1, 1, 1, 1, 1, 0, 0],
    "C": [0, 0, 1, 1, 1, 0, 0, 1],
    "D": [0, 1, 0, 1, 1, 1, 1, 0],
    "E": [0, 1, 1, 1, 1, 0, 0, 1],
    "F": [0, 1, 1, 1, 0, 0, 0, 1],
    "X": [0, 0, 0, 0, 0, 0, 0, 0]
}



"""Function definitions"""

def tick(): # Completes a clock cycle 
    GPIO.output(CLOCK, 1)
    GPIO.output(CLOCK, 0)

def release(): # Outputs bits in parallel 
    GPIO.output(LATCH, 1)
    GPIO.output(LATCH, 0)


def display_character(character: str): # Sends character byte to display
    for status in CHARACTER[character] + CHARACTER[character]:
        GPIO.output(DATA, status)
        tick()
    release()

# def digit_select(digit: int): # Sets one digit to ground and others to not ground
#     off_list = [DIGIT_1, DIGIT_2, DIGIT_3, DIGIT_4]
#     off_list.remove(digit)
#     for off_digit in off_list:
#         GPIO.output(off_digit, 1)
#     GPIO.output(digit, 0)

# def four_digit(statement: str): # Displays entire 4 digit "word"
#     digit_list = [DIGIT_1, DIGIT_2, DIGIT_3, DIGIT_4]
#     while GPIO.input(BUTTON_1) == GPIO.LOW and GPIO.input(BUTTON_2) == GPIO.LOW:
#         for cycles in range(4):
#             for i in range(4): 
#                 clean() 
#                 release()
#                 digit_select(digit_list[i])
#                 display_character(statement[i])
#                 sleep(0.0005)
#     for i in range(4): 
#         clean() 
#         release()
#         digit_select(digit_list[i])
#         display_character("X")

# def dice_select_cycle(index: int) -> int:  # Cycles through die on button press 
#     dice_numbers = ["X4", "X6", "X8", "10", "12", "20"]
#     if index == 5:
#         next_index = 0
#     else: 
#         next_index = index + 1
#     to_be_displayed = "XD" + dice_numbers[next_index]
#     four_digit(to_be_displayed)
#     return(next_index)

# def dice_pick(current_dice_index): # "Rolls" selected dice 
#     dice_numbers = [4, 6, 8, 10, 12, 20]
#     dice_value = dice_numbers[current_dice_index]
#     value = str(random.randint(1, dice_value))
#     if len(value) == 1:
#         value = "X" + value
#     four_digit("XX" + value)



"""Main script"""

try:
    display_character("8")
    # four_digit("XD20")
    # current_dice_index = 5
    # ready_to_change_dice = False
    # ready_to_pick_dice = False
    # while True: 
    #     if GPIO.input(BUTTON_1) == GPIO.HIGH:
    #         ready_to_change_dice = True
    #     if GPIO.input(BUTTON_1) == GPIO.LOW and ready_to_change_dice == True:
    #         current_dice_index = dice_select_cycle(current_dice_index)
    #         ready_to_change_dice = False

    #     if GPIO.input(BUTTON_2) == GPIO.HIGH:
    #         ready_to_pick_dice = True
    #     elif GPIO.input(BUTTON_2) == GPIO.LOW and ready_to_pick_dice == True:
    #         dice_pick(current_dice_index)
    #         ready_to_pick_dice = False

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()