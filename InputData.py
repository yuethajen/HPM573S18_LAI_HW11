

POP_SIZE = 20000    # cohort population size
SIM_LENGTH = 15   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 0.25       # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

ADD_BACKGROUND_MORT = False

# transform rate matrix to probability matrix (no therapy)
TRANS_MATRIX = [
[0.99180649104955032, 0.003386618110301446, 0.0, 0.00037629090114460511, 0.0044305999390036287] ,
[0.0, 2.1810278843297655e-06, 0.9999978189721157, 0.0, 0.0] ,
[0.0, 0.0074021199352473045, 0.9863289792342923, 0.0018505299838118261, 0.0044183708466485677] ,
[0, 0, 0, 1.0, 0] ,
[0, 0, 0, 0, 1.0]
]

# transform rate matrix to probability matrix (anticoagulation therapy)
TRANS_MATRIX_ANTICOAG = [
[0.99180649104955032, 0.003386618110301446, 0.0, 0.00037629090114460511, 0.0044305999390036287] ,
[0.0, 2.1810278843297655e-06, 0.9999978189721157, 0.0, 0.0] ,
[0.0, 0.0055564950899793198, 0.98807645690545287, 0.0019447732814927619, 0.0044222747230750455] ,
[0, 0, 0, 1.0, 0] ,
[0, 0, 0, 0, 1.0]
]


HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke ONLY WHEN THE CYCLE LENGTH IS 1 YEAR
    0.9,  # post-stroke
    0,  # stroke death
    0  # dead
]

HEALTH_COST = [
    0,   # well
    5000,  # stroke
    200,  # post-stroke /year
    0,  # stroke death
    0   # dead
]

HEALTH_COST_ANTICOAG = [
    0,    # well
    5000,  # stroke
    750,  # post-stroke /year
    0,  # stroke death
    0  # dead
]



