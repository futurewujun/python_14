# -*- coding: utf-8 -*-
# 1：引入单元测试
# 2：引入ddt
# 3：测试用例里面引入引入try...except..finally，并写回测试结果
# 4：引入日志
# 5：完成用例的可配置化：想跑哪条用例，就在配置文件里面写好
# 6：搞定全局变量（path变量，数据与文件分离）

import unittest
import HTMLTestRunnerNew
from API_Program.API_03.common import project_path
from API_Program.API_03.common.run_case import RunCase
class RunTest:
    '''生成测试报告'''
    def run_test(self):
        suite=unittest.TestSuite()  #测试套件
        loader=unittest.TestLoader()    #加载用例
        suite.addTest(loader.loadTestsFromTestCase(RunCase))
        # 执行用例
        with open(project_path.report_path,'wb') as file:
            runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                    verbosity=2,
                                                    title='前程贷接口测试报告',
                                                    description='注册接口测试报告',
                                                    tester='未来')
            runner.run(suite)
a=RunTest()
a.run_test()
