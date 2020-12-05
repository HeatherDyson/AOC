import math
import re

def validateFields(passport):

    for field in passport:
        name = (field.split(":"))[0]
        value = (field.split(":"))[1]

        if name == "byr":
            if (len(value) != 4  or
                not value.isnumeric() or
                int(value) < 1920 or
                int(value) > 2003):
                return False
        elif name == "iyr":
            if (len(value) != 4  or
                not value.isnumeric() or
                int(value) < 2010 or
                int(value) > 2020):
                return False
        elif name == "eyr":
            if (len(value) != 4  or
                not value.isnumeric() or
                int(value) < 2020 or
                int(value) > 2030):
                return False
        elif name == "hgt":
            if len(value) < 4:
                return False
            units = value[-2:]
            height = int(value[0:len(value)-2])
            if units != "cm" and units != "in":
                return False
            if (units == "cm" and
                (height < 150 or
                 height > 193)):
                return False
            elif (units == "in" and
                 (height < 59 or
                 height > 76)):
                return False
        elif name == "hcl":
            if value[0] != "#" or len(value) != 7:
                return False
            string = value[1:7]
            if re.search('[^a-f0-9]', string):
                return False
        elif name == "ecl":
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        elif name == "pid":
            if (len(value) != 9 or
                not value.isnumeric()):
                return False

    return True



def main():

    #byr (Birth Year) 4 digits 1920-2003
    #iyr (Issue Year) 4 digits 2010-2020
    #eyr (Expiration Year) 4 digits 2020-2030
    #hgt (Height) num with cm 150-193 or in 59-76
    #hcl (Hair Color) hashtag w/ 6 char 0-9 or a-f
    #ecl (Eye Color) amb blu brn gry grn hzl oth
    #pid (Passport ID) 9 digits
    #cid (Country ID)
    
    #read in file
    f = open("Day4.txt",'r')
    
    passports = []
    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
    fieldsNOCID = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

    fields.sort()
    fieldsNOCID.sort()
    
    currentPassport = []
    for line in f:
        for val in (line.strip('\n')).split(" "):
            passports.append(val)
    f.close()

    passports.append("") #added to catch last passport

    
    numValid = 0
    compareFields = []
    for x in passports:
        if x != "":
            currentPassport.append(x)
            compareFields.append((x.split(":"))[0])
        else:
            compareFields.sort()
            if (compareFields == fields or
                compareFields == fieldsNOCID):
                if validateFields(currentPassport):
                    numValid += 1
            compareFields.clear()
            currentPassport.clear()
    

    print(numValid)

main()
