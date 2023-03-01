import * as selectors from '../selectors/lyko/lyko-selectors'

export class HairCareCategory {
    filterUVCombs() {
        cy.get(selectors.productCategory).click();
        cy.get(selectors.subProductCategory).click();
    }
    goToFirstProduct() {
        cy.get(selectors.firstProduct).first().click();
    }
    goToSecondProduct() {
        cy.get(selectors.secondProduct).first().click();
    }
}
