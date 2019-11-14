# -*- coding: utf-8 -*-

import names
import helpers
import config

from decimal import *

def main():
    startApplication("calc")
    helpers.use_buttons_to_enter("190/3=*2=")
    getcontext().prec = config.PRECISION
    
    answer_should_be_this = (Decimal(190.0)/Decimal(3.0))*Decimal(2.0)
    test.verify(waitForObject(names.screen(answer_should_be_this), config.ANSWER_WAIT_TIMEOUT))
    