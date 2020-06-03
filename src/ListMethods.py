'''
Created on 02-Jun-2020

@author: sharad
'''
import copy
table = [4,3,9,6,8,200]
print(f'Line 6 output :- {table}')
table.append(100)#insert at End
print(f'Line 8 output :- {table}')
table.insert(0,2)
print(f'Line 10 output :- {table}')
table.pop(5)#Remove
print(f'Line 12 output :- {table}')
table.extend([134])#Appending List
print(f'Line 14 output :- {table}')
newtable = table.remove(4)#Remove First Occurence
print(f'Line 16 output :- {newtable}')#None because we have used newtable =table.remove(4) and it return none means no output.We need to used insert value in newtable then must use newtable = table.remove[:]
print(f'Line 16 output impact on table list :- {table}')
#copy using Slicing index
newtable1 = table[:]
print(f'Line 16 output :- {newtable1}')
#shallow copy :-original values unchanged and only modify the new values or vice versa
newtable2 = copy.copy(table)
print(f'New table :- {newtable2}')
#Deep copy :-original values unchanged and only modify the new values or vice versa
newtable3 = copy.deepcopy(table)
print(f'New table :- {newtable3}')
table.clear()
print(f'Line 19 output :- {table}')
table.copy()
print(newtable1)
