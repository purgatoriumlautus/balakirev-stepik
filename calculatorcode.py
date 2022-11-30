def calculator():
    def calc():
        try:
            while True:
                f = input("write an example below  or ''exit'' to close the calculator\n↓   \n")
                if f == "exit":
                    print("the calculator's work has finished - returning to the menu\n")
                    break

                res = 0
                sign = 0
                signer = ''
                for index, value in enumerate(f):
                    if value == "*" or value == "/" or value == "+" or value == "-" or value == "%" or value == "^":
                        sign = index
                        signer = value

                numb1=[b for b in f[:sign]]
                numb2=[a for a in f[sign + 1:]]

                number1 = int(''.join(numb1))
                number2 = int(''.join(numb2))

                if number2 == 0 and signer == "/":
                    print("u can't divide by 0\n")
                    continue

                if signer == "+":
                    res=(number1 + number2)
                elif signer == "-":
                    res=(number1 - number2)
                elif signer == "*":
                    res=(number1 * number2)
                elif signer == "/":
                    res= round((number1 / number2),2)
                elif signer == "^":
                    res=(number1 ** number2)
                elif signer == "%":
                    res=round(((number2/100)*number1),2)
                print(f"the anwser is - {res}\n")
        except:
            print("error - please, write a correct example\n")
            calc()

    while True:
        start = input(f'''write "1" to start a calculator \nwrite anything else to stop the program \n ↓ ↓ ↓\n''')
        if start == "1":
            calc()
        else:
            print("finishing the program,goodbye...")
            break
