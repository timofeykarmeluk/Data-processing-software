import pyreadr as pr
import pandas as pd
from matplotlib import pyplot as plt

EmissionsDataFrame: pd.DataFrame = pr.read_r("../data/summarySCC_PM25.rds")[None]
ClassificationDataFrame: pd.DataFrame = pr.read_r("../data/Source_Classification_Code.rds")[None]

EmissionsDataFrame.groupby("year", as_index=False).sum("Emissions").plot(x="year", y="Emissions", kind="bar")

EmissionsDataFrame[EmissionsDataFrame["fips"] == "24510"].groupby("year", as_index=False).sum("Emissions") \
    .plot(x="year", y="Emissions", kind="bar")

fig, ax = plt.subplots(2, 2)
for i, t in enumerate(EmissionsDataFrame["type"].drop_duplicates().tolist()):
    EmissionsDataFrame[EmissionsDataFrame["type"] == t].groupby("year", as_index=False).sum("Emissions") \
        .plot(x="year", y="Emissions", kind="bar", ax=ax[int(i / 2), i % 2])
    ax[int(i / 2), i % 2].set_title(t)
sources = [i for i in ClassificationDataFrame[["SCC", "EI.Sector"]].to_dict().values()]
sources = {sources[0][i]: sources[1][i] for i in range(len(sources[0]))}
DataFrame = EmissionsDataFrame.apply(lambda x: x.apply(lambda y: sources[y]) if x.name == "SCC" else x)

DataFrame[DataFrame["SCC"].str.contains("Coal")] \
    .groupby("year", as_index=False) \
    .sum("Emissions") \
    .plot(x="year", y="Emissions", kind="bar")

DataFrame[(DataFrame["SCC"].str.startswith("Mobile")) & (DataFrame["fips"] == "24510")] \
    .groupby("year", as_index=False) \
    .sum("Emissions") \
    .plot(x="year", y="Emissions", kind="bar")

DataFrame[(DataFrame["SCC"].str.startswith("Mobile")) & (DataFrame["fips"] == "06037")] \
    .groupby("year", as_index=False) \
    .sum("Emissions") \
    .plot(x="year", y="Emissions", kind="bar")

plt.show()
