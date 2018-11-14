from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import scrapy
from random import *

escreve = open('enderecos_novo.txt', 'w')

chrome_options = Options()
chrome_options.add_argument("--headless")
#driver = webdriver.Chrome("chromedriver.exe")
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
driver.get('https://www.geradordecep.com.br/')


i = 0;
for i in range(75):
	menu_estados = driver.find_element_by_xpath("""//*[@id="campoEstado"]""");
	menu_estados.send_keys("São Paulo")

	gera_cep = driver.find_element_by_xpath("""/html/body/div[3]/section[1]/div/div/div/div[3]/form/div[2]/div/div/div/div[2]/button""")
	gera_cep.click()

	rua = driver.find_element_by_xpath("""/html/body/div[3]/section[1]/div/div/div/div[3]/div[1]/div/span[1]""")
	cep = driver.find_element_by_xpath("""//input[@type="search"][@value]""").get_attribute("value")
	bairro = driver.find_element_by_xpath("""/html/body/div[3]/section[1]/div/div/div/div[3]/div[1]/div/span[2]""")

	texto = rua.text + " , " + str(randrange(0, 10000)) + " , " + cep + " , " + bairro.text
	escreve.write(rua.text + " , " + str(randrange(0, 10000)) + " , " + cep + " , " + bairro.text + "\n")

	print(texto)

