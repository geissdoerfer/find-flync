import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import click

from neslab.find import Model
from neslab.find import distributions


@click.command()
@click.option(
    "--input-file",
    "-i",
    type=click.Path(exists=True),
    help="csv file with results",
    required=True,
)
def cli(input_file):
    df = pd.read_csv(input_file)
    for dist_name in df["dist_name"].unique():
        df_dist = df[df["dist_name"] == dist_name]
        df_dist = df_dist.sort_values("dist_scale")
        plt.plot(np.arange(len(df_dist)), df_dist["disco_latency"], label=dist_name)

    plt.xticks([])
    plt.xlabel("Scale")
    plt.ylabel("Discovery Latency [slots]")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    cli()