export class Checkout {
    verifyProductInCart(product) {
        cy.get(product).should('be.visible');
    }
}
