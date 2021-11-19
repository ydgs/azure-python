from selenium import webdriver

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options, executable_path='C:\\Packages\\Plugins\\Microsoft.CPlat.Core.RunCommandWindows\\1.1.9\\Downloads\\chromedriver.exe')

#from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://google.com/')