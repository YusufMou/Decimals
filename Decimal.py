number = float(input("Input any number with decimal: "))
dp = int(input("How many decimal places: "))
def calc():
    round = number*10 ** dp + 0.5
    round = float(round)
    print (str(round))
    
calc()    