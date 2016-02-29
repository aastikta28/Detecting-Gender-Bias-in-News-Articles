# -*- coding: utf-8 -*-

import sexmachine.detector as gender

def gender_labeling(user_input):
    #user_input = raw_input("Enter name: ")
    d = gender.Detector(case_sensitive=False)
    gen = d.get_gender(user_input)
    if gen == 'male' or gen == 'mostly_male':
        gen = 'male'
    if gen == 'female' or gen == 'mostly_female':
        gen = 'female'
    if gen == 'andy':
        gen = 'male'
    return gen
    
