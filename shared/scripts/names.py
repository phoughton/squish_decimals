# encoding: UTF-8

from objectmaphelper import *

calculator_window = {"text": "Calculator", "type": "Window"}
buttons = {}
buttons['0'] = {"container": calculator_window, "occurrence": 6, "text": "", "type": "Button"}
buttons['1'] = {"container": calculator_window, "occurrence": 5, "text": "", "type": "Button"}
buttons['2'] = {"container": calculator_window, "occurrence": 11, "text": "", "type": "Button"}
buttons['3'] = {"container": calculator_window, "occurrence": 16, "text": "", "type": "Button"}
buttons['4'] = {"container": calculator_window, "occurrence": 4, "text": "", "type": "Button"}
buttons['5'] = {"container": calculator_window, "occurrence": 10, "text": "", "type": "Button"}
buttons['6'] = {"container": calculator_window, "occurrence": 15, "text": "", "type": "Button"}
buttons['7'] = {"container": calculator_window, "occurrence": 3, "text": "", "type": "Button"}
buttons['8'] = {"container": calculator_window, "occurrence": 9, "text": "", "type": "Button"}
buttons['9'] = {"container": calculator_window, "occurrence": 14, "text": "", "type": "Button"}
buttons['.'] = {"container": calculator_window, "occurrence": 17, "text": "", "type": "Button"}

buttons['/'] = {"container": calculator_window, "occurrence": 20, "text": "", "type": "Button"}
buttons['+'] = {"container": calculator_window, "occurrence": 23, "text": "", "type": "Button"}
buttons['*'] = {"container": calculator_window, "occurrence": 21, "text": "", "type": "Button"}
buttons['-'] = {"container": calculator_window, "occurrence": 22, "text": "", "type": "Button"}
buttons['='] = {"container": calculator_window, "occurrence": 28, "text": "", "type": "Button"}

buttons['C'] = {"container": calculator_window, "occurrence": 13, "text": "", "type": "Button"}
buttons['-'] = {"container": calculator_window, "occurrence": 22, "text": "", "type": "Button"}
buttons['←'] = {"container": calculator_window, "occurrence": 2, "text": "", "type": "Button"}


def screen(screen_value):
    if not isinstance(screen_value, str):
        screen_text = str(screen_value)
    else:
        screen_text = screen_value
        
    return {"container": calculator_window, "text": screen_text, "type": "Label"}
