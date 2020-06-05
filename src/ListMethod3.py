'''
Created on 04-Jun-2020

@author: sharad
'''
# Learn anout Sort,Sorted,Reverse


alpha = ['a', 'e' ,'i' ,'c' ,'x']
#Sort method
print(alpha.sort)#alpha.sort doesn't return value
#Solution
#alpha.sort()
print(alpha)
#Sorted function
print(f'Sorted funtion {sorted(alpha)}')
print(f'Original alpha :- {alpha}')
#Sorted Back Actio
new_alpha = alpha.copy()
new_alpha.sort()
print(f'Original alpha :- {alpha}')
print(new_alpha)
#Reverse
new1_alpha = alpha[:]
new1_alpha.reverse()
print(f'Reverse Alpha:- {new1_alpha}')
#First sort Then Reverse
new3_alpha = alpha.copy()
new3_alpha.sort()
print(f'Sort and Reversed :- {new3_alpha}')
new3_alpha.sort(reverse= True)
print(f'Sort and Reverse in one step {new3_alpha}')





