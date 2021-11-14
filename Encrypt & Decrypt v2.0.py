import string
import random
all_list = list(string.ascii_letters + string.digits + string.punctuation + " ")
everything = all_list.copy()

def encypt_decrypt(all_list, everything):
    code_dict = dict(zip(all_list, everything))
    encrypt_m = []
    user_string = ""
    for letter in m:
        encrypt_m.append(code_dict[letter])
    for letter in encrypt_m:
        user_string += letter
    return user_string

while True:
    e_or_d = input("Please select e to encyrpt or d to decrypt\n")
    if e_or_d == "e":
        try:
            s = int(input("Please choose a seed number\n"))
            m = input("Please type a message you would like to encrypt\n")
            random.Random(s).shuffle(all_list)
            user_string = encypt_decrypt(all_list, everything)
            print(user_string)
            break
        except:
            print('Please only input a positive integer')
    elif e_or_d =="d":
        try:
            s = int(input("Please choose a seed number\n"))
            m = input("Please type the message you would like to dencrypt\n")
            random.Random(s).shuffle(all_list)
            user_string = encypt_decrypt(everything, all_list)
            print(user_string)
            break
        except:
            print('Please only input a positive integer')
    else:
        print("Please only select e or d")


