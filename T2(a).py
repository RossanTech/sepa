from msilib.schema import IniFile


def searchname ():
    IniFile = open ("names.txt","r")
    for s in IniFile:
        print(s)
        
def searchname():
    IniFile = open ("names.txt","r")
    for s in IniFile:
        print(s[:-1])
