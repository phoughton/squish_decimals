# -*- coding: utf-8 -*-

import names
import helpers
import config

from decimal import *

def main():
    startApplication("calc")
    helpers.use_buttons_to_enter("10/3=")
    getcontext().prec = config.PRECISION
    
    answer_should_be_this = Decimal(10.0)/Decimal(3.0) 
    test.verify(waitForObject(names.screen(answer_should_be_this), config.ANSWER_WAIT_TIMEOUT))
    