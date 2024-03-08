import os
if __name__ == '__main__':
    os.system('pytest -s -v ../testcase/test_open_baidu.py --alluredir=../report --clean-alluredir')
    os.system('allure generate ../report -o ../report-html --clean')