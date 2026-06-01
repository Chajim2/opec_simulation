import simulation.visualize as visualize
import simulation.market as market
import simulation.country as country
import random

import json

SUPPLY_SENSITIVITY = 8  # how much the market price reacts to change in supply
BASE_PRICE = 75  # equilibrium price when supply matches base demand
BASE_SUPPLY = 16  # daily production in a million of barrels of 4 OPEC countries
PROD_NOISE = 0.15

CURR_STRAT = "ignore_opec"

ROUNDS = 50


def calc_price(supply, base_supply, base_price, sensitivity):
    price = base_price - sensitivity * (supply - base_supply)
    return max(10, price)


class Simulation:
    def __init__(self, strat_name):
        self.market_state = market.MarketState(BASE_PRICE, BASE_SUPPLY)
        self.countries = self.load_countries(strategy_name=strat_name)
        self.prices = []

    def step(self):
        total_prod = 0
        for country in self.countries:
            country.production = country.decide_production(self.market_state)
            country.production += random.uniform(-1, 1) * PROD_NOISE
            total_prod += country.production

        new_price = calc_price(total_prod, BASE_SUPPLY, BASE_PRICE, SUPPLY_SENSITIVITY)

        self.prices.append(new_price)
        self.market_state.update(new_price, total_prod)

        for country in self.countries:
            country.add_history(new_price)

    def plot(self):
        visualize.plot(self.prices)
        cheat_index_list = [(c.name, c.cheat_index_history) for c in self.countries]
        visualize.plot_cheat_index(cheat_index_list)

    def change_strat(self, new_strat):
        self.countries = self.load_countries(new_strat)

    def get_revenues(self):
        return [c.total_revenue for c in self.countries]

    def get_prices(self):
        return self.prices

    def load_countries(self, strategy_name, path="strategies.json"):
        with open(path) as f:
            data = json.load(f)
        try:
            configs = data[strategy_name]
        except KeyError:
            raise ValueError(f"Available strategies: {list(data.keys())}")

        countries = []
        for c in configs:
            c.setdefault("kwargs", {})
            countries.append(country.Country(**c))

        return countries


def main():
    simulation = Simulation(CURR_STRAT)
    for _ in range(ROUNDS):
        simulation.step()

    simulation.plot()

    cartel_total = 0
    print("strategy: ", CURR_STRAT)
    print("")
    print("Revenue of Each Country with noise fixed to zero:")
    print("")
    for country in simulation.countries:
        print(f"{country.name} : ${int(country.total_revenue)}")
        cartel_total += country.total_revenue

    print("")
    print(
        f"Total revenue of OPEC cartel with noise fixed to zero: ${int(cartel_total)}"
    )



if __name__ == "__main__":
    main()

