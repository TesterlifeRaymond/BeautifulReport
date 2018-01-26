"""
@Version: 1.0
@Project: BeautyReport
@Author: Raymond
@Data: 2017/11/15 下午5:28
@File: test_make_report.py
@License: MIT
"""
import os
import unittest
from selenium import webdriver
from lxml import etree
from BeautifulReport import BeautifulReport


class UiAutoTestCase(unittest.TestCase):
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = 'img'
    
    @staticmethod
    def parse(html, xpath):
        """
            解析页面中的元素并返回一个对象
        :param xpath: 需要获取页面中的元素对应的xpath
        :param html: 页面的html元素
        :return:
        """
        return etree.HTML(html).xpath(xpath)
    
    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @classmethod
    def setUpClass(cls):
        """ set Up method """
        cls.driver = webdriver.Firefox()
        cls.test_page = 'http://testerlife.com'
    
    def tearDown(self):
        """ tear Down method """
    
    @classmethod
    def tearDownClass(cls):
        """ tear Down method """
        cls.driver.close()

    def test_home_page_is_ok(self):
        """
        测试访问首页正常, 并使用title进行断言
        """
        self.driver.get(self.test_page)
        print('打开浏览器, 访问: {}'.format(self.test_page))
        title = UiAutoTestCase.parse(self.driver.page_source, '//title/text()')[0]
        print('获取到对应的title: {}'.format(title))
        self.assertEqual(title, "Raymond's Blog")

    @BeautifulReport.add_test_img('点击第一个文章页面前', '点击第一个文章页面后')
    def test_save_img_and_view(self):
        """
            打开首页, 截图, 在截图后点击第一篇文章连接, 跳转页面完成后再次截图
        """
        self.driver.get(self.test_page)
        self.save_img('点击第一个文章页面前')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article[1]/div[2]/header/h1/a').click()
        self.save_img('点击第一个文章页面后')
        print('跳转与保存截图完成')
        self.assertEqual(
            self.parse(self.driver.page_source, '//*[@id="post-tester_4"]/div[2]/header/h1/text()')[0].strip(),
            '测试人员,为什么要学习一门技术-(四)'
        )

    @BeautifulReport.add_test_img('test_errors_save_imgs')
    def test_errors_save_imgs(self):
        """
            如果在测试过程中, 出现不确定的错误, 程序会自动截图, 并返回失败, 如果你需要程序自动截图, 则需要咋测试类中定义 save_img方法
        """
        self.driver.get(self.test_page)
        self.driver.find_element_by_xpath('//abc')

    @BeautifulReport.add_test_img('test_success_case_img')
    def test_success_case_img(self):
        """
            如果case没有出现错误, 即使使用了错误截图装饰器, 也不会影响case的使用
        """
        self.driver.get(self.test_page)
        self.driver.find_element_by_xpath('//title/text()')
