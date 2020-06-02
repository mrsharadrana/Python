'''
Created on 02-Jun-2020

@author: sharad
'''

cart = ['PC' , 'Toys' ,'Food', 'Texst']
print(cart)
cart[0] = 'Mobile'
print(cart)
new_cart = cart[:]
print(new_cart)
new_cart[0] = 'MCc'
cart[0] = 'DxC'
print(new_cart)
print(cart)

