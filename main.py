import visualize
import market
import country
import random

SUPPLY_SENSITIVITY = 8   # how much the market price reacts to change in supply
BASE_PRICE = 75         # equilibrium price when supply matches base demand
BASE_SUPPLY = 16        # daily production in a million of barrels of 4 OPEC countries
PROD_NOISE = 0.1

ROUNDS = 50

def calc_price(supply, base_supply, base_price, sensitivity):
    price = base_price - sensitivity * (supply - base_supply)
    return max(10, price)


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
        cheat_index_list = [(c.name, c.cheat_index_history) for c in country.COUNTRIES]
        visualize.plot_cheat_index(cheat_index_list)

def main():
    simulation = Simulation()
    for _ in range(ROUNDS):
        simulation.step()

    simulation.plot()

if __name__ == "__main__":
    main()

    # only gives trustworthy results when PROD_NOISE = 0
    cartel_total = 0
    print("Profit of Each Country with noise fixed to zero:")
    print("")
    for country in country.COUNTRIES:
        print(f"{country.name} : ${int(country.total_profit)}")
        cartel_total += country.total_profit

    print("")
    print(f"Total profit of OPEC cartel with noise fixed to zero: ${int(cartel_total)}")

