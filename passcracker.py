import hashlib

welcome_message = """ ***********   ****                                                             
*************  ****                                                             
****     ****  ****                       ****                               ,,,
****     ****  ****                       ****                                  
****           ***********   ********** .*******,       .,,,,,,,.,,,,,,,,,   ,,,
****           ****   ****  ****   ****   ****          .,,,   ,.,,   ,,,,   ,,,
****           ****   ****   ......****   ****          .,,,   ,.,,   ,,,,   ,,,
****     ****  ****   ****  ***********   ****          .,,,   ,.,,   ,,,,   ,,,
****     ****  ****   ****  ****   ****   ****          .,,,   ,.,,   ,,.,   ,,,
*************  ****   ****  ***********   ******* ,,,,  .,,,   ,.,,   ,,,,   ,,,"""

print(welcome_message)
found = 0
hashed_password = input('Insert the hashed password')
dict_directory = input('Insert the dictionary directory')

try:
    dict_file = open(dict_directory, 'r')
except Exception:
    print('Oops!' + dict_directory + ' Not found')
