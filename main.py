import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = 'https://fundamentus.com.br/fii_resultado.php'


def get_rs():
    driver.get(url)

    # time.sleep(20)

    element = driver.find_element_by_xpath(
        "//div[@class='conteudo clearfix']//table")

    html_content = element.get_attribute("outerHTML")

    soup = BeautifulSoup(html_content, "html.parser")

    table = soup.find(name="table")

    df_full = pd.read_html(str(table))[0]

    return df_full.to_csv()


option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

rs = get_rs()
fp = open('Planilha_FIIs.csv', 'w')
fp.write(rs)
fp.close()
driver.quit()
