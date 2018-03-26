import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_gun = pd.read_csv('../nics-firearm-background-checks.csv')
df_c17 = pd.read_csv('../nst-est2017-01.csv')
df_underage = pd.read_csv('../pop_under_18.csv')


# only take rows 3 through 59, these include the regions and states we need
df_c17 = df_c17.iloc[3:59]
#rename the columns
df_c17.columns = ['region/state', 'census_april_2010', 'est_base', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
#copy the data sets
df1 = df_c17.copy()
df2 = df_c17.copy()
#drop the region/state column from the first copy
df1.drop(columns = ['region/state'], inplace = True)
#get rid of the commas in all of the numbers
for col in df1.columns:
    df1[col] = df1[col].replace({',':''}, regex=True)
#change all of the numbers to integers
df1 = df1.apply(pd.to_numeric)
# strangley, some of the state names had periods in the beginning of the string
df2['region/state'] = df2['region/state'].map(lambda x: x.lstrip('.'))
# change the region/state column into a list to add into other dataframe
df2 = df2['region/state'].tolist()
# insert the list as a column onto the first copy that we cleaned
df1.insert(loc=0, column='region/state', value=df2)
# rename the dataframe
df_census_clean = df1


# use the first row for the name of the columns
df_underage = df_underage.rename(columns = df_underage.iloc[0])
#drop the row with the orignal column names
df_underage = df_underage.reindex(df_underage.index.drop(0))
#drop all columns after estimated total column
df_underage.drop(df_underage.columns[4:], axis = 1, inplace = True)
#drop the Id and Id2 columns
cols = [0,1]
df_underage.drop(df_underage.columns[cols], axis=1, inplace=True)
# rename columns
df_underage.columns = ['geography', 'est_total']
# change the est_total column to integers
df_underage['est_total'] = df_underage['est_total'].astype(int)
# create empty dictionary
df_underage_dict = {}
# write a loop that takes the assigns the states as keys, and the totals as values
x1 = 0
while x1 < len(df_underage):
    state_name = df_underage['geography'].iloc[x1]
    total_num = df_underage['est_total'].iloc[x1]
    df_underage_dict[state_name] = total_num
    x1 = x1+1
# map dictionary to df_census_clean
df_census_clean['pop_underage_2016'] = df_census_clean['region/state'].map(df_underage_dict)
# fill NaN with zeros
df_census_clean['pop_underage_2016'].fillna(0, inplace=True)

# get the total checks by each state and each month
checks_by_state = df_gun.groupby(['state', 'month'])['totals'].sum().reset_index()

# data frame for all checks done in 2016
df_gun_2016 = checks_by_state[checks_by_state.month.str.contains('2016') == True]
# get totals in 2016 in each state
df_gun_2016 = df_gun_2016.groupby('state')['totals'].sum()
# change to dict
df_gun_2016 = df_gun_2016.to_dict()
# map values of checks in 2016 to state names in the census data
df_census_clean['gun_permits_2016'] = df_census_clean['region/state'].map(df_gun_2016)
# change NaN to 0
df_census_clean['gun_permits_2016'].fillna(0, inplace=True)
# we'll use the same method of creating a dictionary
# and turning it into a series
perc_guns_2016_dict = {}
x2=5
while x2 < len(df_census_clean):
    # subtracting the under 18 population to the census
    not_underage = df_census_clean['2016'].iloc[x2] - df_census_clean['pop_underage_2016'].iloc[x2]
    # number of background checks in 2016
    num_guns = df_census_clean['gun_permits_2016'].iloc[x2]
    # percentage
    percent = round(num_guns/not_underage * 100, 2)
    state = df_census_clean['region/state'].iloc[x2]
    perc_guns_2016_dict[state] = percent
    x2 = x2 + 1
# change dict into series and sort from biggest to smallest
df_perc_guns_2016 = pd.Series(perc_guns_2016_dict, name = 'percent')
df_perc_guns_2016.index.name = 'state'
df_perc_guns_2016 = df_perc_guns_2016.sort_values(ascending=False)


# plot graph
percent_total_tick_placement_2016 = pd.np.arange(len(df_perc_guns_2016))
plt.style.use('seaborn')
percent_ax_2016 = df_perc_guns_2016.plot(kind='bar',figsize=(20,8))

percent_ax_2016.set_title("Number of Firearm Background Checks Compared to State Population in 2016", fontsize=24)
plt.setp(percent_ax_2016.get_xticklabels(), fontsize=12)
percent_ax_2016.set_xticks(percent_total_tick_placement_2016)
percent_ax_2016.set_xticklabels(df_perc_guns_2016.index)
percent_ax_2016.set_xlim(0, len(df_perc_guns_2016) - 1)
percent_ax_2016.set_ylabel('Percent')
percent_ax_2016.set_xlabel("")

plt.savefig('../charts/checks_compared_statepop_2016.png')
