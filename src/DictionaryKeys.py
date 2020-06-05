'''
Created on 05-Jun-2020

@author: sharad
'''
import datetime

print(datetime.date.today())
#Dictionary Keys

my_list = {
 #   [1] : 'abx', #We cannot declare list variable as Key, because List is mutable.
    'bcx' : 'bvc'
    }
print(my_list['bcx'])
my_list1 = {
    123 : 'a',
    123 : 'b'
    }
print(my_list1[123])