Feature: Pesquisar videos no youtube dos melhores Rappers e soma basica

  @rappers
  Scenario Outline: Localizar os videos dos melhores rappers
    Given que acesso o site
    When preencho o campo "<param1>" e clico em pesquisar
    Then sou redirecionado para a pagina do video e o titulo da pagina é <param2>

    Examples:
    | param1 | param2 |
    | eminem cleanin out my closet| Eminem - Cleanin' Out My Closet (Official Music Video) - YouTube |
    | Dr. Dre ft. Snoop Dogg - Still D.R.E. (Official Video) | Dr. Dre ft. Snoop Dogg - Still D.R.E. (Official Video) - YouTube |
    | Joe, Joe Thomas - Ride Wit U (MTV Version) ft. G-Unit | Joe, Joe Thomas - Ride Wit U (MTV Version) ft. G-Unit - YouTube|

    @soma
    Scenario Outline: Efetuar soma
      Given que acesso uma calculadora
      When insiro os valores <num1> e <num2>
      Then o resultado é <res>

      Examples:
      | num1 | num2 | res|
      | 10 | 30 | 40 |
      | 20 | 30 | 50 |
      | 100 | 200| 300 |