# Projeto de Testes Automatizados — QA

Testes end-to-end automatizados para o site [SauceDemo](https://www.saucedemo.com), desenvolvidos com **Cypress** e **Selenium + Python**.

## Casos de Teste

| ID | Cenário | Ferramenta |
|----|---------|------------|
| CT01 | Carregamento da página de login | Cypress + Selenium |
| CT02 | Login com credenciais válidas | Cypress + Selenium |
| CT03 | Login com credenciais inválidas | Cypress + Selenium |
| CT04 | Adicionar produto ao carrinho | Cypress + Selenium |
| CT05 | Logout | Cypress + Selenium |

## Como rodar

### Cypress
```bash
npm install
npx cypress open      # interface visual
npx cypress run       # modo headless
```

### Selenium
```bash
pip install selenium webdriver-manager
python selenium_tests/test_saucedemo.py
```

## Tecnologias
- [Cypress](https://www.cypress.io/)
- [Selenium WebDriver](https://www.selenium.dev/)
- Python 3
- JavaScript