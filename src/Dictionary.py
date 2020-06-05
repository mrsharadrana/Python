'''
Created on 04-Jun-2020

@author: sharad
'''
#Dictionary is an un-ordered format to store key and value

account_Bal = {
    'ram' : 210,
    'shyam' : 650,
    'karan' : 74
    }
print(account_Bal)
print(account_Bal['karan'])

#List in Dictionary
account_CashBal = {
    'a' :['a','b'],
    'b' : 'string',
    'c' : True
    }
print(account_CashBal['b'])

#Multiple Dictionary in a list

account = [
    {    
    'a' :['a','b'],
    'b' : 'string',
    'c' : True
    },
    {
    'a' :['a','b'],
    'b' : 'string',
    'c' : True
    }
]
print(account[0]['a'])



