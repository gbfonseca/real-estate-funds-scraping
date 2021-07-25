import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from filters.filterDY import filterDY
from filters.filterPVP import filterPVP

url = 'https://fundamentus.com.br/fii_resultado.php'


option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)


def get_rs():
    driver.get(url)

    element = driver.find_element_by_xpath(
        "//div[@class='conteudo clearfix']//table")

    html_content = element.get_attribute("outerHTML")

    soup = BeautifulSoup(html_content, "html.parser")

    table = soup.find(name="table")

    df_full = pd.read_html(str(table), index_col=0)[0]
    df_full = filterDY(df_full)
    df_full = filterPVP(df_full)
    return df_full.to_csv('brazil-real-estates-sheets.csv')


get_rs()
driver.quit()
