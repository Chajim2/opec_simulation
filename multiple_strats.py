from main import Simulation, ROUNDS
from simulation.visualize import plot_strategy_revenues, plot_strategy_prices
import json

rev_by_strat = {}
price_per_strat = []

COUNTRY_NAMES = ["Saudi Arabia", "Venezuela", "UAE", "Nigeria"]
STRAT_NAMES = []

def one_run(strat_name):
    simulation = Simulation(strat_name)
    for _ in range(ROUNDS):
        simulation.step()
    rev_by_strat[strat_name] = simulation.get_revenues()
    price_per_strat.append(simulation.get_prices())


def compare_all():
    with open("strategies.json", "r") as f:
        all_strats = json.load(f)
    for name, _ in all_strats.items():
        #if name not in ["saudi_enforcer", "saudi_saviour"]:
         #   continue
        STRAT_NAMES.append(name)
        one_run(name)
    
compare_all()
plot_strategy_revenues(rev_by_strat, COUNTRY_NAMES)
plot_strategy_prices(STRAT_NAMES, price_per_strat)