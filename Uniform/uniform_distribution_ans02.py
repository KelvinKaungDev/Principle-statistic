from scipy.stats import uniform

ans_one     = uniform.cdf(30, 20, 40)
ans_two     = 1 - uniform.cdf(40, 20, 40)
first_file  = uniform.cdf(35, 20, 40)
second_file = uniform.cdf(45, 20, 40)
ans_three   = second_file - first_file

print(ans_one)
print(ans_two)
print(ans_three)


