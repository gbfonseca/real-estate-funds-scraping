import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = 'https://fundamentus.com.br/fii_resultado.php'


option = Options()
option.headless = False
driver = webdriver.Firefox(options=option)


def get_rs():
    driver.get(url)

    element = driver.find_element_by_xpath(
        "//div[@class='conteudo clearfix']//table")

    html_content = element.get_attribute("outerHTML")

    soup = BeautifulSoup(html_content, "html.parser")

    table = soup.find(name="table")

    df_full = pd.read_html(str(table), index_col=0)[0]

    return df_full.to_csv('Planilha.csv')


get_rs()
driver.quit()
