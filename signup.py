import random
import time
import yaml

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


config = yaml.load(open('earnaha.yml'), Loader=yaml.Loader)

timeout = 10
email_list = []
password_list = []
birthday_list = ['1','9','9']

new_email = ''

def main():
    print(email_random(email_list))
    print(pwd_random(password_list))
    print(birthday_random(birthday_list), birthday_list[3])

def signup(driver):
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/a[2]/div'))).click()     #login
    # # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/a[1]/div'))).click()       #signup
    # # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys(config['c_username']) 
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(config['c_username']) 
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(config['c_password']) 
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/section/div/div/div/form/div[2]/button'))).click()
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/section/div/div/div/form/div[3]/button'))).click()
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/div[5]/div[3]/button'))).click()
    
    # driver.execute_script("window.open('');")
    # driver.switch_to.window(driver.window_handles[1]) 
    
    # get href from gmail
    driver.get('https://mail.google.com/mail/u/0/#inbox')
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'identifierId'))).send_keys(config['c_username']) 
    time.sleep(2)
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.NAME, 'Passwd'))).send_keys(config['c_password'])
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))).click()
    
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id=":1"]/div/div/div[8]'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id=":1"]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]'))).click()
    c = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id=":1"]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]'))).find_elements(By.TAG_NAME, 'a')
    
    
    #signup for oauth
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/a[1]/div'))).click()
    # driver.execute_script("window.open('');")
    # driver.switch_to.window(driver.window_handles[1]) 
    # driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AaSxoQwVL-19Y5LLIGyWFlWWo30oCHSOmdyrUQgn0tAd-yWZoV_pzFkX5y6kunRmwRbXeSPgcMqYGQ&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1694779515%3A1715072123694556&theme=mn&ddm=0')
    
    # create_google(driver)
    
    # driver.switch_to.window(driver.window_handles[0])
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'email'))).send_keys(new_email+'@gmail.com') 
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(pwd_random(password_list))
    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/section/div/div/div/form/div[3]/button'))).click() 
    
    driver.get(driver.current_url+'/profile/account')
            
def create_google(driver):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button/span'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]/span[3]'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.NAME, 'firstName'))).send_keys(email_random(email_list))
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="collectNameNext"]/div/button/span'))).click()
    
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'year'))).send_keys(birthday_random(birthday_list))
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'month'))).send_keys(birthday_list[3])
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'day'))).send_keys(birthday_list[3])
    select = Select(driver.find_element(By.ID, 'gender'))
    select.select_by_index(2)
    
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthdaygenderNext"]/div/button/span'))).click()
    email = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'selectionc2')))
    new_email = email.text
    email.click()
    
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="next"]/div/button/span'))).click()
    
    pwd = pwd_random(password_list)
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.NAME, 'Passwd'))).send_keys(pwd) 
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.NAME, 'PasswdAgain'))).send_keys(pwd) 
    
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="createpasswordNext"]/div/button/span'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/button/div[3]'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="next"]/div/button/span'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]'))).click()
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gb"]/div[2]/div[3]/div[1]/div[2]/div/a'))).click()


def email_random(email_list):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for number in range(1, 5):
        email_list += random.choice(numbers)
    for letter in range(1, 5):
        email_list += random.choice(letters)
        
    random.shuffle(email_list)
    email = ""
    for email_char in email_list:
        email += email_char
        
    return email
    
def pwd_random(password_list):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for number in range(1, 4):
        password_list += random.choice(numbers)
    for symbol in range(1, 4):
        password_list += random.choice(symbols)
    for letter in range(1, 4):
        password_list += random.choice(letters)
        
    random.shuffle(password_list)
    password = ""
    for password_char in password_list:
        password += password_char
        
    return password


def birthday_random(birthday_list):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    birthday_list += random.choice(numbers)
        
    birthday = ""
    for birthday_char in birthday_list:
        birthday += birthday_char
        
    return birthday
        

if __name__ == '__main__':
    main()
    
# V803My6s@gmail.com
# 8~J72!U~sfor i, te in enumerate(c):
        if 'https' in te.text:
            print(i, te.text, te.get_attribute('href'))