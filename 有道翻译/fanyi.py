import urllib.request
import json
import urllib.parse
import time

while True:
    content = input('请输入要翻译的内容:(输入q!退出)')
    if content == 'q!':
        break
    
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    '''
    data = {}
    data['i'] = content
    data['type'] = 'AUTO'
    data['doctype'] = 'json'
    data['keyfrom'] = 'fanyi.web'
    data['version'] = '2.1'
    data['typoResult'] = 'false'
    data['ue'] = 'UTF-8'
    data = urllib.parse.urlencode(data).encode('utf-8')


    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')


    #response = urllib.request.urlopen(url,data)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    #print(html)
    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']
    print(target)
    time.sleep(1)
