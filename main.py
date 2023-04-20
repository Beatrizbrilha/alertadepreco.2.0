import time
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get(
    "https://www.amazon.com.br/dp/B09TMK7QFX?ref=ods_erd_dpcc_ttl_ppw_nrc_ucc")

time.sleep(3)

preco_element = navegador.find_element('xpath','//*[@id="corePrice_feature_div"]/div/span[1]/span[2]/span[2]')
preco = float(preco_element.text.replace(',', '.'))

if preco < 880.0:
    msg = MIMEText(f"O preço do produto está abaixo de R$ 880,00! O preço atual é: R$ {preco:.2f}")
    msg['Subject'] = 'Alerta de preço na Amazon'
    msg['From'] = 'seuemail@gmail.com'
    msg['To'] = 'emaildodestinatario@gmail.com'



    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login('seuemail@gmail.com', 'suasenhadeapp')
    smtp_server.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp_server.quit()

time.sleep(10)
navegador.quit()
