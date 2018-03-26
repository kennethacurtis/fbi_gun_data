import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_gun = pd.read_csv('../nics-firearm-background-checks.csv')

# get the total checks by each state and each month
checks_by_state = df_gun.groupby(['state', 'month'])['totals'].sum().reset_index()

# group the states and sum the totals
state_totals = checks_by_state.groupby('state')['totals'].sum()

# plot graph
state_total_tick_placement = pd.np.arange(len(state_totals))
plt.style.use('seaborn')
state_ax = state_totals.plot(kind='bar',figsize=(20,8))

state_ax.set_title("NICS Background Check Totals By State Since Nov. 1998", fontsize=24)
state_ax.set_yticklabels([ "{0:,.0f}".format(y) for y in state_ax.get_yticks() ], fontsize=12);
plt.setp(state_ax.get_xticklabels(), fontsize=12)
state_ax.set_xticks(state_total_tick_placement)
state_ax.set_xticklabels(state_totals.index)
state_ax.set_xlim(0, len(state_totals) - 1)
state_ax.set_xlabel("")

plt.savefig('../charts/check_totals_state.png')
