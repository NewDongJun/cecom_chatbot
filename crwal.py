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
print(recent_notice_url)
print()



#table = form.find("table",{"class":"table-basic"})
print(type(section))
print(type(section.form))








#print(type(page_body))
#print(page_body)



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
