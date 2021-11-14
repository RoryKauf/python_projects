import random
while True:
    e_or_d = input("Please select e to encyrpt or d to decrypt\n")
    if e_or_d == "e":
        m = list(input("Please enter a message\n"))
        s = int(input("Please choose a seed number\n"))
        random.Random(s).shuffle(m)
        en_message = ""
        for letter in m:
            en_message += letter
        print(en_message)
        break
    elif e_or_d =="d":
        s = int(input("What is the seed number for the message?\n"))
        m = list(input("Please enter your encrypted message\n"))
        m_len = len(m)
        i = list(range(0, (m_len)))
        random.Random(s).shuffle(i)
        m_dict = dict(zip(i,m))
        de_m = []
        for i in range(0, m_len):
            de_m.append(m_dict[i])
        dec_message = ""
        for letter in de_m:
            dec_message += letter
        print(dec_message)
        break
    else:
        print("Please only select e or d")








