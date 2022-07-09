from statsmodels.stats.proportion import proportion_confint

Approve = proportion_confint(410, 1000, method = 'normal')
Fail    = proportion_confint(1000 - 410, 1000, method = 'normal')


print(Approve)
print(Fail)
