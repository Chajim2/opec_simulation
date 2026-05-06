import strategies
import json

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

def load_countries(strategy_name, path="strategies.json"):
    with open(path) as f:
        data = json.load(f)

    try:
        configs = data[strategy_name]
    except KeyError:
        raise ValueError(f"Available strategies: {list(data.keys())}")

    countries = []
    for c in configs:
        c.setdefault("kwargs", {})
        countries.append(Country(**c))

    return countries

COUNTRIES = load_countries("base_strat") 
