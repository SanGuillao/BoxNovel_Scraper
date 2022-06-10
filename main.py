from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#object of Options class
c = Options()
#passing headless parameter
c.add_argument("--headless")
c.add_argument("--log-level=3")

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver", options=c)
#driver = webdriver.Chrome("chromedriver")

# head over to boxnovel
driver.get("https://boxnovel.com/novel/top-tier-providence-secretly-cultivate-for-a-thousand-years/")

# wait for the element of most recent to load
elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='manga-chapters-holder']/div[2]/div/ul/li[1]")))

# find what the most recent chapter is
recent = driver.find_element(By.XPATH, "//*[@id='manga-chapters-holder']/div[2]/div/ul/li[1]").text

temp_list = recent.split()
for itr in temp_list:
    if itr.isnumeric():
        newest = int(itr)

#print(newest)

for counter in range(1, 30):
    chapter = '%01d' % counter
    #print(chapter)
    str = "https://boxnovel.com/novel/top-tier-providence-secretly-cultivate-for-a-thousand-years/chapter-" + chapter
    
    driver.get(str)
    
    body = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]").text
    
    file_path = "Chapters\ch" + '%02d' % int(chapter) + ".txt"
    with open(file_path, 'w') as f:
        for line in body:
            f.write(line)
            
    f.close()
    
    print(f"Completed output to {file_path}")

# close the driver
driver.close()
