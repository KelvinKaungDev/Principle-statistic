from scipy.stats import norm

ans_one     = 1 - norm.cdf(30, 20, 40)
ans_two     = 1 - norm.cdf(40, 20, 40)
first_file  = norm.cdf(35, 20, 40)
second_file = norm.cdf(45, 20, 40)
ans_three   = second_file - first_file

print(ans_one)
print(ans_two)
print(ans_three)


