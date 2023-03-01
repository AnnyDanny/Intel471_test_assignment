import { Checkout } from '../pages/checkout';
import { HairCareCategory } from '../pages/hair_care_category';
import { Home } from '../pages/home'
import { Product } from '../pages/product';
import * as config from '../selectors/lyko/lyko-env'
import * as selectors from '../selectors/lyko/lyko-selectors'

const checkout = new Checkout();
const hairCareCategory = new HairCareCategory();
const home = new Home();
const product = new Product();

describe('Add products to cart', () => {
  beforeEach(() => {
      cy.setCookie(selectors.cookieConsent, config.cookieConsentValue);
      cy.visit(config.prodUrl);
  });

  it('Add product to cart', () => {
    home.goToHairCareCategoty();

    hairCareCategory.filterUVCombs();
    hairCareCategory.goToFirstProduct();

    product.addProductToCart();
    product.goToCategory();

    hairCareCategory.goToSecondProduct();

    product.addProductToCart();

    home.openMiniCart();
    home.verifyProductInMiniCart(product.elements.firstProduct);
    home.verifyProductInMiniCart(product.elements.secondProduct);
    home.goToCheckout();

    checkout.verifyProductInCart(product.elements.firstProduct);
    checkout.verifyProductInCart(product.elements.secondProduct);
  });
});
