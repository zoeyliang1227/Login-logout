import yaml
import time
import logger

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = yaml.load(open('earnaha.yml'), Loader=yaml.Loader)
dev_logger = logger.get_logger(__name__)

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

    driver.get(url)
    

    return driver

def main():
    driver = get_driver()
    login(driver)

def login(driver):
    #success
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/aside/a'))).click() 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(config['s_username']) 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(config['s_password']) 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/section/div/div/div/form/div[2]/button'))).click()  
    
    time.sleep(1)
    check_login(driver)
    driver.get(driver.current_url+'/profile/account')
    time.sleep(1)
    calender(driver)
    signout(driver)
    
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/a[2]/div'))).click() 
    
    #fail
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(config['f_username']) 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(config['f_password']) 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/section/div/div/div/form/div[2]/button'))).click() 
    
    check_login(driver)
    
    #oauth
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/section/div/div/div/div[3]/form[1]/button/span[2]'))).click() 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'identifierId'))).send_keys(config['o_username']) 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.NAME, 'Passwd'))).send_keys(config['o_password'])
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))).click()

    
def check_img(driver):
    try:
        if driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/button/div/div/div/div/img'):
            return True
    except:
        return False
    
def check_error(driver):
    try:
        if driver.find_element(By.ID, 'error-element-password').text == 'Wrong email or password':
            return True
    except:
        return False
    
def check_login(driver):
    dev_logger.info('check login')
    if check_error(driver):
        dev_logger.info('failure')
    
    elif check_img(driver) and driver.current_url == 'https://app.earnaha.com/':
        dev_logger.info('success')
        
    else:
        dev_logger.info('There is something wrong')
        
            
    
        
def signout(driver):    
    dev_logger.info('signout')
    time.sleep(2)
    actions = ActionChains(driver)
    ele = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]')
    cl = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/button')
    actions.move_to_element(ele).click(cl).perform()  
    
    dev_logger.info('logout')
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/button'))).click() 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div/div/div[2]/div[2]/button'))).click() 

def calender(driver):
    dev_logger.info('calender')
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/div[4]/a/div'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[1]/div/div[4]/div[1]'))).click()
    cal = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div'))).find_elements(By.CLASS_NAME, 'css-1rmp3tn')
    a = 0 
    for w, we in enumerate(cal, start=1):
        week = we.find_elements(By.CLASS_NAME, 'css-ltumv2')
        for i in range(len(week)):
            z = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[' + str(w+1) +']/div[' + str(i+1) +']/div/button')))
            if z.text == str(datetime.now().day) and z.get_attribute('tabindex') == '0':
                z.click()
                a+=1
                break
        if a != 0:
            break
        
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[3]/div/button/div'))).click()
    
if __name__ == '__main__':
    main()