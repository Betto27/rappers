from behave import given, when, then
from time import sleep
from nose.tools import assert_equal
from selenium import webdriver


driver = webdriver.Chrome()

@given(u'que acesso o {url}')
def step_impl(context, url):
    driver.maximize_window()
    driver.get(url)



@when(u'eu preencho os campos e clico em registrar')
def step_impl(context):
    #Campo primeiro nome
    driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(1) > div:nth-child(2) > input').send_keys('Jurema')
    #Campo segundo nome
    driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(1) > div:nth-child(3) > input').send_keys('Aguiar')
    #Campo endereço
    driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(2) > div > textarea').send_keys('Brasil, Copa Cabana')
    #Campo email
    driver.find_element_by_css_selector('#eid > input').send_keys('Jurema@gmail.com')
    #Campo telefone
    driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(4) > div > input').send_keys('9878554200')
    #Campo sexo
    driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(5) > div > label:nth-child(2) > input').click()
    #Campo Hobbies
    driver.find_element_by_id('checkbox1').click()
    driver.find_element_by_id('checkbox2').click()
    driver.find_element_by_id('checkbox3').click()
    #Campo language
    driver.find_element_by_id('msdd').click()
    driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(7) > div > multi-select > div:nth-child(2) > ul > li:nth-child(29)').click()
    #Click fora para fechar o combobox
    driver.find_element_by_css_selector('#section > div > div').click()
    #Campo Skills
    driver.find_element_by_css_selector('#Skills').click()
    driver.find_element_by_css_selector('#Skills > option:nth-child(61)').click()
    #Campo Country
    driver.find_element_by_css_selector('#countries').click()
    driver.find_element_by_css_selector('#countries > option:nth-child(33)').click()
    #Campo selecionar Country
    driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(10) > div > span > span.selection > span').click()
    driver.find_element_by_css_selector('#select2-country-results > li.select2-results__option.select2-results__option--highlighted').click()
    #Campo Ano
    driver.find_element_by_css_selector('#yearbox').click()
    driver.find_element_by_css_selector('#yearbox > option:nth-child(5)').click()
    #Campo mês
    driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(11) > div:nth-child(3) > select').click()
    driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(11) > div:nth-child(3) > select > option:nth-child(5)').click()
    #Campo dia
    driver.find_element_by_css_selector('#daybox').click()
    driver.find_element_by_css_selector('#daybox > option:nth-child(6)').click()
    #Campo password
    driver.find_element_by_css_selector('#firstpassword').send_keys('L123*456p')
    #Campo Confirmar password
    driver.find_element_by_css_selector('#secondpassword').send_keys('L123*456p')
    #Clicar no botão enviar
    driver.find_element_by_css_selector('#submitbtn').click()

@then(u'os sistema me retorna uma mensagem')
def step_impl(context):
    sleep(10)
    driver.close()
