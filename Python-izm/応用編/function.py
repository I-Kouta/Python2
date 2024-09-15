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

print("\n")

# クラス作成

class TestClass:

    def __init__(self, code, name): # クラスの初期化時に必ず実行される(省略できない)
        self.code = code
        self.name = name

classes = []
classes.append(TestClass(1, "テスト1")) # クラスのインスタンス化
classes.append(TestClass(2, "テスト2")) # クラスのインスタンス化

for test_cls in classes:
    print("--- クラス ---")
    print("code --> " + str(test_cls.code))
    print("name --> " + test_cls.name)
