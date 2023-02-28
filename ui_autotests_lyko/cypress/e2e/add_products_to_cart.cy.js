import { AddProductToCart } from '../pages/add_product_to_cart';

const addProductToCart = new AddProductToCart()

describe('Add products to cart', () => {
  beforeEach(() => {
    addProductToCart.setCookies();
    addProductToCart.visitMainPage();
  });

  it('Add product to cart', () => {
    addProductToCart.navigateToMainMenuButton();
    addProductToCart.choseProductCategories();
    addProductToCart.addProductToCart();
    addProductToCart.checkMiniCart();
    addProductToCart.checkCheckout();
  });
});
