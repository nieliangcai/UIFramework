import requests

class github_api_test():
    username = 'nieliangcai'
    password = 'yyy0909'
    def get_test(self):
        res = requests.get('https://api.github.com/user',auth=(self.username,self.password))
        return res

res = github_api_test()
res = res.get_test()
print(res.status_code)
print(res.headers['content-type'])
print(res.json()['id'])