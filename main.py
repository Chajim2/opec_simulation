import visualize
import market
import country
import random

SUPPLY_SENSITIVITY = 8   # how much the market price reacts to change in supply
BASE_PRICE = 75         # equilibrium price when supply matches base demand
BASE_SUPPLY = 16        # daily production in a million of barrels of 4 OPEC countries
PROD_NOISE = 0.1
DEMAND_SHOCK_SIZE = -30

ROUNDS = 50
DEMAND_SHOCK_ROUND = ROUNDS // 2 # set to above rounds so it never triggers, 
                                #change to // 2 for a demand shock

def calc_price(supply, base_supply, base_price, sensitivity):
    price = base_price - sensitivity * (supply - base_supply)
    return max(10, price)


class Simulation():
    def __init__(self):
        self.market_state = market.MarketState(BASE_PRICE, BASE_SUPPLY)
        self.countries = country.COUNTRIES
        self.prices = []
        self.demand_shift = 0.0
        self.shock_applied = False
        
    def step(self):
        total_prod = 0
        for country in self.countries:
            country.production = country.decide_production(self.market_state)
            country.production += random.uniform(-1, 1) * PROD_NOISE
            total_prod += country.production

        if not self.shock_applied and self.market_state.round == DEMAND_SHOCK_ROUND:
            self.demand_shift += DEMAND_SHOCK_SIZE
            self.shock_applied = True

        new_price = calc_price(total_prod, BASE_SUPPLY,
                                BASE_PRICE + self.demand_shift, SUPPLY_SENSITIVITY)

        self.prices.append(new_price)
        self.market_state.update(new_price, total_prod)
        
        for country in self.countries:
            country.add_history(new_price)

    def plot(self):
        visualize.plot(self.prices)
        cheat_index_list = [(c.name, c.cheat_index_history) for c in country.COUNTRIES]
        visualize.plot_cheat_index(cheat_index_list)
        visualize.plot_revenues([c.total_revenue for c in self.countries],
                                 [c.name for c in self.countries])

    def get_revenues(self):
        return [c.total_revenue for c in self.countries]

    def get_prices(self):
        return self.prices

    def change_start(self, start_name):
        try:
            self.countries = country.load_countries(start_name)        
        except:
            print("strategy not found")


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

