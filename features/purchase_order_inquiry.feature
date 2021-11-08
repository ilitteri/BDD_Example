Feature: Purchase order inquiry

    Scenario: Product addition to purchase order
        Given that I have a purchase order with products added
        When I add a product that is not in the to the purchase order
        Then the product is added to the purchase order

    Scenario: Product removal from purchase order
        Given that I have a purchase order with products added
        When I delete an added product from my purchase order
        Then the product is removed from the purchase order
    
    Scenario: Decrease quantity of a product in purchase order
        Given that I have a purchase order with products added
        When I decrease the quantity of an added product
        Then the product's quantity is decreased in the purchase order
    
    Scenario: Increase quantity of a product in purchase order
        Given that I have a purchase order with products added
        When I increase the quantity of an added product
        Then the product's quantity is increased in the purchase order
