import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', index_col=0)

df = df.T

fig, ax = plt.subplots(figsize=(10, 6))

df.plot(ax=ax, kind='line', lw=2, alpha=0.8)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Monthly Nominal Accrued Wages (SUM)', fontsize=12)
ax.set_ylim([100000, 10000000])

ax.legend(fontsize=10, loc='upper left')
plt.title('Changes in Average Monthly Nominal Accrued Wages by Economic Activity (2016-2021)', fontsize=14)

plt.show()
