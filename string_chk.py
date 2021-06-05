import re
import io

file1 = io.open('rockyou.txt','r', encoding="latin-1")
words = file1.readlines()

print(" ")
print("Welcome to the rockyou string searcher.")

print("  _____            _  __     __                             ")
print(" |  __ \          | | \ \   / /                             ")
print(" | |__) |___   ___| | _\ \_/ /__  _   _                     ")
print(" |  _  // _ \ / __| |/ /\   / _ \| | | |                    ")
print(" | | \ \ (_) | (__|   <  | | (_) | |_| |                    ")
print(" |_|  \_\___/ \___|_|\_\ |_|\___/ \__,_|                    ")
print("   _____ _        _              _____ _               _    ")
print("  / ____| |      (_)            / ____| |             | |   ")
print(" | (___ | |_ _ __ _ _ __   __ _| |    | |__   ___  ___| | __")
print("  \___ \| __| '__| | '_ \ / _` | |    | '_ \ / _ \/ __| |/ /")
print("  ____) | |_| |  | | | | | (_| | |____| | | |  __/ (__|   < ")
print(" |_____/ \__|_|  |_|_| |_|\__, |\_____|_| |_|\___|\___|_|\_\ ")
print("                           __/ |                            ")
print("                          |___/                             ")

print(" ")
print("The rockyou.txt wordlist is a dictionary used to perform different types of password cracking attacks. \nThe rockyou wordlist comes prepackaged with a number of hacking tools and is the go to list for password attacks. \nThis simple tool lets you search the list for a specific string and it will return a count and all matches. \n")
print(" ")
substr = input("What string would you like to search for? ")
print(" ")

count = 0
results = []

for line in words:
    try:
       if substr in line:
           count = count + 1
           results.append(line)
    except:
        continue

print("There are " + str(count) + " passwords that contain the string '" + substr + "'.")
print("That's " + str(count/len(words)*100) + "%.")
print(" ")

response = input("Would you like to see them? (Y/N) ")
print(" ")
if response.upper() == "Y":
    for things in results:
        print(things)
else:
    print("k. bye.")
    exit()
