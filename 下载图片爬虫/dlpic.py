import re,urllib.request,string
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    #print(html)
    return html

def get_page(url):
    html = url_open(url)
    return '2797'
	
   # a = html.find('current-comment-page') + 23
   # b = html.find(']',a)
    # return html[a:b]
	
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    
    reg = "img src='(.*?)'"
    imgre = re.compile(reg)
    img_addrs = re.findall(imgre,html)

    '''
    a = html.find('img src=')
	
    if a != -1:
        
        b = html.find('.jpg', a)
        if b != -1:
            
            img_addrs.append(html[a+9:b+4])
            
        else
        b = a + 9
            a = html.find('img src=', b)
    '''
    
    #for each in img_addrs:
     #   print(each)

    return img_addrs
def real_url(img_addrs):
    img_url = []
    for each in img_addrs:
        img_url.append('http://rosi8.cc' + each)
    return img_url
    
def save_imgs(folder,img_url):
    for each in img_url:
        i = 0
        
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
            i+=1
            print('成功绘制')
           
            

def download_mm(folder='ooxx',pages=10):
    
    #os.mkdir(folder)
    #os.chdir(folder)
	
    url = 'http://rosi8.cc/rosixiezhen/'
    page_num = int(get_page(url))
    
    for i in range(0,10):
        page_num -= 1
        print(str(page_num))
        for n in range(2,6):
            
            page_url = url  + '20160530/' + str(page_num) + '_' + str(n) + '.html' 
            print(page_url)
            img_addrs = find_imgs(page_url)
            img_url = real_url(img_addrs)
            save_imgs(folder,img_url)
            
            
if __name__ == '__main__':
	download_mm()

