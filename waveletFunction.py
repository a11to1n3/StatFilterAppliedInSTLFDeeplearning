#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:16:17 2020

@author: duypham
"""

import pywt

def waveletFunc(signal, wavelet="db2", level=1):
    coeff = pywt.wavedec(signal, wavelet, level)
    cA1, cD1 = coeff
    cD11 = np.zeros_like(cD1)
    cA11 = np.zeros_like(cA1)    
    coeff1 = list([cA1,cD11])
    coeff2 = list([cA11,cD1])
    highCancelledSignal = pywt.waverec(coeff1, wavelet)
    lowCancelledSignal = pywt.waverec(coeff2, wavelet)
    return highCancelledSignal, lowCancelledSignal, cA1, cD1

def extract(data_load):
    high_end = data_load.copy()
    low_low_end = data_load.copy()
    low_high_end = data_load.copy()
    _,high_end[:,:,0], low_init, high_init = waveletFunc(data_load[:,:,0])
    low_low_init, low_high_init,_,_  = waveletFunc(low_init)
    low_low_coeff = list([low_low_init, high_init])
    low_high_coeff = list([low_high_init, high_init])
    low_low_end[:,:,0] = pywt.waverec(low_low_coeff,'db2')
    low_high_end[:,:,0] = pywt.waverec(low_high_coeff,'db2')
    return high_end, low_low_end, low_high_end