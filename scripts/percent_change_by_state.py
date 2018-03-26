import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_gun = pd.read_csv('../nics-firearm-background-checks.csv')

checks_by_state = df_gun.groupby(['state', 'month'])['totals'].sum().reset_index()

# dataset that excludes November 1998
checks_by_state_clean = checks_by_state[checks_by_state.month.str.contains('1998-11') == False]

# using same method as above to make a dictionary
# and turn it into a pandas Series
x=0
change_dict_clean = {}
while x < len(checks_by_state_clean):
    og_num = checks_by_state_clean.iloc[x]['totals']
    new_num = checks_by_state_clean.iloc[x + 230]['totals']
    decrease = new_num - og_num
    perc_change = round(decrease / og_num * 100, 0)
    change_dict_clean[checks_by_state_clean.iloc[x]['state']] = perc_change
    x = x + 231

df_percent_change_clean = pd.Series(change_dict_clean, name = 'percent_change')
df_percent_change_clean.index.name = 'state'

# drop inf
df_percent_change_clean = df_percent_change_clean.replace([np.inf, -np.inf], np.nan).dropna()

# sort biggest to smallest
df_percent_change_clean = df_percent_change_clean.sort_values(ascending = False)

# plot graph
percent_total_tick_placement_clean = pd.np.arange(len(df_percent_change_clean))
plt.style.use('seaborn')
percent_ax_clean = df_percent_change_clean.plot(kind='bar',figsize=(20,8))

percent_ax_clean.set_title("Firearm Background Check Growth Rate by State Since Dec. 1999", fontsize=24)
percent_ax_clean.set_yticklabels([ "{0:,.0f}".format(y) for y in percent_ax_clean.get_yticks() ], fontsize=12);
plt.setp(percent_ax_clean.get_xticklabels(), fontsize=12)
percent_ax_clean.set_xticks(percent_total_tick_placement_clean)
percent_ax_clean.set_xticklabels(df_percent_change_clean.index)
percent_ax_clean.set_xlim(0, len(df_percent_change_clean) - 1)
percent_ax_clean.set_ylabel('Percent')
percent_ax_clean.set_xlabel("")

plt.savefig('../charts/percent_change_by_state.png')
