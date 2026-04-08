import strategies
import random

CHEAT_PROBABILITY = 0.3

class Country():
    def __init__(self, patience: int, mine_price: int,
                  name: str, quota: float, strategy: str,
                  kwargs = {}):

        self.patience = patience 
        self.mine_price = mine_price
        self.name = name
        self.quota = quota
        self.kwargs = kwargs

        self.production = quota
        self.total_revenue = 0
        self.total_profit = 0
        self.compliance_history = []
        self.strategy = strategy    

    def decide_production(self, market_state) -> float:
        strategy_function = strategies.strategy_dict[self.strategy]
        return strategy_function(self, market_state)
    
    def add_history(self, price: float):
        """ call only after setting self.production """

        self.total_revenue += price * self.production
        self.total_profit += (price - self.mine_price) * self.production
        self.compliance_history.append(self.production / self.quota)



COUNTRIES = [
    Country(
        name = "Saudi arabia",
        quota = 10,
        mine_price = 3,
        patience = 10,
        strategy = "enforce",
        kwargs= {
            "cutoff_price" : 45,
            "flood_left" : 0,
            "flood_length" : 3,
            "cooldown_left" : 0,
            "cooldown_length" : 3 
        }
    ),Country(
        name="Venezuela",
        quota=2,
        mine_price=20,
        patience=2,
        strategy="random"
    ),
    Country(
        name="UAE",
        quota=4,
        mine_price=5,
        patience=8,
        strategy="creeper",
        kwargs={"cutoff_price" : 45}
    )
]
