import string
import random

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

print('\33[34m' + welcome_message + '\x1b[0m')

pwd_length = 0
while pwd_length == 0:
    try:
        pwd_length = int(input('Insert the password lenght: '))
    except Exception:
        print('\033[91m' + "Please, insert a valid lenght." +
              '\033[0m')

# Get the alphabets by type
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

alphabet = lower + upper + num + symbols

# Generate a random string using the alphabet
generated = random.sample(alphabet, pwd_length)

pwd = "".join(generated)

print('\33[92m' + 'Password generated: ' + '\x1b[0m' + pwd)
