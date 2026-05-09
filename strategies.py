import random
CHEAT_PROBABILITY = 0.3

def play_comply(country, market_state):
    return country.quota

def play_random(country, market_state):
    if random.random() < CHEAT_PROBABILITY:
        return country.quota * 1.2
    return country.quota

def play_creeper(country, market_state):
    if market_state.price < country.kwargs['cutoff_price']\
          or market_state.round == 0:
        return country.quota
    
    return country.quota * (country.cheat_index_history[-1] + 0.015)

def play_enforce(country, market_state):
    if country.kwargs['flood_left'] > 0:
        if country.kwargs['flood_left'] == 1:
            country.kwargs['cooldown_left'] = country.kwargs['cooldown_length']
        country.kwargs['flood_left'] -= 1
        return country.quota * 1.5

    if country.kwargs['cooldown_left'] > 0:
        country.kwargs['cooldown_left'] -= 1
        return country.quota
    
    if market_state.price > country.kwargs['cutoff_price']\
          or market_state.round == 0:
        return country.quota
    
    # raise hell
    country.kwargs['flood_left'] = country.kwargs['flood_length']
    return country.quota * 1.5

# Country playing this strategy desperate do maintain stable revenue from crude oil production
# Target revenue is calculated as budget price times quota
# Therefore, if market price drop bellow budget price, the quantity to has to
# increase to make that same revenue
def play_desperate(country, market_state):
    if market_state.round == 0:
        return country.quota

    if market_state.price >= country.kwargs['budget_price']:
        return country.quota

    dynamic_multiplier = country.kwargs['budget_price'] / market_state.price
    max_production_multiplier = country.kwargs['max_production'] / country.quota

    return country.quota * min(max_production_multiplier, dynamic_multiplier)


def play_passive(country, market_state):
    return country.quota

strategy_dict = {
    "comply" : play_comply,
    "random" : play_random,
    "creeper" : play_creeper,
    "enforce" : play_enforce,
    "desperate" : play_desperate,
    "passive" : play_passive
}