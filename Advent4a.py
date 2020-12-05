import math

def main():

    #byr (Birth Year)
    #iyr (Issue Year)
    #eyr (Expiration Year)
    #hgt (Height)
    #hcl (Hair Color)
    #ecl (Eye Color)
    #pid (Passport ID)
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
            compareFields.append((x.split(":"))[0])
        else:
            compareFields.sort()
            if (compareFields == fields or
                compareFields == fieldsNOCID):
                numValid += 1
            compareFields.clear()
    

    print(numValid)

main()
