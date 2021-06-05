import re
import io

file1 = io.open('rockyou.txt','r', encoding="latin-1")
words = file1.readlines()

str_min = input("Enter min no of characters: ")
str_up_min = input("Enter min no of uppercase characters: ")
str_dwn_min = input("Enter min no of lowercase characters: ")
str_spc_min = input("Enter min no of special characters: ")
str_num_min = input("Enter min no of numerical characters: ")

count = 0
results = []
for line in words:
    try:
        uppercase_characters = re.findall(r"[A-Z]", line)
        lowercase_characters = re.findall(r"[a-z]", line)
        numerical_characters = re.findall(r"[0-9]", line)
        special_characters = re.findall(r"[, .!?]", line)

        if len(line) >= int(str_min):
            if len(uppercase_characters) >= int(str_up_min):
                if len(lowercase_characters) >= int(str_dwn_min):
                    if len(numerical_characters) >= int(str_num_min):
                        if len(special_characters) >= int(str_spc_min):
                            count = count +1
                            results.append(line)                      
    except:
        continue

print("There are " + str(count) + " strings that match the password policy you added." )
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