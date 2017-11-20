"""
@Version: 1.0
@Project: BeautyReport
@Author: Raymond
@Data: 2017/11/15 下午5:28
@File: test_make_report.py
@License: MIT
"""
import unittest
from BeautifulReport import BeautifulReport


class UnittestCaseSecond(unittest.TestCase):
    """ 测试代码生成与loader 测试数据"""
    
    def test_equal(self):
        """
            test 1==1
        :return:
        """
        import time
        time.sleep(1)
        self.assertTrue(1 == 1)
    
    @BeautifulReport.add_test_img('测试报告.png')
    def test_is_none(self):
        """
            test None object
        :return:
        """
        print(111)
        self.assertIsNone(None)
    
    def test_isupper(self):
        """
            test isupper
        :return:
        """
        print(222)
        self.assertTrue('FOO'.isuper())
        self.assertFalse('Foo'.isupper())


class UnittestTestCase(unittest.TestCase):
    """ 测试代码生成与loader 测试数据"""
    
    @unittest.skip('Pass')
    def test_equal(self):
        """
            test 1==1
        :return:
        """
        print('开始测试')
        print('这个测试将被跳过')
        self.assertTrue(1 != 1)
    
    @BeautifulReport.add_test_img('测试报告.png', '测试报告.png')
    def test_is_none(self):
        """
            test None object
        :return:
        """
        print('开始测试')
        print('这个测试是判断None != None')
        self.assertIsNone(None)
    
    def test_isupper(self):
        """
            test isupper
        :return:
        """
        print('开始测试')
        print('这个测试是判断大小写是否正确')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
