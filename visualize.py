import seaborn as sns

def plot(prices: list[int]) -> None:
    line_plot = sns.lineplot(prices)
    fig = line_plot.get_figure()

    line_plot.set_xlabel("Rounds", fontsize=12)
    line_plot.set_ylabel("Barrel price ($)", fontsize=12)
    line_plot.set_title("Crude oil price", fontsize=15)

    fig.savefig("0_price.png")
    fig.clear()

def plot_cheat_index(cheat_index_list: list[tuple[str, list[float]]]) -> None:
    line_plot = None

    for name, cheat_index in cheat_index_list:
        line_plot = sns.lineplot(cheat_index, label=name)

    fig = line_plot.get_figure()

    line_plot.set_xlabel("Rounds", fontsize=12)
    line_plot.set_ylabel("Level of cheating", fontsize=12)
    line_plot.set_title("Cheating over time", fontsize=15)

    line_plot.legend()
    fig.savefig("0_cheating.png")
    fig.clear()