from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from os import listdir
from os import mkdir
from argparse import ArgumentParser
from create_pdf import CreatePDF

# object for argument passing
parser = ArgumentParser()
parser.add_argument("URL")

arg = parser.parse_args()
url = arg.URL

#object of Options class
c = Options()
#passing headless parameter
c.add_argument("--headless") # run without gui
c.add_argument("--log-level=3") # suppress the log messages from ping

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver", options=c)
#driver = webdriver.Chrome("chromedriver")

# head over to boxnovel
#driver.get("https://boxnovel.com/novel/top-tier-providence-secretly-cultivate-for-a-thousand-years/")
driver.get(url)

# wait for the element of most recent to load
elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='manga-chapters-holder']/div[2]/div/ul/li[1]/a")))

# find the title of the series
series = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[2]/h1").text

# find what the most recent chapter is
recent = driver.find_element(By.XPATH, "//*[@id='manga-chapters-holder']/div[2]/div/ul/li[1]/a").text

newest = 1
temp_list = recent.split()
for itr in temp_list:
    if itr.isnumeric():
        newest = int(itr)

#print(newest)

# grab all the names of the files in the chapters folder
# compare what chapters are already there to new ones
dir_list = []
previous = 1

try:
    dir_list = listdir(series + "\\")
except:
    pass
    
for itr in dir_list:
    temp_list = itr.split('.')
    for titr in temp_list:
        if titr.isnumeric() and int(titr) > previous:
            previous = int(titr)
        
#print(previous)


for counter in range(previous, newest+1):
    chapter = '%01d' % counter
    str = url
    #print(chapter)
    #str = "https://boxnovel.com/novel/top-tier-providence-secretly-cultivate-for-a-thousand-years/chapter-" + chapter
    
    str += "chapter-" + chapter
    
    driver.get(str)
    
    body = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]").text
    
    try:
        mkdir(series)
    except:
        pass
    
    file_path = series + "\\" + '%02d' % int(chapter) + ".pdf"
    CreatePDF(file_path, body)
    
    print(f"Completed output to {file_path}")

# close the driver
driver.close()
