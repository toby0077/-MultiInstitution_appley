# -*- coding: utf-8 -*-
"""
Spyder Editor

多平台借贷公式，变量：时间和贷款平台个数
Toby QQ：231469242
"""
#时间，单位月
time=1
#平台申请个数
num_apply=8

def MultiInstitution_appley(time,num_apply):
    if time<=1/4 and num_apply>=6:
        return True
    if time<=1 and num_apply>=7:
        return True
    if time<=3 and num_apply>=9:
        return True
    if time<=6 and num_apply>=11:
        return True
    if time<=12 and num_apply>=12:
        return True
    if time<=18 and num_apply>=19:
        return True
    if time<=24 and num_apply>=19:
        return True
    if time<=60 and num_apply>=19:
        return True