from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

random_num = 0 #random.randint(1,5)

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_argument("--start-maximized");
chrome_options.add_argument("--headless")
chrome_options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36""')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com/')

search_terms = [
    {
        "Subject": "Camping Tents",
        "Query": "The best Coleman Camping tents (Part 1)",
        "navbar_dropdown": "//*[@id='menu-item-8696']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7456']",
        "page_link": "https://allcamping-gears.com/camping-tents/",
        "first_related_blog_items": "//*[@id='post-4358']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a[1]",
        "second_related_blog_items": "//*[@id='post-4358']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    },
    {
        "Subject": "Camping Hammocks",
        "Query": "camping hammocks allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8696']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7457']/a",
        "page_link": "https://allcamping-gears.com/camping-hammocks/",
        "first_related_blog_items": "//*[@id='post-5281']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a",
        "second_related_blog_items": "//*[@id='post-5281']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    },
    {
        "Subject": "Camping Backpacks",
        "Query": "camping backpacks allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8692']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7459']/a",
        "page_link": "https://allcamping-gears.com/camping-backpacks/",
        "first_related_blog_items": "//*[@id='post-5954']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a",
        "second_related_blog_items": "//*[@id='post-5954']/div/div/div/section/div/div/div/section/div/div[3]/div/div[4]/div/p/a"
    },
    {
        "Subject": "Camping Stoves",
        "Query": "camping stoves allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8697']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7461']/a",
        "page_link": "https://allcamping-gears.com/camping-stoves/",
        "first_related_blog_items": "//*[@id='post-6179']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a",
        "second_related_blog_items": "//*[@id='post-6179']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    },
    {
        "Subject": "Camping Tables",
        "Query": "camping tables allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8698']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7463']/a",
        "page_link": "https://allcamping-gears.com/camping-tables-and-chairs/",
        "first_related_blog_items": "//*[@id='post-6310']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a",
        "second_related_blog_items": "//*[@id='post-6310']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    },
    {
        "Subject": "Camping Shower Tents",
        "Query": "camping shower tents allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8698']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7462']/a",
        "page_link": "https://allcamping-gears.com/camping-shower-tents/",
        "first_related_blog_items": "//*[@id='post-6312']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a",
        "second_related_blog_items": "//*[@id='post-6312']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    }
]

search_box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_box.send_keys(f"{search_terms[random_num]['Query']}")
search_box.submit()

website_address = "allcamping-gears.com"


all_results = driver.find_elements_by_class_name("iUh30")

next_result = driver.find_element_by_id("pnnext").get_attribute('href')

print(next_result)

CPG_website = ""

# for website in all_results:
#     if (website.text == "https://allcamping-gears.com"):
#         CPG_website = website;

result_count = 10
start_word = ""
start_index = 0
next_result_page = ""

#while not ("https://allcamping-gears.com") in next_result_page:
while ("https://allcamping-gears.com" not in next_result_page):
    all_results = driver.find_elements_by_class_name("iUh30")

    for website in all_results:
        print(website.text)

        if (website.text == "https://allcamping-gears.com"):
            CPG_website = website;


    print(result_count)

    if result_count < 210:
        print("Entered")

        splitted = next_result.split("&")

        for index, parts in enumerate(splitted):
            if ("start" in parts):
                start_index = index
        
        start_word = "start" + "=" + str(result_count)

        splitted[start_index] = start_word

        next_result_page = '&'.join(splitted)

    driver.get(next_result_page)

    result_count = result_count + 10
    print(result_count)

print("Python tasks completed successfully")
