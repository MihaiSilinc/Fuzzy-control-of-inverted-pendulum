# -*- coding: utf-8 -*-
from math import *
"""
In this file your task is to write the solver function!

"""

def solver(t,w):
    """
     Parameters
     ----------
     t : TYPE: float
         DESCRIPTION: the angle theta
     w : TYPE: float
         DESCRIPTION: the angular speed omega

     Returns
     -------
     F : TYPE: float
         DESCRIPTION: the force that must be applied to the cart
     or

     None :if we have a division by zero

     """
    nvb = (-55, -25)
    nb = (-40, -10)
    n = (-20, 0)
    zo = (-5, 5)
    p = (0, 20)
    pb = (10, 40)
    pvb = (25, 55)
    angleMembersOld = [nvb, nb, n, zo, p, pb, pvb]
    angleMembers = []
    nb = (-13, -3)
    n = (-6, 0)
    zo = (-1, 1)
    p = (0, 6)
    pb = (3, 13)
    angularSMembersOld = [nb, n, zo, p, pb]
    angularSMembers = []
    for i in angleMembersOld:
        x = t
        b = (i[0] + i[1]) * 0.5
        a = i[0]
        c = i[1]
        angleMembers.append(max(0, min((x-a)/(b-a), 1, (c-x)/(c-b))))


    """
    For angle members list:
    0 - NVB
    1 - NB
    2 - N
    3 - ZO
    4 - P
    5 - PB 
    6 - PVB
    """

    for i in angularSMembersOld:
        x = w
        b = (i[0] + i[1]) * 0.5
        a = i[0]
        c = i[1]
        angularSMembers.append(max(0, min((x - a) / (b - a), 1, (c - x) / (c - b))))


    """
        For angular speed members list:
        0 - NB
        1 - N 
        2 - ZO
        3 - P
        4 - PB
        """
    maximum = []
    # 𝑚𝑎𝑥(𝑐𝑒𝑙𝑙𝑠 𝑡ℎ𝑎𝑡 𝑎𝑟𝑒 labeled Z as an example  𝑚𝑎𝑥(0, 0, 0, 0. 1(6), 0) = 0. 1(6))
    """
     1 -> PVVB
     2 -> PVB
     3 -> PB
     4 -> P 
     5 -> ZO
     6 -> N
     7 -> NB
     8 -> NVB
     9 -> NVVB
     
     the numbers being the position for each member in resultList list
    """
    resultList = []
    for i in range(11):
        resultList.append(-1)
    for i in range(5):
        for j in range(7):
            if i + j == 1 or i + j == 0:
                if resultList[1] < min(angleMembers[j], angularSMembers[i]) or resultList[1] == -1:
                    resultList[1] = min(angleMembers[j], angularSMembers[i])
            elif i + j == 9 or i + j == 10:
                if resultList[9] < min(angleMembers[j], angularSMembers[i]) or resultList[9] == -1:
                    resultList[9] = min(angleMembers[j], angularSMembers[i])
            else:
                if resultList[i+j] < min(angleMembers[j], angularSMembers[i]) or resultList[i+j] == -1:
                    resultList[i+j] = min(angleMembers[j], angularSMembers[i])
    numerator = 0
    for i in range(10):
        if i == 0:
            continue
        numerator += resultList[i] * (i-5) * 8

    denominator = 0
    for i in range(10):
        if i == 0:
            continue
        denominator += resultList[i]

    if denominator !=0:
        return numerator / denominator
    else:
        return None





