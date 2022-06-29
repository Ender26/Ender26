while(True):
    converter = input("What do you want to convert: temperature or measurement: ")

    if converter == "temperature" or converter == "Temperature" or converter == "T":

        CorF = input("From C or F wil you convert: ")
        howMuch = float(input("How much would you like to convert: "))

        if CorF == "C":
            print(howMuch, "C in F is ", howMuch * 9/5 + 32 )

        if CorF == "F":
            print("{howMuch}F in C is " , (howMuch - 32) * 5/9)

    if converter == "measurement" or converter == "Measurement" or converter == "M":
        CMorM= input("From cm or m: ")
        howMuch = float(input("How much would you like to convert: "))
        if CMorM == "cm" or CMorM == "Cm":
            print(howMuch ,"cm in m is ",howMuch/100, "m")
        if CMorM == "m" or CMorM =="M":
            print(howMuch, "m in cm is ", howMuch*100, "cm")
    
    cont = input("Do you want to convert other thing(Y or N): ")
    if cont == "Y" or cont == "y":
        pass
    else:
        break