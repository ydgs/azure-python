from selenium import webdriver

driver = webdriver.Chrome('C:\\Packages\\Plugins\\Microsoft.CPlat.Core.RunCommandWindows\\1.1.9\\Downloads\\chromedriver.exe')

#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://google.com/')