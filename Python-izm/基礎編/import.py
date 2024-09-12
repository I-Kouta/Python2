# python import.py

import testmod # 対象のモジュールのインポート

test_class_1 = testmod.TestClass() # インスタンスの作成
test_class_1.test_method('1') # 呼び出し

from testmod import TestClass

test_class_2 = TestClass()
test_class_2.test_method('2')
