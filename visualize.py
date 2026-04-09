import seaborn as sns

def plot(prices: list[int]) -> None:
    line_plot = sns.lineplot(prices)
    fig = line_plot.get_figure()

    line_plot.set_xlabel("Rounds", fontsize=12)
    line_plot.set_ylabel("Barrel price ($)", fontsize=12)
    line_plot.set_title("Crude oil price", fontsize=15)

    fig.savefig("res.png")