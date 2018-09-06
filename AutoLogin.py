from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Scripts\chromedriver.exe')
driver.get("http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&")
assert "IP控制网关" in driver.title
element = driver.find_element_by_name("username")
element.clear
element.send_keys("20173894")
element = driver.find_element_by_name("password")
element.clear
element.send_keys("981006")
element.submit()
assert "网络已连接" in driver.page_source
driver.close()
