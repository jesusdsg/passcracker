import hashlib

welcome_message = """

*
$$$$$$$\                                                                      $$\                           
$$  __$$\                                                                     $$ |                          
$$ |  $$ |$$$$$$\   $$$$$$$\  $$$$$$$\  $$$$$$$\  $$$$$$\  $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$$$$$$  |\____$$\ $$  _____|$$  _____|$$  _____|$$  __$$\ \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
$$  ____/ $$$$$$$ |\$$$$$$\  \$$$$$$\  $$ /      $$ |  \__|$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
$$ |     $$  __$$ | \____$$\  \____$$\ $$ |      $$ |     $$  __$$ |$$ |      $$  _$$<  $$   ____|$$ |      
$$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
\__|      \_______|\_______/ \_______/  \_______|\__|      \_______| \_______|\__|  \__| \_______|\__|      
                                                                                                            

"""

menu = {
    1: 'MD5 Password',
    2: 'Sha1 Password',
    3: 'Sha512 Password'
}


def print_menu():
    # show the main menu to get the hash type
    print('Please, Select the hash type of your password: ')
    for key in menu.keys():
        print(key, ' - ', menu[key])
    print('')


def decrypt_by_option(option, cipher_word):
    # decrypt based in the selected option
    if option == 1:
        return hashlib.md5(cipher_word.strip())
    if option == 2:
        return hashlib.sha1(cipher_word.strip())
    if option == 3:
        return hashlib.sha512(cipher_word.strip())


def decrypt_password(option):
    # main decrypt method
    found = False
    for word in dict_file:
        cipher_word = word.encode('utf-8')
        hashed_word = decrypt_by_option(option, cipher_word)
        digest = hashed_word.hexdigest()

        if digest == hashed_password:
            print('\33[92m' + 'Password found: ' + '\x1b[0m' + word)
            found = True

    if not found:
        print('\033[91m' + "Error, password not found in file " +
              '\033[0m' + dict_directory)


# initialize the script
print('\33[92m' + welcome_message + '\x1b[0m')
print_menu()
option = 0

while option == 0:
    try:
        option = int(input('Insert the menu option: '))
    except Exception:
        print('Oops! Something went wrong, please insert a number')

print('\n')

# get the encrypted password and the dictionary
hashed_password = input('Insert the hashed password: ')
dict_directory = input('Insert the dictionary directory: ')

try:
    dict_file = open(dict_directory, 'r')
except Exception:
    print('Oops!' + dict_directory + ' Not found')

if option != 0:
    decrypt_password(option)
