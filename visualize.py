import seaborn as sns

def plot(prices: list[int]) -> None:
    line_plot = sns.lineplot(prices)
    fig = line_plot.get_figure()

    line_plot.set_xlabel("Rounds", fontsize=12)
    line_plot.set_ylabel("Barrel price ($)", fontsize=12)
    line_plot.set_title("Crude oil price", fontsize=15)

    fig.savefig("res.png")
    fig.clear()

def plot_compliance(compliance_list: list[tuple[str, list[float]]]) -> None:
    line_plot = None

    for name, compliance in compliance_list:
        line_plot = sns.lineplot(compliance, label=name)

    fig = line_plot.get_figure()

    line_plot.set_xlabel("Rounds", fontsize=12)
    line_plot.set_ylabel("Compliance", fontsize=12)
    line_plot.set_title("Compliance over time", fontsize=15)

    line_plot.legend()
    fig.savefig("compliance.png")
    fig.clear()