import urllib2
import urllib
import os
from bs4 import BeautifulSoup

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent }
def getData(url):
    try:
        req = urllib2.Request(url,None, headers)
        respone = urllib2.urlopen(req)
        return respone.read()
    except urllib2.URLError,e:
        print e.reason



def getImageList(page):
    url = 'http://jandan.net/ooxx/'
    url = url + 'page-' + str(page) + '#comments'

    html = getData(url)
    try:
        soup = BeautifulSoup(html)
    except TypeError:
        return []

    imgs = soup.find_all('img')
    image_list = []
    for img in imgs:
        src = ''
        if img.has_attr('org_src'):
            src =img['org_src']
        else:
            src = img['src']
        if src.find('sinaimg') != -1:
            image_list.append(src)
    return image_list


def saveImage(url, filename):
    image = getData(url)
    f = file('./image/' + filename,'wb')
    f.write(image)
    f.close()


def sprider():
    path = os.path.dirname(__file__)
    path = path + '/image'
    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(900,1700):
        imagelist = getImageList(i)
        idx = 0
        for url in imagelist:
            print 'get page:' + str(i) + '->' + str(idx) + ":" + url
            saveImage(url, url.split('/')[-1])
            idx = idx + 1
    
if __name__ == "__main__":
    sprider()
    
