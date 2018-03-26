import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_gun = pd.read_csv('../nics-firearm-background-checks.csv')


# get the total checks by each state and each month
checks_by_state = df_gun.groupby(['state', 'month'])['totals'].sum().reset_index()

# dataset that excludes November 1998
checks_by_state_clean = checks_by_state[checks_by_state.month.str.contains('1998-11') == False]


# create a data frame for each state that has total checks by month
# Georgia
checks_by_state_georgia = checks_by_state_clean[checks_by_state_clean['state']=='Georgia']
checks_by_state_georgia = checks_by_state_georgia.groupby('month')['totals'].sum()

# Kentucky
checks_by_state_kentucky = checks_by_state_clean[checks_by_state_clean['state']=='Kentucky']
checks_by_state_kentucky = checks_by_state_kentucky.groupby('month')['totals'].sum()

# Massachusetts
checks_by_state_mass = checks_by_state_clean[checks_by_state_clean['state']=='Massachusetts']
checks_by_state_mass = checks_by_state_mass.groupby('month')['totals'].sum()


# plot graph
growth_rates_tick_placement = pd.np.arange(2, len(checks_by_state_georgia), 12)
plt.style.use('seaborn')
ax_state_growth = checks_by_state_georgia.plot(figsize=(20,8), label='Georgia')
plt.plot(checks_by_state_kentucky, label='Kentucky')
plt.plot(checks_by_state_mass, label='Massachusetts')
plt.legend()

ax_state_growth.set_title("Monthly NICS Gun Permit Check Totals For States With Most Growth", fontsize=24)
ax_state_growth.set_yticklabels([ "{0:,.0f}".format(y) for y in ax_state_growth.get_yticks() ], fontsize=12);
plt.setp(ax_state_growth.get_xticklabels(), rotation=0, fontsize=12)
ax_state_growth.set_xticks(growth_rates_tick_placement)
ax_state_growth.set_xticklabels([checks_by_state_georgia.index[i].split("-")[0] for i in growth_rates_tick_placement])
ax_state_growth.set_xlim(0, len(checks_by_state_georgia) - 1)
ax_state_growth.set_xlabel("")

plt.savefig('../charts/checks_states_most_growth.png')
