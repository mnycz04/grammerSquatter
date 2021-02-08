"""Python program that automatically does grammar squats"""

from time import sleep

from num2words import num2words
from pynput import keyboard
from pynput.keyboard import Controller, Key


def on_press(key):
    if key == Key.ctrl_r:
        return False


kb = Controller()


while 1:
    num_squats = input("Enter the number of squats to do: ")
    num_squats = int(num_squats.strip())

    with keyboard.Listener(
            on_press=on_press) as ears:
        ears.join()

    for i in range(num_squats):
        kb.press(Key.ctrl_l)
        sleep(2)
        kb.release(Key.ctrl_l)
        kb.tap('Y')
        kb.type(f"{num2words(i + 1).title().replace('-', ' ')}.")
        kb.tap(Key.enter)
