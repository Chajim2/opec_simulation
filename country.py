
class Country():
    def __init__(self, patience: int, mine_price: int,
                  name: str, quota: int, strategy: str):

        self.patience = patience 
        self.mine_price = mine_price
        self.name = name
        self.quota = quota

        self.production = quota
        self.total_revenue = 0
        self.compliance_history = []
        self.strategy = strategy    

    def decide_production(self, marketState) -> float:
        if self.strategy == "comply":
            return self.quota
    
    def add_history(self, price: float):
        """ call only after setting self.production """
        
        self.total_revenue += price * self.production
        self.compliance_history.append(self.production / self.quota)



COUNTRIES = [
    Country(
        name = "Saudi arabia",
        quota = 10_000_000,
        mine_price = 3,
        patience = 10,
        strategy = "comply"
    ),Country(
        name="Venezuela",
        quota=2_000_000,
        mine_price=20,
        patience=2,
        strategy="comply"
    ),
    Country(
        name="UAE",
        quota=4_000_000,
        mine_price=5,
        patience=8,
        strategy="comply"
    )
]
