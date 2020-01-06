"""
Написать тесты(pytest or unittest) к предыдущим 2 заданиям, запустив которые, я бы смог бы проверить их корректность
Обязательно проверить всю критическую функциональность
"""

import unittest
import time
from task1 import SiamObj
from task2 import Message


class TestMetaclass(unittest.TestCase):
    def test_isEqual(self):
        unit1 = SiamObj('1', '2', a=1)
        unit2 = SiamObj('1', '2', a=1)
        self.assertEqual(unit1, unit2)

    def test_notEqual(self):
        unit1 = SiamObj('1', '2', a=1)
        unit3 = SiamObj('2', '2', a=1)
        self.assertNotEqual(unit1, unit3)


class TestProperty(unittest.TestCase):

    def test_sett(self):
        self.m = Message()
        self.assertEqual(type(m.msg), str)

    def test_resetTimer(self):
        m = Message()
        initial = m.msg
        self.assertEqual(m.msg, initial)
        time.sleep(1)
        self.assertEqual(m.msg, initial)
        m.msg = 'smth'
        self.assertNotEqual(m.msg, initial)
        initial = m.msg
        time.sleep(1)
        self.assertEqual(m.msg, initial)

    def test_updateCache(self):
        m = Message()
        initial = m.msg
        self.assertEqual(m.msg, initial)
        time.sleep(1)
        self.assertEqual(m.msg, initial)


if __name__ == "__main__":
    unittest.main()
