# importing all required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# defining the path of your selenium web-driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# using web-driver initiate a call to the website
url = "https://fortune.com/fortune500/2020/search/?sector=Retailing"
# u can try on other fortune 500 websites also
# url = "https://fortune.com/fortune500/2020/search/?sector=Technology"
driver.get(url)

# add a 10 sec wait for the page to completely load
driver.implicitly_wait(10)

# declaring an empty list and dictionary
data = []
d = {}

# declare a variable to get the total number of pages in the website
L_page = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/div/div[2]/div/div[2]/span[1]/span')
L_page = int(L_page.text)
time.sleep(2)

# Extracting the row wise data
for n in range(1, L_page + 1):
    for i in range(1, 11):
        _i = str(i)
        # get the xpath for each field and customize it to get updated for each row
        try:
            name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                   '//*[@id="content"]/div[3]/div[2]/div/div[1]/div[2]/div[' + _i + ']/div/div[2]/a/div/span/div')))
            revenue = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '//*[@id="content"]/div[3]/div[2]/div/div[1]/div[2]/div[' + _i + ']/div/div[3]/a/div/span')))
            revenue_percentage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                                 '//*[@id="content"]/div[3]/div[2]/div/div[1]/div[2]/div[' + _i + ']/div/div[4]/a/div/span')))
            profit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                     '//*[@id="content"]/div[3]/div[2]/div/div[1]/div[2]/div[' + _i + ']/div/div[5]/a/div/span')))
            profit_percentage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                                '//*[@id="content"]/div[3]/div[2]/div/div[1]/div[2]/div[' + _i + ']/div/div[6]/a/div/span')))
            assets = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                     '//*[@id="content"]/div[3]/div[2]/div/div[1]/div[2]/div[' + _i + ']/div/div[7]/a/div/span')))
            market_Value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                           '//*[@id="content"]/div[3]/div[2]/div/div[1]/div[2]/div[' + _i + ']/div/div[8]/a/div/span')))
            employees = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '//*[@id="content"]/div[3]/div[2]/div/div[1]/div[2]/div[' + _i + ']/div/div[10]/a/div/span')))
            d['Name'] = name.text
            d['Revenue $ million'] = revenue.text
            d['Revenue % change'] = revenue_percentage.text
            d['Profits $ million'] = profit.text
            d['Profit % change'] = profit_percentage.text
            d['Assets $ million'] = assets.text
            d['Market value (03-2020) $M'] = market_Value.text
            d['Number of employees'] = employees.text
            data.append(d.copy())
        # if there are less than 10 elements in the row then exit the loop, because this can happen at the last page only
        except:
            break
    # go to next page after getting the required data from current page
    next_btn = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/div/div[2]/div/div[3]/button')
    driver.execute_script("arguments[0].click();", next_btn)
    # wait for 1 sec to load, change it if you have very slow network
    time.sleep(1)

# our data is collected, print the list of dictionary and close the website
print(data)
driver.close()
