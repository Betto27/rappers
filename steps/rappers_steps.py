from behave import *
from selenium import webdriver
from nose.tools import assert_equal
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()


@given(u'que acesso o site')
def step_impl(context):
    driver.get("https://www.youtube.com")


@when(u'preencho o campo "{rapper1}" e clico em pesquisar')
def step_impl(context, rapper1):

    #Escrever no campo de pesquisa
    driver.find_element_by_id("search").send_keys(rapper1)
    sleep(3)
    #Clicar no botão de pesquisar
    driver.find_element_by_css_selector("#search-icon-legacy").click()
    sleep(5)

    #Clicar no link com descrição do nome do video
    cont = 0
    if cont == 0:
        driver.find_element_by_partial_link_text(rapper1).click()
        sleep(3)
    elif cont == 1:
        driver.find_element_by_partial_link_text(rapper1).click()
    elif cont == 2:
        driver.find_element_by_partial_link_text(rapper1).click()
    else:
        pass



@then(u'sou redirecionado para a pagina do video e o titulo da pagina é {titulo}')
def step_impl(context, titulo):
    assert_equal(driver.title, titulo)
    sleep(5)


def after_all(context):
    driver.close()





