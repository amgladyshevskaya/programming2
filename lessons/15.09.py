import math
import pprint
#Задание 5.1

'''
vowels  = 'ao'
cons = 'ptk'
for v in vowels:
    for c in cons:
        print(c+v)

#Задание 5.2
nouns = 'mama rama'
verbs = 'myla krasila'
for s in nouns.split():
    for v in verbs.split():
        for o in nouns.split():
            print(s +' '+v+' '+o+'.')
'''
#Задание 1
vals = [1,2,3,4,5]
def mean(vals):
    if len(vals)>0:
        return float(sum(vals))/len(vals)
    else:
        print('n/a')


            
        
 
