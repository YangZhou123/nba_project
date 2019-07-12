from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import collections
import time
import csv
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://stats.nba.com/player/202695/boxscores-traditional/?sort=gdate&dir=1')

table0 = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table/div[2]/div[1]/table')
print(table0.text)
with open('data0.txt', 'w') as f:
    f.write(table0.text)

button = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table/div[3]/div/div/a[2]/i')
button.click()

table1 = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table/div[2]/div[1]/table')
print(table0.text)
with open('data1.txt', 'w') as f:
    f.write(table1.text)