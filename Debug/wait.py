from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
element = WebDriverWait(driver,3,0.5).until(EC.alert_is_present)#(EC.presence_of_element_located((By.ID,'kw')))
print(element)


current_handler = driver.current_window_handle
all_handlers = driver.window_handles
for handler in all_handlers:
    if handler != current_handler:
        driver.switch_to.window(handler)
    driver.switch_to.default_content()