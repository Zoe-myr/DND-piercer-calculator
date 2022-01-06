#this code takes any full name and gets the initials
#even for names with no or multiple middle names
fullName = input("enter your full name: ")
nameSplit = fullName.split(' ')
names = 0
for index in nameSplit:
    print(nameSplit[names][0], end='')
    names += 1
 
