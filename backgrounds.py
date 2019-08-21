# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:24:05 2019

@author: Steffen 000
"""
import numpy as np

def bg_description(bg_name):
    if bg_name == 'Alert1':
        return '''
You gain +5 bonus to initiative. \n
You can't be surprised while you are conscious. \n
Other creatures don't gain advantage on attack rolls against you as a
result of being hidden.
'''

    elif bg_name == 'Athlete1':
        return '''
Increase your Strength or Dexterity by 1, to a maximum of 20.\n
When you are prone, standing up only requires 5 feet of movement. \n
Climbing doesn't cost you any extra movement. \n
You can make a running jump after only 5 feet on foot.
'''

    elif bg_name == 'Actor1':
        return '''
Increase your Charisma by 1, to a maximum of 20.\n
You have advantage of Charisma (Deception) and Charisma (Performance)
checks to pass yourself off as someone else.\n
You can mimic the speech of another person or the sounds made by other 
creatures. You must have heard the speech or sound for at least 1 
minute. A successful Wisdom (Insight) check contested by your Charisma
(Deception) check allows a listener to determine the effect is faked.
'''

    elif bg_name == 'Blade Master (UA)1':
        return '''
You master the shortsword, longsword, scimitar, rapier, and greatsword.
You gain the following benefits when using any of them:\n
You gain a +1 bonus to attack rolls you make with the weapon.\n
On your turn, you can use your reaction to assume a parrying stance, 
provided you have the weapon in hand. Doing so grants you a +1 bonus 
to your AC until the start of your next turn or until you’re not 
holding the weapon.\n
When you make an opportunity attack with the weapon, you have advantage
on the attack roll.
'''

    else:
        return '''
        This feat has not been added yet
        '''
      
        
bg_list = ['Alert1','Athlete1','Actor1','Blade Master (UA)1']
bg_N=len(bg_list)



def test_bg():
    for i in xrange(len(bg_list)):
        print bg_description(bg_list[i])
    return

#test_bg()
