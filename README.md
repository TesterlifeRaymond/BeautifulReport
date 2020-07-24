# 项目年久失修, 有问题可以直接联系作者
    qq: 58558327

# BeautifulReport
---
适用于unittest自动化测试的可视化报告

# 这是什么报告?
---

### 这是unittest自动化测试报告的生成packages

这是一个基于unittest.TestReport模块实现的测试用例模板, 可以把我们每次测试中的结果通过BeautifulReport整合成一个可视化的报表.

### 如何使用它?

```shell
>>> git clone https://github.com/TesterlifeRaymond/BeautifulReport
>>> cp -R BeautifulReport to/python/site-packages/
```

可以直接在sample路径直接运行

```shell
>>> python sample.py
``` 

或

```python

import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('../tests', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')

```

### Report API简介

* BeautifulReport.report
    * report (
        filename -> 测试报告名称, 如果不指定默认文件名为report.html
        description -> 测试报告用例名称展示
        log_path='.' -> log文件写入路径
    )

* BeautifulReport.add_test_img

如果使用报告过程中需要把测试报告的截图放在报告中, 可以使用add_test_img方法

* add_test_img (
    *pargs
)

可以在测试用例上挂载一个装饰器, 实例内容如下

`ps:` 
    
* 默认存放的图片路径是img, 需要在当前测试项目的启动路径下, 创建一个img文件夹
* 传递给装饰器的图片,在运行测试前可以不存在, 运行测试之后生成即可.
* 当文件在报告中展示后, 想要看到原图, 可以点击报告中的缩略图查看完整的截图

```python
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
        save_some_img('测试报告.png')
        self.assertIsNone(None)
```

* 运行sample之后生成如下报告

![测试报告](https://raw.githubusercontent.com/TesterlifeRaymond/BeautifulReport/master/img/%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A.png)

# 鸣谢:

[再见理想-飞哥](https://github.com/zhangfei19841004/ztest) 提供的HTML实现, 及Java数据展示的实现部分, 如果是Java同学请移步
