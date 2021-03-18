from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


def login(login_driver, email, password):
    """
    :param login_driver:
    :param email:
    :param password:
    :return:
    """
    login_driver.get('https://www.instagram.com/')  # instagram url

    username = WebDriverWait(login_driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="username"]')))
    username.clear()
    username.send_keys(email)  # user insertion in 'user' element

    passwd = WebDriverWait(login_driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))  # 'password 'input element
    passwd.clear()
    passwd.send_keys(password)  # password insertion in 'password' element

    passwd.send_keys(Keys.RETURN)  # log in to page

    return driver


def watch_story(driver_story, target_user):
    """
    :param target_user:
    :param driver_story:
    :param profile_url:
    """
    driver_story.get("https://www.instagram.com/stories/" + target_user + "/")

    # /html/body/div[1]/section/div[1]/div/section/div/div[1]/div/div/div/div[3]/button
    click_watch = '''//*[@id="react-root"]/section/div[1]/div/section/div/div[1]/div/div/div/div[3]/button'''
    story_element = WebDriverWait(driver_story, 20).until(
        EC.presence_of_element_located((By.XPATH, click_watch)))
    story_element.click()
    sleep(60)


if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path="geckodriver.exe")
    driver = login(driver, email="jscomsats@gmail.com", password="instashaam")
    print("login success")
    sleep(10)

    user_list = ["_tarance_"]
    for each_user in user_list:
        try:
            watch_story(driver, target_user=each_user)
        except:
            print("watch error", each_user)
