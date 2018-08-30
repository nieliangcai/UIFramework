from selenium.webdriver.common.by import By


topic_loc = (By.XPATH,'//*[@id="create_topic_btn"]')            #发布主题
select_loc = (By.XPATH,'//*[@id="tab-value"]')                  #选择模块
title_loc = (By.XPATH,'//*[@id="title"]')                       #主题
content_loc = (By.XPATH,'//*[@class="CodeMirror cm-s-paper"]')  #发布内容
submit_loc  = (By.CSS_SELECTOR,'.span-primary')                 #提交