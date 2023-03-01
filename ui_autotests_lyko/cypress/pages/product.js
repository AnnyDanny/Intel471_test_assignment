import * as selectors from '../selectors/lyko/lyko-selectors'

export class Product {
    elements ={
        firstProduct : selectors.checkFirstProduct,
        secondProduct : selectors.checkSecondProduct,
    }
    addProductToCart() {
        cy.contains('Buy').first().click();
    }
    goToCategory() {
        cy.get(selectors.productCategory).first().click();
    }
}
