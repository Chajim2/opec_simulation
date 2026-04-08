class MarketState():
    def __init__(self, price: float, base_supply: int) -> None:
        self.price = price
        self.total_production = 0
        self.base_supply = base_supply 
    
    def update(self, price: float, total_production: int) -> None:
        self.price = price
        self.total_production = total_production
