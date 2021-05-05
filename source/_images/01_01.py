from mypo import Loader, Market
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

LOAD = True
PATH = "/app/source/_images/"

if not LOAD:
    loader = Loader()
    loader.get('SPY', 0)
    loader.get('SHY', 0)
    loader.get('IEF', 0)
    loader.get('TLT', 0)
    loader.get('EWJ', 0)
    loader.get('FXI', 0)
    loader.get('GLD', 0)
    loader.get('^GSPC', 0)
    loader.save(os.path.join(PATH, '01_01.bin'))
else:
    loader = Loader.load(os.path.join(PATH, '01_01.bin'))

# ETF
loader._total_assets['^GSPC'] = 0
etf = loader.filter(tickers=['SPY', '^GSPC']).get_market()
df = etf.get_normalized_prices()
df.rename(columns={'^GSPC': 'S&P500'}, inplace=True)
df = pd.melt(df.reset_index(), var_name='銘柄', id_vars='Date', value_name='price')


plt.clf()
sns.set_theme(style="darkgrid")
sns.set(font='IPAGothic')

grid = sns.relplot(x='Date', y='price', col='銘柄', data=df, kind='line', aspect=1.5)
grid.set_axis_labels("", "倍率")
grid.set_titles("")

plt.savefig(os.path.join(PATH, "01_01_fig_ETF.svg"), bbox_inches='tight')

spy = loader.filter(tickers=['SPY']).get_market()
df = spy.get_normalized_prices()

# SPY
plt.clf()
sns.set_theme(style="darkgrid")
sns.set(font='IPAGothic')

grid = sns.relplot(x='Date', y='SPY', data=df, kind='line', aspect=1.5)
ax = plt.gca()
ax.set(xlabel='', ylabel='倍率')
plt.savefig(os.path.join(PATH, "01_01_fig_SPY.svg"), bbox_inches='tight')


plt.clf()
sns.set_theme(style="darkgrid")
sns.set(font='IPAGothic')

grid = sns.relplot(x='Date', y='SPY', data=df, kind='line', aspect=1.5)
ax = plt.gca()
ax.set(xlabel='', ylabel='倍率')
ax.annotate(
    text='',
    xy=(pd.to_datetime('2000-07-01'), 3.5),
    xytext=(pd.to_datetime('2000-07-01'), 4.2),
    arrowprops=dict(facecolor='darkorange', shrink=0.05),
    )
ax.text(
    x=pd.to_datetime('2000-01-01'),
    y=4.2,
    s='ココ',
    color="darkorange",
    fontweight="bold"
)
plt.axhline(y=3.5, color="black", dashes=(2, 1), zorder=0)
plt.savefig(os.path.join(PATH, "01_01_fig_SPY1.svg"), bbox_inches='tight')


plt.clf()
sns.set_theme(style="darkgrid")
sns.set(font='IPAGothic')

grid = sns.relplot(x='Date', y='SPY', data=df, kind='line', aspect=1.5)
ax = plt.gca()
ax.set(xlabel='', ylabel='倍率')
ax.annotate(
    text='',
    xy=(pd.to_datetime('2012-01-01'), 3.1),
    xytext=(pd.to_datetime('2012-01-01'), 4.2),
    arrowprops=dict(facecolor='darkorange', shrink=0.05),
)
ax.text(
    x=pd.to_datetime('2011-8-01'),
    y=4.2,
    s='ココ',
    color="darkorange",
    fontweight="bold"
)
plt.axhline(y=3.1, color="black", dashes=(2, 1), zorder=0)
plt.savefig(os.path.join(PATH, "01_01_fig_SPY2.svg"), bbox_inches='tight')

# EWJ
ewj = loader.filter(tickers=['EWJ']).get_market()
df = ewj.get_normalized_prices()

plt.clf()
sns.set_theme(style="darkgrid")
sns.set(font='IPAGothic')

grid = sns.relplot(x='Date', y='EWJ', data=df, kind='line', aspect=1.5)
ax = plt.gca()
ax.set(xlabel='', ylabel='倍率')

plt.axhline(y=1.1, color="black", dashes=(2, 1), zorder=0)
plt.savefig(os.path.join(PATH, "01_01_fig_EWJ.svg"), bbox_inches='tight')

# FXI
fxi = loader.filter(tickers=['FXI']).get_market()
df = fxi.get_normalized_prices()

plt.clf()
sns.set_theme(style="darkgrid")
sns.set(font='IPAGothic')

grid = sns.relplot(x='Date', y='FXI', data=df, kind='line', aspect=1.5)
ax = plt.gca()
ax.set(xlabel='', ylabel='倍率')

plt.axhline(y=4.1, color="black", dashes=(2, 1), zorder=0)
plt.savefig(os.path.join(PATH, "01_01_fig_FXI.svg"), bbox_inches='tight')


# TLT
tlt = loader.filter(tickers=['TLT']).get_market()
df = tlt.get_normalized_prices()

plt.clf()
sns.set_theme(style="darkgrid")
sns.set(font='IPAGothic')

grid = sns.relplot(x='Date', y='TLT', data=df, kind='line', aspect=1.5)
ax = plt.gca()
ax.set(xlabel='', ylabel='倍率')

plt.savefig(os.path.join(PATH, "01_01_fig_TLT.svg"), bbox_inches='tight')

# IEF
ief = loader.filter(tickers=['IEF']).get_market()
df = ief.get_normalized_prices()

plt.clf()
sns.set_theme(style="darkgrid")
sns.set(font='IPAGothic')

grid = sns.relplot(x='Date', y='IEF', data=df, kind='line', aspect=1.5)
ax = plt.gca()
ax.set(xlabel='', ylabel='倍率')

plt.savefig(os.path.join(PATH, "01_01_fig_IEF.svg"), bbox_inches='tight')

# SHY
shy = loader.filter(tickers=['SHY']).get_market()
df = shy.get_normalized_prices()

plt.clf()
sns.set_theme(style="darkgrid")
sns.set(font='IPAGothic')

grid = sns.relplot(x='Date', y='SHY', data=df, kind='line', aspect=1.5)
ax = plt.gca()
ax.set(xlabel='', ylabel='倍率')

plt.savefig(os.path.join(PATH, "01_01_fig_SHY.svg"), bbox_inches='tight')


# Lehman Brothers
lehman = loader.filter(tickers=['SPY', 'IEF']).get_market()
index = lehman.get_index()

lehman = lehman.extract(index[(pd.to_datetime('2008-1-1') < index) & (index < pd.to_datetime('2012-1-1'))])
df = lehman.get_normalized_prices()
df = pd.melt(df.reset_index(), var_name='ticker', id_vars='Date', value_name='price')

plt.clf()
sns.set_theme(style="darkgrid")
sns.set(font='IPAGothic')

grid = sns.relplot(x='Date', y='price', hue='ticker', data=df, kind='line', aspect=1.5, legend=False)
ax = plt.gca()
ax.set(xlabel='', ylabel='倍率')

ax.text(
    x=pd.to_datetime('2011-11-01'),
    y=1.1,
    s='IEF',
    color="#dd8452",
    fontweight="bold"
)
ax.text(
    x=pd.to_datetime('2011-11-01'),
    y=0.7,
    s='SPY',
    color="#4c72b0",
    fontweight="bold"
)

plt.savefig(os.path.join(PATH, "01_01_fig_LEHMAN.svg"), bbox_inches='tight')
