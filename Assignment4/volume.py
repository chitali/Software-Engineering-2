def checkInput(): 
    while(True):
        try:
            length = float(input("Enter a length: "))
            if length >= 0:
                break
        except ValueError:
            print("Invalid Input.")
    while(True):
        try:
            width = float(input("Enter a width: "))
            if width >= 0:
                break
        except ValueError:
            print("Invalid Input.")
    while(True):
        try:
            height = float(input("Enter a height: "))
            if height >= 0:
                break
        except ValueError:
            print("Invalid Input")
    calcVol(length, width, height)

def calcVol(l, w, h):
    print("Volume:",  l * w * h) 


checkInput()
        