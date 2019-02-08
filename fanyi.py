import urllib.request
import json
import urllib.parse

content = input('请输入要翻译的内容:')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'


data = {}
data['i'] = content
data['type'] = 'AUTO'
data['doctype'] = 'json'
data['keyfrom'] = 'fanyi.web'
data['version'] = '2.1'
data['typoResult'] = 'false'
data['ue'] = 'UTF-8'
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
#print(html)
target = json.loads(html)
print('翻译结果：%s' % (target['translateResult'][0][0]['tgt']))
