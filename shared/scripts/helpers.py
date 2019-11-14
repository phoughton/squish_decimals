# -*- coding: utf-8 -*-

import squish
import names

def use_buttons_to_enter(key_string):
    for index in range(len(key_string)):
        char_key = key_string[index]
        squish.clickButton(squish.waitForObject(names.buttons[char_key]))
        