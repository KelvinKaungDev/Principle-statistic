from scipy.stats import uniform

ans_one      = uniform.cdf(6, 2, 6)
ans_two      = 1 - uniform.cdf(5.3, 2, 6)
first_group  = uniform.cdf(3, 2, 6)
second_group = uniform.cdf(7, 2, 6)
ans_three    = second_group - first_group

print(ans_one)
print(ans_two)
print(ans_three)


