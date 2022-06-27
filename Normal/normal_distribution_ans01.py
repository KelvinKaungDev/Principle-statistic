import imp
from scipy.stats import norm

first_height  = norm.cdf(180, 185, 2.5)
second_height = norm.cdf(190, 185, 2.5)
ans_one       = second_height - first_height
ans_two       = 1 - norm.cdf(192, 185, 2.5)
ans_three     = norm.cdf(178, 185, 2.5)

print(ans_one)
print(ans_two)
print(ans_three)
