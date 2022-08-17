from statsmodels.stats.weightstats import ztest
data = [55, 85, 90, 30, 45, 65, 25, 72, 103, 35]
alpha = 0.05
zscore, pvalue= ztest(data, value = 60)
print("Z statistics: ", zscore)
print("P value: ", pvalue)

if( pvalue< alpha):
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")
