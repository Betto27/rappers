Feature: Acessar o site de forma automatizada

  @registrar
  Scenario: Se registrar no site
    Given que acesso o http://demo.automationtesting.in/Register.html
    When eu preencho os campos e clico em registrar
    Then os sistema me retorna uma mensagem