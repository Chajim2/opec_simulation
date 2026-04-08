import matplotlib.pyplot as plt
import seaborn as sns

def plot(prices: list[int]) -> None:
    line_plot = sns.lineplot(prices)
    fig = line_plot.get_figure()
    fig.savefig("res.png")