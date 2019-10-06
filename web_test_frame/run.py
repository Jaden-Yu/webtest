import unittest
from HTMLTestRunner import HTMLTestRunner
import time

test_case = unittest.defaultTestLoader.discover('./cases','**cases.py')
suite = unittest.TestSuite()
suite.addTest(test_case)

now = time.strftime('%Y-%m-%d %H_%M_%S')

file_path ='./reports/' + 'test_report' + now + '.html'

title = '测试报告'
descr = 'Ui测试'

with open(file_path,'wb') as f:
    runner = HTMLTestRunner(stream=f,title=title,description=descr)
    runner.run(suite)
    f.close()
