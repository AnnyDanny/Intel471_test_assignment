import * as config from '../selectors/lyko/lyko-env'
import * as selectors from '../selectors/lyko/lyko-selectors'

export class AddProductToCart {
    setCookies() {
        cy.setCookie(selectors.cookieConsent, config.cookieConsentValue);
    }
    visitMainPage() {
        cy.visit(config.prodUrl);
    }
    navigateToMainMenuButton() {
        cy.get(selectors.mainMenuButton).click();
        cy.contains('Hair Care').click({force: true});
    }
    choseProductCategories() {
        cy.get(selectors.productCategory).click();
        cy.get(selectors.subProductCategory).click();
        cy.get(selectors.firstProduct).first().click();
    }
    addProductToCart() {
        cy.contains('Buy').first().click();
        cy.get(selectors.productCategory).first().click();
        cy.get(selectors.secondProduct).first().click();
        cy.contains('Buy').first().click();
    }
    checkMiniCart() {
        cy.get(selectors.miniCartButton).click();
        cy.get(selectors.miniCart).within(() => {
            cy.get(selectors.checkFirstProduct).should('be.visible');
            cy.get(selectors.checkSecondProduct).should('be.visible');
        });
    }
    checkCheckout() {
        cy.contains('To checkout').click({force: true});
        cy.get("h2").contains("Checkout");
        cy.get(selectors.checkFirstProduct).should('be.visible');
        cy.get(selectors.checkSecondProduct).should('be.visible');
    }
}