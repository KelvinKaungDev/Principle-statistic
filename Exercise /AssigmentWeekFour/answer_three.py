from statsmodels.stats.proportion import proportion_confint

Less_three_hour = proportion_confint(450, 1030, method = 'normal')
more_three_hour = proportion_confint(1030 - 450, 1030, method = 'normal')

print(Less_three_hour)
print(more_three_hour)
