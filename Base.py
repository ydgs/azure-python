from selenium import webdriver

chrome_options = webdriver.ChromeOptions(); 
#chrome_options.add_argument("--headless")

chrome_options.add_argument("--disable-background-timer-throttling");
chrome_options.add_argument("--disable-backgrounding-occluded-windows");
chrome_options.add_argument("--disable-breakpad");
chrome_options.add_argument("--disable-component-extensions-with-background-pages");
chrome_options.add_argument("--disable-dev-shm-usage");
chrome_options.add_argument("--disable-extensions");
chrome_options.add_argument("--disable-features=TranslateUI,BlinkGenPropertyTrees");
chrome_options.add_argument("--disable-ipc-flooding-protection");
chrome_options.add_argument("--disable-renderer-backgrounding");
chrome_options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess");
chrome_options.add_argument("--force-color-profile=srgb");
chrome_options.add_argument("--hide-scrollbars");
chrome_options.add_argument("--metrics-recording-only");
chrome_options.add_argument("--mute-audio");
chrome_options.add_argument("--headless");
chrome_options.add_argument("--no-sandbox");

driver = webdriver.Chrome(options=chrome_options, executable_path='C:\\Packages\\Plugins\\Microsoft.CPlat.Core.RunCommandWindows\\1.1.9\\Downloads\\chromedriver.exe')

#from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://google.com/')