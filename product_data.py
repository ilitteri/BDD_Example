class ProductData:
    def __init__(
        self, 
        id: str, 
        description: str, 
        category: str, 
        manufacturer: str, 
        price: float, 
        stock: int
    ) -> None:
        self.id = id
        self.description = description
        self.category = category
        self.manufacturer = manufacturer
        self.price = price
        self.stock = stock
