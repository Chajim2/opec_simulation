import visualize
import market
import country
import random

SUPPLY_SENSITIVITY = 3   # how much the market price reacts to change in supply
BASE_PRICE = 80         # equilibrium price when supply matches base demand
BASE_SUPPLY = 10        # a million of barrels
PROD_NOISE = 0.2

ROUNDS = 150

def calc_price(supply, base_supply, base_price, sensitivity):
    return  base_price - sensitivity * (supply - base_supply) 


class Simulation():
    def __init__(self):
        self.market_state = market.MarketState(BASE_PRICE, BASE_SUPPLY)
        self.countries = country.COUNTRIES
        self.prices = []
        
    def step(self):
        total_prod = 0
        for country in self.countries:
            country.production = country.decide_production(self.market_state)
            country.production += random.uniform(-1, 1) * PROD_NOISE
            total_prod += country.production

        new_price = calc_price(total_prod, BASE_SUPPLY,
                                BASE_PRICE, SUPPLY_SENSITIVITY)

        self.prices.append(new_price)
        self.market_state.update(new_price, total_prod)
        
        for country in self.countries:
            country.add_history(new_price)

    def plot(self):
        visualize.plot(self.prices)

def main():
    simulation = Simulation()
    for _ in range(ROUNDS):
        simulation.step()

    simulation.plot()

if __name__ == "__main__":
    main()
