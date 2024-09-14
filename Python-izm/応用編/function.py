# python function.py

def testFunc(num1, num2, num3):
    if num1 == 1:
        print("足し算 : " + str(num2) + " + " + str(num3) + " = " + str(num2 + num3))
    elif num1 == 2:
        print("引き算 : " + str(num2) + " - " + str(num3) + " = " + str(num2 - num3))
    elif num1 == 3:
        print("掛け算 : " + str(num2) + " * " + str(num3) + " = " + str(num2 * num3))
    else:
        print("割り算 : " + str(num2) + " / " + str(num3) + " = " + str(num2 / num3))

testFunc(5, 3, 3)
