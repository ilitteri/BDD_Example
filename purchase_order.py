from __future__ import annotations

from typing import Dict, Tuple
from product_data import ProductData

class PurchaseOrder:
    def __init__(self) -> None:
        self.__products: Dict[str, Tuple[ProductData, int]] = {}

    def __contains__(self, product_id: str) -> bool:
        return product_id in self.__products

    def add_product(self, product: ProductData, quantity: int) -> None:
        self.__products[product.id] = [product, quantity]

    def remove_product(self, product_id: str) -> None:
        del self.__products[product_id]

    def increase_quantity(self, product_id: str, quantity: int=1) -> None:
        self.__products[product_id][1] += quantity

    def decrease_quantity(self, product_id: str, quantity: int=1) -> None:
        self.__products[product_id][1] -= quantity

    def products(self):
        return list(self.__products.keys())

    def product_quantity(self, product_id:  str) -> ProductData:
        return self.__products[product_id][1]
