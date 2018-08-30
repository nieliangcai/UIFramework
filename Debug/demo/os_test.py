import os,sys
print(sys.getdefaultencoding())
# print(os.getcwd())
# # os.system('taskkill /F /IM chromedriver.exe')
# print(os.pardir)
# print(os.sep)
# print(os.name)
# print(os.system("calc"))
# test = r"C:\Users\HP\Desktop\W3CSchool_git\UIFramework"
# for i in os.walk('test'):
#     print(i)
base_path = os.path.dirname(os.path.abspath(__file__))
print(os.path.split(base_path)[-1])
print(os.path.basename(base_path))
results = os.path.join(base_path,'results','report.txt')
print(results)