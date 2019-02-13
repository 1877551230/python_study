import urllib.request

respond = urllib.request.urlopen('http://rosi8.cc/picture/201605/rosi18833301529235.jpg')
cat_img = respond.read()
with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)
