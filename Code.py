# W.I.P.
print("1.+")
print("2.-")
print("3.*")
print("4./")
print("5.²")
print("6.√")
print("7.A◻")
Operation=int(input("Please Choose an Operation."))
if(Operation ==1):
    Addend=int(input("Please Enter a Number."))
    Adder=int(input("Please Enter Another Number."))
    Addend+=Adder      
    print("Your Answer:", Addend)
elif(Operation ==2):
    Subtrahend=int(input("Please Enter a Number."))
    Minuend=int(input("Please Enter Another Number."))
    Subtrahend-=Minuend
    print("Your Answer:",Subtrahend)
elif(Operation ==3):
    Multiplicand=int(input("Please Enter a Number."))
    Multiplier=int(input("Please Enter Another Number."))
    Multiplicand*=Multiplier
    print("Your Answer:",Multiplicand)
elif(Operation ==4):
    Dividend=int(input("Please Enter a Number."))
    Divisor=int(input("Please Enter Another Number."))
    Dividend/=Divisor
    print("Your Answer:",Dividend)
elif(Operation ==5):
    Square=int(input("Please Enter a Number."))
    Square**=2
    print("Your Answer:",Square)
elif(Operation ==6):
    SquareRoot=int(input("Please Enter a Number."))
    SquareRoot**=.5
    print("Your Answer:",SquareRoot)
elif(Operation ==7):
    SquareShapeBase=int(input("Please Enter the Base of the square"))
    SquareShapeHeight=int(input("Please Enter the Height of the Square"))
    SquareShapeBase*=SquareShapeHeight
    print("Your Answer:",SquareShapeBase)
