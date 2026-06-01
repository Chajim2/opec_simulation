import seaborn as sns
import pandas as pd

def plot(prices: list[int]) -> None:
    line_plot = sns.lineplot(prices)
    fig = line_plot.get_figure()

    line_plot.set_xlabel("Rounds", fontsize=12)
    line_plot.set_ylabel("Barrel price ($)", fontsize=12)
    line_plot.set_title("Crude oil price", fontsize=15)

    line_plot.set_ylim(0, 100)

    fig.savefig("results/price.png")
    fig.clear()

def plot_cheat_index(cheat_index_list: list[tuple[str, list[float]]]) -> None:
    line_plot = None

    for name, cheat_index in cheat_index_list:
        line_plot = sns.lineplot(cheat_index, label=name)

    fig = line_plot.get_figure()

    line_plot.set_xlabel("Rounds", fontsize=12)
    line_plot.set_ylabel("Production/Quota", fontsize=12)
    line_plot.set_title("Cheating over time", fontsize=15)

    line_plot.set_ylim(0.8, 2)

    line_plot.legend()
    fig.savefig("results/cheating.png")
    fig.clear()

def plot_revenues(revenues : list[int], countries : list[str]):
    bar_plot = sns.barplot(x=countries, y=revenues)
    fig = bar_plot.get_figure()

    bar_plot.set_xlabel("Country", fontsize=12)
    bar_plot.set_ylabel("Revenue (million $)", fontsize=12)
    bar_plot.set_title("Revenue by Country", fontsize=15)

    bar_plot.set_ylim(0, 30_000)

    fig.tight_layout()
    fig.savefig("results/revenues.png")
    fig.clear()

def plot_strategy_revenues(strategy_data: dict[str, list[float]], countries: list[str]) -> None:
    rows = []

    for strategy, revenues in strategy_data.items():
        for country, revenue in zip(countries, revenues):
            rows.append({
                "Country": country,
                "Revenue": revenue,
                "Strategy": strategy
            })

    df = pd.DataFrame(rows)

    bar_plot = sns.barplot(
        data=df,
        x="Country",
        y="Revenue",
        hue="Strategy"
    )

    fig = bar_plot.get_figure()

    bar_plot.set_xlabel("Country", fontsize=12)
    bar_plot.set_ylabel("Revenue (million $)", fontsize=12)
    bar_plot.set_title("Revenue by Strategy", fontsize=15)

    bar_plot.set_ylim(0, 40_000)

    fig.tight_layout()
    fig.savefig("results/strategy_revenues.png")
    fig.clear()


def plot_strategy_prices(strategy_names: list[str],
                         price_hists: list[list[float]]) -> None:

    line_plot = None

    for strategy, prices in zip(strategy_names, price_hists):
        line_plot = sns.lineplot(
            x=range(len(prices)),
            y=prices,
            label=strategy
        )

    fig = line_plot.get_figure()

    line_plot.set_ylim(0, 100)

    line_plot.set_xlabel("Rounds", fontsize=12)
    line_plot.set_ylabel("Barrel price ($)", fontsize=12)
    line_plot.set_title("Oil price by strategy", fontsize=15)

    line_plot.legend()

    fig.savefig("results/strategy_prices.png")
    fig.clear()