# A function that prints names and ages in a txt file

def searchname():
    IniFile = open("names.txt", "r")
    for s in IniFile:
        print(s[:-1])
        
        
searchname()

# A function that prints only the lines where the name starts with the letter “A”

def searchname():
    IniFile = open("names.txt", "r")
    for s in IniFile:
        if s.startswith("A"):
            print(s)
        
searchname()


# A function that reads a letter from a user and prints a name, handles case sensitivity and longer strings

def searchname():
    uname = input("Enter your first name's initial: ")
    IniFile = open("names.txt", "r")
    for s in IniFile:
        if s.lower().startswith(uname.lower()):
            print(s)

searchname()

# A function that prints only age that = 5


def searchage():
    ageLi = []
    IniFile = open("names.txt", "r")
    uAge = 5
    for s in IniFile:
        ageLi.append(s.replace('\n', ''))
    for a in ageLi:
        if str(uAge) in a:
            print(a)
            
searchage()

# A function that takes user input for age and prints out users with similar ages


def searchage():
    
    IniFile = open("names.txt", "r")
    ageLi = []
    uAge = int(input('Enter a value for age: '))
    for s in IniFile:
        
        if str(uAge) in s:
                ageLi.append(s.replace('\n', ''))
                print(s)

searchage()         
 
#Main function

def main():
    choice = int (input ('Enter 1 to Search for name and 2 to Search for Age: '))
    if choice == 1:
        
        searchname()
        
    elif choice == 2:
            
            searchage()
    else: 
        print('ICORRECT INPUT! Enter a 1 or 2')
        
main()