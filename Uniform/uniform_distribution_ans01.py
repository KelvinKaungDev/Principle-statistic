from scipy.stats import norm

ans_one      = norm.cdf(6, 2, 6)
ans_two      = 1 - norm.cdf(5.3, 2, 6)
first_group  = norm.cdf(3, 2, 6)
second_group = norm.cdf(7, 2, 6)
ans_three    = second_group - first_group

print(ans_one)
print(ans_two)
print(ans_three)


