from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions() # stops driver from closing immediately
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.vlr.gg/295610/loud-vs-sentinels-champions-tour-2024-americas-kickoff-opening-b/?game=153737&tab=overview")

try: # Implicit Wait: make the webdriver wait a couple of seconds to load the page before we continue onto the rest of the code
    driver.implicitly_wait(1)

    # Scraping Team Names
    teamsElements = driver.find_elements(By.CLASS_NAME, value="wf-title-med")
    teams = []
    for team in teamsElements:
        teams.append(team.text)
    print(teams)
    
    

finally:
    driver.quit()






#-----EXAMPLE WEB SCRAPING ON NEWEGG FOR PRICE--------#

# url = "https://www.newegg.com/p/3D5-002P-00044?Item=3D5-002P-00044&cm_sp=Homepage_SS-_-P2_3D5-002P-00044-_-02192024"
# result = requests.get(url)

# doc = BeautifulSoup(result.text, "html.parser")

# prices = doc.find_all(text="$")
# parent = prices[0].parent
# strong = parent.find("strong")
# print(strong.string)

#----VALORANT STATS WEB SCRAPING TEST---------#

# use next_sibling, previous_sibling to traverse content siblings of the same family tree
# use next_siblings to give a generator object, then convert to list
# use .contents to find the contents of a certain element/tag
# use .descendants to show all elements/tags, need to convert to list
    # you can also use .children

# url = "https://www.vlr.gg/295610/loud-vs-sentinels-champions-tour-2024-americas-kickoff-opening-b"
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")

# # tbody = doc.find_all("tbody") # THIS IS TO FIND ALL THE TABLES IN THE PAGE

# tbody = soup.tbody
# trs = tbody.contents

# playerslist = tbody.find_all(['div'], class_="text-of")


# players = []

# for playerDiv in playerslist:
#     s = ''.join(filter(str.isalnum, playerDiv.text))
#     players.append(s)

# print(players)



    




        