import requests,os
import unittest,json
from random import randint

class test_api(unittest.TestCase):

    str_int = ""
    for i in range(8):
        int_num = str(randint(0, 9))
        str_int+=int_num

    def setUp(self):
        self.url = "http://118.31.19.120:3000/api/v1"
        self.accesstoken = '707995c0-f643-4a27-8df1-66be03e528e5'
        self.id = "5b6938070ec61db748a534ff"
        self.title = "小心走火12345阿萨德 %s" %self.str_int
        self.content = "小心走火，修改了刚刚新增的主题-->八位随机数"

    def test_get_topics(self):
        '''查看所有主题'''
        pramas = {
            'page':1,
            "tab":"share",
            "limit":20,
            "mdrender":"false"
        }
        response = requests.get(url=self.url+'/topics',params=pramas)
        for i in range(len(response.json()['data'])):
            dicts = dict(response.json()['data'][i])
            # print(dicts['id'])
            self.assertEqual(response.status_code,200)
            return dicts['id']

    def test_topic_id(self):
        '''根据ID，查看一个主题'''
        params  = {
            "mdrender":"true",
            "accesstoken":self.accesstoken
        }
        response = requests.get(url=self.url+'/topic/'+self.id,params=params)
        datas = response.json()['data']
        self.assertEqual(datas['id'],self.id)
        self.assertIn('小姑凉',datas['title'])
        return datas['id'],datas['title']

    def test_new_topic(self):
        '''新增一个主题'''
        params = {
            "accesstoken":self.accesstoken,
            "title":self.title,
            "tab":"share",
            "content":"mac for test python"
        }
        response = requests.post(url=self.url+'/topics',data=params)
        self.assertEqual(response.json()['success'],True)
        return response.json()['topic_id']

    def test_edit_topic(self):
        '''编辑之前新增的主题 ,api /topics/update '''
        data = {
            "accesstoken": self.accesstoken,
            "topic_id":self.test_new_topic(),
            "title":self.str_int,
            "tab":"share",
            "content":self.content
        }
        datas = json.loads(data)
        response = requests.post(url=self.url+'/topics/update',data=datas)
        print(response.json())

if __name__=="__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTests([test_api("test_topic_id"),test_api("test_new_topic"),test_api("test_edit_topic")])
    # Base_path = os.path.dirname(os.path.abspath(__file__))
    # report = os.path.join(Base_path,'results','text.log')
    # with open(report,'wb') as f:
    runner = unittest.TextTestRunner(verbosity=2,descriptions='python report')
    runner.run(suite)