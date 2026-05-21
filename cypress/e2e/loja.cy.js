// Projeto de testes E2E — Cypress
// Site de exemplo: https://www.saucedemo.com (site público feito para treino de QA)

describe('Testes da loja SauceDemo', () => {

  beforeEach(() => {
    // Antes de cada teste, acessa o site
    cy.visit('https://www.saucedemo.com')
  })

  it('CT01 - Deve carregar a página de login', () => {
    cy.title().should('include', 'Swag Labs')
    cy.get('#user-name').should('be.visible')
    cy.get('#password').should('be.visible')
    cy.get('#login-button').should('be.visible')
  })

  it('CT02 - Deve fazer login com credenciais válidas', () => {
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()
    cy.url().should('include', '/inventory')
    cy.get('.title').should('have.text', 'Products')
  })

  it('CT03 - Deve exibir erro com credenciais inválidas', () => {
    cy.get('#user-name').type('usuario_errado')
    cy.get('#password').type('senha_errada')
    cy.get('#login-button').click()
    cy.get('[data-test="error"]').should('be.visible')
    cy.get('[data-test="error"]').should('contain', 'Username and password do not match')
  })

  it('CT04 - Deve adicionar produto ao carrinho', () => {
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()
    cy.get('.inventory_item').first().find('button').click()
    cy.get('.shopping_cart_badge').should('have.text', '1')
  })

  it('CT05 - Deve fazer logout', () => {
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()
    cy.get('#react-burger-menu-btn').click()
    cy.get('#logout_sidebar_link').click()
    cy.url().should('eq', 'https://www.saucedemo.com/')
  })

})