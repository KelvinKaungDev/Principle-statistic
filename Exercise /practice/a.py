from scipy.stats import binom;

ans_one   = binom.pmf(6,6,0.3);

# 0.30
# 0.32
# 0.18
# 0.059
# 0.010
#

ans_two   = binom.cdf(2,6,0.3);
ans_three = 1 - binom.cdf(2,6,0.3);

print(ans_one); #0.059535
print(ans_two); #0.74431
print(ans_three); #0.25569
