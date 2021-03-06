def declareTarget():
    while True:
        target = input("Enter the target number. Integers only!")
        if checkInt(target) == True:
            break
        else:
            print("Integers only. Please try again")
            continue
    print("The Target is " + target + "")
    
    declareValues(target)

def declareValues(target):
    values=[]
    while True:
        while True:
            newValue = input("Type a number to add to list of values. Integers only!")
            if checkInt(newValue) == True:
                values.append(newValue)
                break
            else:
                print("Integers only. Please try again")
                continue
        if addValuePrompt() == True:
            continue
        else:
            break
    values.sort(key=int)
    findNearestNum(target, values)
    
def checkInt(x):
    try:
        x=int(x)
        return True
    except ValueError:
        pass
        return False
        
def addValuePrompt():
    while True:
        answer = raw_input("Add another value? y/n")
        if answer == "y" or answer == "n":
            break
        
    if answer == "y":
        return True
    elif answer == "n":
        return False
def findNearestNum(target, values):
    differences=[]
    values.sort(key=int)
    for x in values:
        difference = int(target)-int(x)
        if difference < 0:
            difference = difference * -1
        differences.append(difference)
    
    closestDifference = min(x for x in differences if x!=0)
    print("")
    print("")
    print("Target Value")
    print target
    print("")
    print("Values")
    print values
    print("")
    print("Nearest Value")
    print(values[differences.index(closestDifference)])
    
declareTarget()
