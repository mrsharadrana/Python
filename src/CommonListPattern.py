'''
Created on 04-Jun-2020

@author: sharad
'''
#Use of len ,join ,range
from textwrap import wrap


parent = '!'
new_parent = parent.join(['Hi' ,'man' ,'Guru' ,'Here'])
print(new_parent)
print(len(new_parent))

list_parent = list(range(3,31,3))
print(list_parent)
custom_parent = list_parent[1:10:2]
print(custom_parent)







