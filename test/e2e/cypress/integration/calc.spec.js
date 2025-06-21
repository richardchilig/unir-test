/// <reference types="cypress" />

context('Calc', () => {
  beforeEach(() => {
    cy.visit('http://calc-web/')
  })

  it('get the title', () => {
    cy.title().should('include', 'Calculator')
  })

  it('can type operands', () => {
    cy.get('#in-op1').clear().should('have.value', '')
      .type('5').should('have.value', '5')
    cy.get('#in-op2').clear().should('have.value', '')
      .type('-5').should('have.value', '-5')
  })

  it('can click add', () => {
    cy.get('#in-op1').clear().type('2')
    cy.get('#in-op2').clear().type('3')
    cy.get('#button-add').click()
    cy.get('#result-area')
      .invoke('text')
      .should('include', '5')  // más tolerante que 'have.text'
    cy.screenshot()
  })

  it('can click subtract', () => {
    cy.get('#in-op1').clear().type('10')
    cy.get('#in-op2').clear().type('4')
    cy.get('#button-subtract').click()
    cy.get('#result-area')
      .invoke('text')
      .should('include', '6')
  })

  it('can click multiply', () => {
    cy.get('#in-op1').clear().type('2')
    cy.get('#in-op2').clear().type('3')
    cy.get('#button-multiply').click()
    cy.get('#result-area')
      .invoke('text')
      .should('include', '6')
  })

  it('can click divide', () => {
    cy.get('#in-op1').clear().type('10')
    cy.get('#in-op2').clear().type('2')
    cy.get('#button-divide').click()
    cy.get('#result-area')
      .invoke('text')
      .should('include', '5')
  })

  it('increases the history log', () => {
    cy.get('#in-op1').clear().type('4')
    cy.get('#in-op2').clear().type('6')
    cy.get('#button-add').click()
    cy.get('#in-op1').clear().type('10')
    cy.get('#in-op2').clear().type('2')
    cy.get('#button-subtract').click()

    // Mostrar el contenido real del historial en la consola
    cy.get('#history-area').invoke('text').then(text => {
      cy.log('Contenido del historial:', text)
    })

    // Asegurarse de que hay al menos 2 entradas
    cy.get('#history-area li').should('have.length.at.least', 2)
  })
})

