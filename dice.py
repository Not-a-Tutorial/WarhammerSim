#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from math import ceil

def roll(value):
    """
    Description
    -----------
    A basic function that allows either a D6 roll or a D3 roll following the Warhammer 40k rules with minor error handling.
    
    Parameters
    ----------
    value : str
        Either D6 or D3
    
    Returns
    -------
    throw : int
        The result of a single die roll
    """
    while True:
        if value == "D6":
            #Chooses a random number from 1 to 6, inclusive
            throw = randint(1,6)
            return throw
        if value == "D3":
            #Chooses a number 1 to 6 and then divides by two, rounding up
            throw = ceil(randint(1,6)/2)
            return throw
        else:
            print("Enter either D6 or D3")
            value = input()

def outcome(rolls, tray, thresh, crit_succeed, crit_fail):
    """

    Parameters
    ----------
    rolls : int
        Number of dice being thrown.
    tray : list
        The results of dice rolls where [0] is standard and [1] is critical.
    thresh : int
        The value a die needs to equal or exceed to succeed.
    crit_succeed : int
        The value a die needs to automatically succeeds.
    crit_fail : int
        The value a die needs to automatically fail.

    Returns
    -------
    tray : list
        The updated results of standard and critical successes.

    """
    for i in range(rolls):
        temp = roll("D6")
        print("Rolled: "+str(temp))
        if temp == crit_fail:
            continue
        if temp >= thresh:
            tray[0] = tray[0] + 1
        if temp >= crit_succeed:
            tray[1] = tray[1] + 1
    return tray

if __name__ == '__main__':
    # Test Error Handling
    # roll("ace")
    # Test D3
    # print(roll("D3"))
    # Test D6
    print(roll("D6"))
