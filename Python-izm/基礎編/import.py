# python import.py

import testmod

test_class_1 = testmod.TestClass()
test_class_1.test_method('1')

from testmod import TestClass

test_class_2 = testmod.TestClass()
test_class_2.test_method('2')
