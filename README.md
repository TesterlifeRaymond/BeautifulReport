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
>>> python sample
``` 

或

```python

import unittest
import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('tests', pattern='test*.py')
    result = BeautifulReport.BeautifulReport(test_suite)
    result.report(description='测试deafult报告', log_path='sample/report')

```

### Report API简介

* BeautifulReport.report
    * report (
        filename -> 测试报告名称, 如果不指定默认文件名为report.html
        description -> 测试报告用例名称展示
        log_path='.' -> log文件写入路径
    )


* 运行sample之后生成如下报告

!['测试报告'](https://raw.githubusercontent.com/TesterlifeRaymond/BeautifulReport/master/img/%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A.png)

# 鸣谢:

[再见理想-飞哥](https://github.com/zhangfei19841004/ztest) 提供的HTML实现, 及Java数据展示的实现部分, 如果是Java同学请移步
