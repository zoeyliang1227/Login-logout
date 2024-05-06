import yaml
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

config = yaml.load(open('earnaha.yml'), Loader=yaml.Loader)

timeout = 20

def get_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')                 # 瀏覽器不提供可視化頁面
    options.add_argument('-no-sandbox')               # 以最高權限運行
    options.add_argument('--start-maximized')        # 縮放縮放（全屏窗口）設置元素比較準確
    options.add_argument('--disable-gpu')            # 谷歌文檔說明需要加上這個屬性來規避bug
    options.add_argument('--window-size=1920,1080')  # 設置瀏覽器按鈕（窗口大小）
    options.add_argument('--incognito')               # 啟動無痕

    driver = webdriver.Chrome(options=options)
    url = config['url']

    # driver.implicitly_wait(10)
    # driver.get(url)
    # driver.delete_all_cookies() #清cookie
    
    # with open("cookies.yml", "r") as f:
    #     cookies = yaml.safe_load(f)
    #     for c in cookies:
    #         if 'domain' in c:
    #             c['domain'] = 'xxx'
    #         dev_logger.info(c)
    #         driver.add_cookie(c)

    driver.get(url)
    

    return driver

def main():
    start = time.time()
    driver = get_driver()
    login(driver)

def login(driver):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/aside/a'))).click() 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(config['username']) 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(config['password']) 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/section/div/div/div/form/div[2]/button'))).click()  
    
    check_login(driver)
    driver.get(driver.current_url+'/profile/account')
    calender(driver)
    # signout(driver)
    
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/section/div/div/div/div[3]/form[1]/button/span[2]'))).click() 
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'identifierId'))).send_keys(config['o_username']) 
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))).click()
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.NAME, 'Passwd'))).send_keys(config['o_password'])
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))).click()
    
    # signout(driver)
    
    # cookie2 = driver.get_cookies() #取得登入後cookie
    # with open("cookies.yml", "w") as f:
    #     yaml.safe_dump(data=cookie2, stream=f)
    
def check_img(driver):
    img = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/button/div/div/div/div/img')))
    if img:
        return True
    else:
        return False
    
def check_login(driver):
    time.sleep(3)
    if check_img(driver) and driver.current_url == 'https://app.earnaha.com/':
        print('success')
    else:
        print('failure')
        
def signout(driver):
    time.sleep(3)
    
    actions = ActionChains(driver)
    ele = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]')
    cl = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/button')
    time.sleep(2)
    # js = 'document.getElementsByClassName("scroll")[0].scrollTop=10000' 
    # driver.execute_script(js)
    actions.move_to_element(ele).click(cl).perform()  
    
    c = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div').find_elements(By.CLASS_NAME, 'MuiBox-root css-1rmp3tn')
    print(len(c))
    for i in c :
        print(i.text)

    # actions = ActionChains(driver)
    # ele2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/button')
    # actions.move_to_element(ele2).click(ele2).perform()
    # # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/button/div/div/svg'))).click() 
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/button/div/div'))).click() 
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/button'))).click() 
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/a[2]/div'))).click()

def calender(driver):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/div[4]/a/div'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[1]/div/div[4]/div[1]'))).click()
    cal = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]'))).find_elements(By.TAG_NAME, 'div')
    print(len(cal))
    # for i in cal:
    #     z = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[' + str(i) +']/div/button')))
    #     print(z.get_attribute('tabindex'))
        
    # z = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/button')))
    # print(z.get_attribute('tabindex'))
    # z.click()
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]'))).click()
    
    # /html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[2]
    # /html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[3]

if __name__ == '__main__':
    main()