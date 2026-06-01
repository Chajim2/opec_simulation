class MarketState():
    def __init__(self, price: float, base_supply: int) -> None:
        self.price = price
        self.base_supply = base_supply 

        self.total_production = 0
        self.round = 0
    
    def update(self, price: float, total_production: int) -> None:
        self.price = price
        self.total_production = total_production
        self.round += 1
