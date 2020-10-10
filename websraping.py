import requests
from bs4 import BeautifulSoup

page = requests.get("https://forums.tomshardware.com/")

soup = BeautifulSoup(page.content, 'html.parser')
# lists = list(soup.find_all('a', class_='uix_categoryTitle'))
# category = [index.text for index in lists]
list_of_div = list(soup.find_all(
    'div', class_='block-container th_node--overwriteTextStyling'))
category_list = []
URL = 'https://forums.tomshardware.com'
for category in list_of_div:
    h2 = category.find_all("h2")
    print()
    # print("===================>>>>>>>>>", category)
    subcategorys = category.find_all("div", class_="node-main js-nodeMain")
    obj ={}
    subcategory_list = []
    for subcategory in subcategorys:
        sub_name = subcategory.h3.a.text
        link = subcategory.h3.a['href']
        link = URL + link
        obj = {
            'subcategory_name': sub_name,
            'link': link
        }
        subcategory_list.append(obj)
    category_link = URL + h2[0].div.a['href']
    category_obj ={
        'category_name': h2[0].div.a.text,
        'link': category_link,
        'subcat_list': subcategory_list
    }



    category_list.append(category_obj)

print(category_list)
# h2_list = subcategory.find_all("h2")
# for h2 in h2_list:
#     print(h2.text)
