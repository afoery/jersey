#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:18:48 2020

@author: alisha
"""
import matplotlib.pyplot as plt
import functions, analysis_importD, analysis_diff, analysis_stats
from scipy.stats import ttest_rel
import matplotlib.patches as mpatches


#get path to data file
path = functions.get_data_in_parentDic('data')

#import df
df, numbers = analysis_importD.import_df(path)

#extract data
ans = analysis_importD.extract_data(df, 'slider')


#calculate diff between rating [high - low]
diff, high_num, low_num = analysis_diff.order_and_diff(numbers, ans)

#individual t-tests
t_test_indiv = analysis_stats.indiv_ttest(high_num, low_num)

#color significant means
colors = []
for i in range(len(t_test_indiv)):
    if t_test_indiv[i][1] < 0.05:
        colors.append("pink")
    else:
        colors.append('blue')
        
        
#plot means of indiv subs
means = diff.mean(axis = 1)
means_barplot = means.plot.bar(color = colors)
means_barplot.set_xlabel('Participants')
means_barplot.set_ylabel('Subject mean difference scores')

#add legend
patch = mpatches.Patch(color = 'pink', label = r'$\alpha$ < 0.05')
patch2 = mpatches.Patch(color = 'blue', label = r'$\alpha$ > 0.05')

means_barplot.legend(handles = [patch, patch2])



means_of_means = means.mean()
std_of_means = means.std()


#means of high and low number ratings
means_high = high_num.mean(axis = 1).to_list()
means_low  = low_num.mean(axis = 1).to_list()

#run a t-test for the group
t_test_group = ttest_rel(means_high, means_low)
print(t_test_group)


#plot group average and p value
fig, ax = plt.subplots()
ax.bar(1,means_of_means, yerr = std_of_means, capsize = 7)
ax.text(1.3,3, F'p = {round(t_test_group[1],3)}')
ax.set_ylabel('Group mean difference score')
ax.set_xticks([])
