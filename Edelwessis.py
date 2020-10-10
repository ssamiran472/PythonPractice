import time
import xlsxwriter
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


STOCK_NAME_LIST = []
DATE_LIST = []
LIST_OF_TH = []
values = []

def selenium_scraping(url):
    
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_link_text('Show all').click()
    time.sleep(5)
    page = driver.page_source

    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')
    # stockName = list(soup.find_all('a', class_='ng-binding'))
    # for a in stockName:
    #     print(a.text)
    # stockName_list = [a.text for a in stockName[0:2]]
    # date_list = [a.text for a in stockName[3:13]]
    # print("sock list is 1 ===>>>>", stockName_list)
    # print("date list is 2 ===>>>>", date_list)
    return soup


def scraping_start():
    url = "https://www.edelweiss.in/market/nse-option-chain"
    soup = selenium_scraping(url)
    stockName = list(soup.find_all('a', class_='ng-binding'))
    # for a in stockName:
    #     print(a.text)
    STOCK_NAME_LIST = [a.text for a in stockName[0:2]]
    DATE_LIST = [a.text for a in stockName[3:13]]
    print("sock list is ===>>>>", STOCK_NAME_LIST)
    print("date list is ===>>>>", DATE_LIST)
    table_div = soup.find_all('table', class_='table ed')[0]
    
    table_div= table_div.find_all('tr')[1]
    for th in table_div.find_all('th'):
        LIST_OF_TH.append(th.text)
    
    print(LIST_OF_TH)
    table_divs = soup.find_all('table', class_='table ed')[1]
    # print('table divs',table_divs)
    stock_val_table =table_divs.find_all('tr')
    i = 0
    for tr in stock_val_table:
        i += 1
        val = []
        for td in tr.find_all('td'):
            val.append(td.text)
            # print(td.text)
        
        values.append(val)
    print(values)
scraping_start()

workbook = xlsxwriter.Workbook('hello.xlsx') 
worksheet = workbook.add_worksheet()
worksheet.write('D1', 'CALL') 
worksheet.write('L1', 'PUT')
row = 1
col = 0
for item in LIST_OF_TH:
    worksheet.write(row, col, item)
    col += 1

for items in values:
    col=0
    row += 1
    for item in items:
        worksheet.write(row, col, item)
        col +=1

# worksheet.write('A1', LIST_OF_TH[0])
# worksheet.write('B1', LIST_OF_TH[1])
# worksheet.write('C1', LIST_OF_TH[2])
# worksheet.write('D1', LIST_OF_TH[3])
# worksheet.write('E1', LIST_OF_TH[4])
# worksheet.write('F1', LIST_OF_TH[5])
# worksheet.write('G1', LIST_OF_TH[6])
# worksheet.write('H1', LIST_OF_TH[7])
# worksheet.write('I1', LIST_OF_TH[8])
# worksheet.write('J1', LIST_OF_TH[9])
# worksheet.write('K1', LIST_OF_TH[10])
# worksheet.write('L1', LIST_OF_TH[11])
# worksheet.write('M1', LIST_OF_TH[12])
# worksheet.write('N1', LIST_OF_TH[13])
# worksheet.write('O1', LIST_OF_TH[14])
# worksheet.write('P1', LIST_OF_TH[15])
workbook.close() 
print('done')

