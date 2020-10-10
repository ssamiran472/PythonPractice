from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# driver = webdriver.Chrome()

# driver.get("https://www.freelancer.com")
# # driver.find_element_by_id("searchField")
# frame = driver.find_element_by_xpath('//*[@id="searchField"]')
# driver.switch_to.frame(frame)
# # frame.send_keys("Movies")
# pass1 = driver.find_element_by_id("searchField")
# pass1.send_keys("Movies")
# login = driver.find_element_by_xpath(
#     "/html/body/app-root/app-logged-out-shell/app-navigation/app-navigation-logged-out/fl-bit/fl-container/fl-bit/fl-link[1]/a")
# login.click()


class automation:
    def __init__(self, link):
        self.link = link
        self.driver = webdriver.Chrome()

    def freelancer(self):
        self.driver.get(self.link)
        delay = 3  # seconds
        try:
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/app-root/app-logged-out-shell/app-navigation/app-navigation-logged-out/fl-bit/fl-container/fl-bit/fl-link[1]/a')))
            myElem.click()
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        try:
            click_username = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/app-root/app-logged-out-shell/app-login-page/fl-page-layout/main/fl-container/fl-page-layout-single/app-login/fl-card/fl-bit/fl-bit/app-credentials-form/form/fl-input[1]/fl-bit/fl-bit/input')))
            click_username.send_keys("samiransarkar513@gmail.com")
            print("username clicked")
            password = self.driver.find_element_by_xpath(
                "/html/body/app-root/app-logged-out-shell/app-login-page/fl-page-layout/main/fl-container/fl-page-layout-single/app-login/fl-card/fl-bit/fl-bit/app-credentials-form/form/fl-input[2]/fl-bit/fl-bit/input")
            password.send_keys("Samiran@12")

            self.driver.find_element_by_xpath(
                "/html/body/app-root/app-logged-out-shell/app-login-page/fl-page-layout/main/fl-container/fl-page-layout-single/app-login/fl-card/fl-bit/fl-bit/app-credentials-form/form/app-login-signup-button/fl-button/button").click()
        except TimeoutException:
            print("time out when login page loded.")

        try:
            search_box = "/html/body/div[2]/main/section/fl-search/div/div[2]/div/fl-header-filter/div/div[1]/form/input"
            brows_button = "/html/body/app-root/app-logged-in-shell/div/div[1]/app-navigation/app-navigation-primary/fl-bit/fl-container/fl-callout[1]/fl-callout-trigger/fl-button/button"
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, brows_button))).click()
            self.driver.find_element_by_xpath(search_box).send_keys("Django")

        except:
            print(" timeout on dashboard page.")

        print("automation complete.")


freelance = automation("https://freelancer.com")
freelance.freelancer()
