import urllib.request as ur
#import urllib.parse as up
from bs4 import BeautifulSoup


#html = ur.urlopen("http://www.naver.com")
#bsobject = BeautifulSoup(html,"html.parser")
#
#print(bsobject.head.title)
#print()

#-----------------------------


notice_page = ur.urlopen("https://cse.cau.ac.kr/sub05/sub0501.php")
target_page = BeautifulSoup(notice_page,"html.parser")  #type은 bs4.BeautifulSoup

page_body = target_page.find("section",{"id":"middle"})
div = page_body.div
section = div.find("section",{"id":"content"})
print(section.div.h2)
print()

form = section.find("form",{"id":"listpage_form"})
tbody = form.table.tbody
recent_notice = tbody.tr
recent_notice_url = recent_notice.find("td",{"class":"aleft"})
#print(recent_notice_url)
#print("----------------------------------------")
#
#print(recent_notice_url.a)
#print("----------------------------------------")
#


page_number = str(recent_notice_url.a)[65:69]
notice_title = str(recent_notice_url.a)[139:-12]
print(notice_title)
print("-----------------------------------------")
#print(page_number)

complete_url = "https://cse.cau.ac.kr/sub05/sub0501.php" + "?dir=bbs&nmode=view&code=oktomato_bbs05&uid=" + page_number + "&search=&keyword=&temp1=&offset=1"
print(complete_url)




#
# data = bsobject.head
#
# data.find()
#
# #print(bsobject.body.find("section", {"id":"middle"}))
#

#
# print(data)
#print(type(data))
