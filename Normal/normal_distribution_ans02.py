import imp
from scipy.stats import norm

ans_one   = 1 - norm.cdf(110, 100, 16)
ans_two   = norm.cdf(85, 100, 16)
first_Iq  = norm.cdf(90, 100, 16)
second_Iq = norm.cdf(115, 100, 16)
ans_three = second_Iq - first_Iq

print(ans_one)
print(ans_two)
print(ans_three)
