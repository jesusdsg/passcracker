import hashlib

welcome_message = """                                                                           *(*                       
(((((((.                             .(((((((                             *(*                       
((.  ((( ,((((((   ((((((,  *((((((  (((      /((((((# .((((((/   ((((((. *(* /((/  ,(((((   (((((((
((. *(((      ((/ /(((     ,(((.    (((/      /((( /((      .((  (((*     *(%#((   (((  (((  ((((/#(
((((((.  ,((((((/  *(((((.  ,(((((( ((((      /((      ,#((((((  (((      *((((,   ((((((((  (((    
((.      ((/ (((/      (((      ,((, (((%. *( /((      (((  (((  (((*  ,  *(*/(((  (((/      (((    
((.      ,((((/(/ (((((((. ,((((((*   ,(((((/ /((      .(((((((   ((((((. *(* .(((. (((((((  (((     """

print(welcome_message)
found = 0
hashed_password = input('Insert the hashed password')
dict_directory = input('Insert the dictionary directory')

try:
    dict_file = open(dict_directory, 'r')
except Exception:
    print('Oops!' + dict_directory + ' Not found')

for word in dict_file:
    cipher_word = word.encode('utf-8')
    hashed_word = hashlib.md5(cipher_word().strip())
    digest = hashed_word.hexdigest()

    if digest == hashed_password:
        print('Password found: ' + word)
        found = found + 1

if not found:
    print('Password not found in file ' + dict_directory)
