from behave import *
from behave.runner import Context

from purchase_order import PurchaseOrder
from product_data import ProductData

@given("that I have a purchase order with products added")
def step_impl(context: Context) -> None:
    some_product = ProductData(
        id="1",
        description="apple tv",
        category="tv",
        manufacturer="apple",
        price=199.99,
        stock=999999
    )
    context.order = PurchaseOrder()
    context.order.add_product(product=some_product, quantity=2)

# Scenario 1
@when("I add a product that is not in the to the purchase order")
def step_impl(context: Context) -> None:
    other_product = ProductData(
        id="2",
        description="iphone 13",
        category="smartphones",
        manufacturer="apple",
        price=1199.99,
        stock=999999
    )
    context.order.add_product(product=other_product, quantity=1)

@then("the product is added to the purchase order")
def step_impl(context: Context) -> None:
    assert "2" in context.order


# Scenario 2
@when("I delete an added product from my purchase order")
def step_impl(context: Context) -> None:
    context.order.remove_product(product_id="1")

@then("the product is removed from the purchase order")
def step_impl(context: Context) -> None:
    assert "1" not in context.order


# Scenario 3
@when("I decrease the quantity of an added product")
def step_impl(context: Context) -> None:
    context.order.decrease_quantity(product_id="1")

@then("the product's quantity is decreased in the purchase order")
def step_impl(context: Context) -> None:
    assert context.order.product_quantity(product_id="1") == 1


# Scenario 4
@when("I increase the quantity of an added product")
def step_impl(context: Context) -> None:
    context.order.increase_quantity(product_id="1")

@then("the product's quantity is increased in the purchase order")
def step_impl(context: Context) -> None:
    assert context.order.product_quantity(product_id="1") == 3
