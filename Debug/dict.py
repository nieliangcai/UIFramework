dict = {'status': 1, 'msg': '会员登录成功！', 'url': '/index.aspx'}

print(dict.values())
print(dict.items())

dict['school'] = 'hunanuniversity'
print(dict)
del dict['school']
print(dict)
