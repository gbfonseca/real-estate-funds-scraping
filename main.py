import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = 'https://fundamentus.com.br/fii_resultado.php'


option = Options()
option.headless = False
driver = webdriver.Firefox(options=option)


def returnDYEqualOrBiggerFour(data_frame):
    data_frame['Dividend Yield'] = data_frame['Dividend Yield'].str.rstrip('%')
    data_frame['Dividend Yield'] = data_frame['Dividend Yield'].str.replace(
        ',', '.')
    data_frame['Dividend Yield'] = data_frame['Dividend Yield'].astype(
        float) / 100
    is_more_four_percent = data_frame['Dividend Yield'] >= 0.04
    df_full = data_frame[is_more_four_percent]
    data_frame['Dividend Yield'] = data_frame['Dividend Yield'].astype(str)
    data_frame['Dividend Yield'] = data_frame['Dividend Yield'].str.replace(
        '.', ',')
    return data_frame


def get_rs():
    driver.get(url)

    element = driver.find_element_by_xpath(
        "//div[@class='conteudo clearfix']//table")

    html_content = element.get_attribute("outerHTML")

    soup = BeautifulSoup(html_content, "html.parser")

    table = soup.find(name="table")

    df_full = pd.read_html(str(table), index_col=0)[0]
    df_full = returnDYEqualOrBiggerFour(df_full)

    return df_full.to_csv('brazil-real-estates-sheets.csv')


get_rs()
driver.quit()
