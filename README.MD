## Investigating NICS Firearm Background Checks with FBI Gun Data

## Project Purpose:

Analyze a dataset and then communicate my findings using Python libraries such as NumPy, pandas, and Matplotlib

<a href='https://kennethacurtis.github.io/fbi_gun_data/'>View the project here</a>

# Conclusions

This analysis allowed me to see the bigger picture when it comes to guns in America. Even though I didn't calculate actual gun sales, the data still allowed me to see trends between each state and all over the U.S. These are the conclusions I have arrived at:

### A one-to-one comparison cannot be made on background checks and gun sales

As noted in the introduction of this analysis, background checks can give you an idea of gun sale activity, but a one-to-one comparison cannot be made. I chose not to estimate gun sales numbers for this reason. Although it is debated on the exact percentage, researchers are discovering that a significant amount of gun sales happen without background checks. In a <a href='https://www.theguardian.com/us-news/2017/jan/02/guns-state-background-checks-study'>report by The Guardian</a>:

>The 2015 survey found that just 22% of gun owners who had acquired a gun in the previous two years reported doing so without a background check. Gun owners who had acquired a gun earlier than that – between two and five years before 2015, or more than five years before – were more likely to remember doing so without a background check. A full 57% of gun owners who reported acquiring their most recent gun more than five years before 2015 reported getting the gun without a background check. Because the survey relied on the memories of the participants, the researchers wrote, the more recent gun acquisition data might be more accurate.

In a similar <a href='https://www.thetrace.org/2015/10/private-sale-loophole-background-check-harvard-research/'>report by The Trace</a>:

> * **Roughly 70 percent**: Gun owners who purchased their most recent gun.
* **Roughly 30 percent**: Gun owners who did not purchase their most recent gun, instead obtaining it through a transfer (i.e., a gift, an inheritance, a swap between friends).
* Zeroing in on the population of gun buyers, about 34 percent did not go through a background check.
* Among the gun owners who got their firearms through a transfer, roughly two-thirds did not go through a background check.

> Add it up, and it works out to:  
* **Roughly 60 percent**: the share of gun owners surveyed who did go through a background check when they obtained (through sale or transfer) their latest gun.
* **Roughly 40 percent**: the share of gun owners who did not.

#### NICS Background check activity has steadily risen since 1998

In the first visualization, the graph showed a steady increase in background checks for guns since 1998. The spikes in December likely due to <a href='https://www.thetrace.org/2015/11/black-friday-gun-sales-background-checks/'>Black Friday sales</a>. Spikes that do not happen in December could be due to <a href='https://www.nytimes.com/interactive/2015/12/10/us/gun-sales-terrorism-obama-restrictions.html'>calls for new gun restrictions</a>.

#### Kentucky has the highest amount of background checks since 1998

Along with the state having the highest amount of checks, the state has some of the highest background check activity, as well as the highest background check growth. Kentucky has some of the <a href='https://en.wikipedia.org/wiki/Gun_laws_in_Kentucky'>least restrictive gun control</a> compared to other states, and <a href='https://www.thetrace.org/2016/11/nra-gun-record-rating-system-straight-a-students/'>over 80% of legislatures recieve a high grade from the NRA</a> on gun legislation. <a href='http://www.lex18.com/story/37602072/state-lawmakers-introduce-gun-control-legislation'>Stricter gun laws</a> have been introduced due to <a href='https://www.cnn.com/2018/01/23/us/kentucky-high-school-shooting/index.html'>recent gun violence</a>. The last graph in this report shows that more firearm background checks happen in Kentucky than people over 18. This shows high activity, but also has a caveat. Kentucky runs a new check on each concealed carry license holder each month, adding to the total number of checks for the state.

# Source Index

###### Data
* U.S. Census Bureau:
    * <a href='https://www.census.gov/data/tables/2017/demo/popest/state-total.html'>Annual population estimates for the U.S.</a>
    * <a href='https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_16_1YR_B09001&prodType=table'> Population Under 18 Years</a>
* FBI National Instant Criminal Background Check System:
    * <a href='https://www.fbi.gov/services/cjis/nics'>NICS webpage</a>
    * <a href='https://github.com/BuzzFeedNews/nics-firearm-background-checks/tree/master/data'>Data repository</a>

###### Reports
* <a href='https://www.thetrace.org/2015/11/black-friday-gun-sales-background-checks/'>FBI: Black Friday 2015 Broke Record for Gun Sales</a>
* <a href='https://www.thetrace.org/2015/10/private-sale-loophole-background-check-harvard-research/'>Just How Many People Get Guns Without a Background Check? Fast-Tracked Research Is Set to Provide an Answer</a>
* <a href='https://en.wikipedia.org/wiki/Gun_laws_in_Kentucky'>Gun laws in Kentucky</a>
* <a href='http://www.lrc.ky.gov/Statutes/statute.aspx?id=43448'>527.020 Carrying concealed deadly weapon</a>
* <a href='https://www.thetrace.org/2016/11/nra-gun-record-rating-system-straight-a-students/'>The NRA’s Straight-A Students</a>
* <a href='https://www.cnn.com/2018/01/23/us/kentucky-high-school-shooting/index.html'>Kentucky school shooting: 2 students killed, 18 injured</a>
* <a href='http://www.lex18.com/story/37602072/state-lawmakers-introduce-gun-control-legislation'>http://www.lex18.com/story/37602072/state-lawmakers-introduce-gun-control-legislation</a>
* <a href='https://nypost.com/2018/01/22/15-year-old-girl-wounded-in-shooting-at-texas-high-school/'>15-year-old girl wounded in shooting at Texas high school</a>
* <a href='https://www.theguardian.com/us-news/2017/jan/02/guns-state-background-checks-study'>
Just one in five Americans obtains gun without background check, survey finds</a>
* <a href='https://www.thetrace.org/2015/10/private-sale-loophole-background-check-harvard-research/'>Just How Many People Get Guns Without a Background Check? Fast-Tracked Research Is Set to Provide an Answer</a>
