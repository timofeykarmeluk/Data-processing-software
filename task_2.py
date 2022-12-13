# Task 2. Working with files
import pandas as pd
from tabulate import tabulate
import os

print('Part 1')

def pollutantmean(dir, pol, ids):
    if isinstance(ids, int):
        ids = [ids]
    file = pd.concat([pd.read_csv('../data/' + dir + '/' + format(id, "03d") + ".csv") for id in ids])
    mean = file[pol].mean()
    return mean

print(pollutantmean('specdata', 'sulfate', range(1, 11)))
print(pollutantmean('specdata', 'nitrate', range(70, 73)))
print(pollutantmean('specdata', 'nitrate', 23))

print("Part 2")

def complete(dir, ids):
    if isinstance(ids, int):
        ids = [ids]
    result_data = []
    for id in ids:
        file = pd.read_csv('../data/' + dir + '/' + format(id, "03d") + ".csv").dropna()
        result_data.append([id, len(file.index)])
    col_names = ["id", "nobs"]
    print(tabulate(result_data, headers=col_names))

complete('specdata', 1)
complete('specdata', [2, 4, 8, 10, 12])
complete('specdata', range(30, 24, -1))

print("Part 3")

def corr(dir, threshold):
    files = [pd.read_csv('../data/' + dir + "/" + file).dropna() for file in os.listdir('../data/' + dir)]
    corrs = []
    for file in files:
        if len(file.index) > threshold:
            corrs.append(file['sulfate'].corr(file['nitrate']))
    return corrs

print(corr('specdata', 150))
print(corr('specdata', 400))
print(corr('specdata', 5000))
