# -*- coding: utf-8 -*-

import names
import helpers
import config

def main():
    startApplication("calc")
    helpers.use_buttons_to_enter("2*4=")
    
    answer_should_be_this = 8
    test.verify(waitForObject(names.screen(answer_should_be_this), config.ANSWER_WAIT_TIMEOUT))
    