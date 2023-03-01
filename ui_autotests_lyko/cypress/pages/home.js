import * as selectors from '../selectors/lyko/lyko-selectors'

export class Home {
    goToHairCareCategoty() {
        cy.get(selectors.mainMenuButton).click();
        cy.contains('Hair Care').click({force: true});
    }
    openMiniCart() {
        cy.get(selectors.miniCartButton).click();
    }
    verifyProductInMiniCart(product) {
        cy.get(selectors.miniCart).within(() => {
            cy.get(product).should('be.visible');
        });
    }
    goToCheckout() {
        cy.contains('To checkout').click({force: true});
        cy.get("h2").contains("Checkout");
    }
}
