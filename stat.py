# code to save my sanity for stat319 ch9 stuff
# https://www.geeksforgeeks.org/how-to-find-the-z-critical-value-in-python/ 
# https://www.geeksforgeeks.org/introduction-to-power-analysis-in-python/

import statistics   as st
import math         as m
import numpy        as np
import scipy        as sp

###########################################
##### [ NORMAL DISTRIBUTION RELATED ] #####
###########################################

### sig lvl / probability -> z-score (left/right/two-tailed)

# left-tailed
def z_left(alpha):
    val = sp.stats.norm.ppf(alpha)
    return val                              # returns -z_alpha

# right-tailed
def z_right(alpha):
    val = sp.stats.norm.ppf(1 - alpha)
    return val                              # returns z_alpha

# two-tailed
def z_two(alpha):
    vals = sp.stats.norm.ppf([alpha/2, 1 - alpha/2])
    return vals                             # returns [-z_(alpha/2), z_(alpha/2)]

### z-score -> sig lvl / probability / alpha. notation: phi(z_alpha)
def z_to_prob(zscore):                  
    val = sp.stats.norm.cdf(zscore)
    return val                              # returns alpha (z_alpha -> alpha)

### calculating test statistic involving the normal distribution (sigma = pop stdev)
def z_test_stat(xbar, mean0, sigma, n):
    return (xbar - mean0) / ( sigma / m.sqrt(n))

######################################
##### [ T DISTRIBUTION RELATED ] #####
######################################

# crit lvl -> t-score (left/right/two-tailed)

# left-tailed
def t_left(alpha, df):
    val = sp.stats.t.ppf(alpha, df)
    return val                              # returns -t_(alpha, df)

# right-tailed
def t_right(alpha, df):
    val = sp.stats.t.ppf(1 - alpha, df)
    return val                              # returns t_(alpha, df)

# two-tailed
def t_two(alpha, df):
    vals = sp.stats.t.ppf([alpha/2, 1 - alpha/2], df)
    return vals                             # returns [-t_(alpha/2, df), t_(alpha/2, df)]

### calculating test statistic involving the t distribution (s = sample stdev)
### MIGHT MODIFY LATER TO HAVE IT TAKE IN A SAMPLE DATA ARRAY AND CALCULATE S FROM IT
def t_test_stat(xbar, mean0, s, n):
    return (xbar - mean0) / ( s / m.sqrt(n))

#############################################
##### [ POPULATION MEAN-RELATED TESTS ] #####
#############################################

### Power analysis for normal population hypothesis test with known stdev

# beta(mean2) for Ha: mean > mean0
def beta_mean_right(alpha, mean0, mean2, stdev, n):
    dist = (mean0 - mean2) / (stdev / m.sqrt(n))
    pos_z = z_right(alpha)
    return z_to_prob(pos_z + dist)
    
# beta(mean2) for Ha: mean < mean0
def beta_mean_left(alpha, mean0, mean2, stdev, n):
    dist = (mean0 - mean2) / (stdev / m.sqrt(n))
    neg_z = z_left(alpha)
    return 1 - z_to_prob(neg_z + dist)

# beta(mean2) for Ha: mean != mean0
def beta_mean_two(alpha, mean0, mean2, stdev, n):
    dist = (mean0 - mean2) / (stdev / m.sqrt(n))
    neg_z = z_two(alpha)[0]
    pos_z = z_two(alpha)[1]
    return z_to_prob(pos_z + dist) - z_to_prob(neg_z + dist)

### sample size n for which at level alpha one/two-tailed test has beta(mean2) = beta

def n_one_tailed(stdev, alpha, beta, mean0, mean2):
    z_alpha = z_right(alpha)
    z_beta = z_right(beta)
    thing = stdev * (z_alpha + z_beta) / (mean0 - mean2)
    return m.ceil(pow(thing, 2))

def n_two_tailed(stdev, alpha, beta, mean0, mean2):
    z_alpha = z_right(alpha/2)
    z_beta = z_right(beta)
    thing = stdev * (z_alpha + z_beta) / (mean0 - mean2)
    return m.ceil(pow(thing, 2))

###################################################
##### [ POPULATION PROPORTION-RELATED TESTS ] #####
###################################################

# beta(mean2) for Ha: mean > mean0
def beta_prop_right(alpha, p0, q0, p2, q2, n):
    pos_z = z_right(alpha)
    sq1 = 0
    sq2 = 0
    thing = (mean0 - mean2) / (stdev / m.sqrt(n))
    pos_z = z_right(alpha)
    return z_to_prob(pos_z + dist)
    
# beta(mean2) for Ha: mean < mean0
def beta_prop_left(alpha, mean0, mean2, stdev, n):

    return "1"

# beta(mean2) for Ha: mean != mean0
def beta_prop_two(alpha, mean0, mean2, stdev, n):
    return "1"













############################
##### [ TESTING AREA ] #####
############################

r = 5
sig = 0.01
z = -2.88








data = [15.0, 10, 10, 15, 25, 7, 3, 8, 10, 10, 11, 7, 5, 15, 7.5, 7.5, 12, 7, 10.5, 6, 10, 7.5]

avg = st.mean(data)
#print(avg)

stdev = st.stdev(data)
#print(stdev)

size = len(data)
#print(size)