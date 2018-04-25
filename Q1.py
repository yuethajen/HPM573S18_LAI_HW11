import numpy as np
import scr.MarkovClasses as MarkovCls

# part 1
all_causes_mortality = 18/1000
stroke_mortality = 36.2/100000
non_stroke_mortality = (all_causes_mortality*100000-36.2)/100000

rate_stroke_mortality = np.log(1-stroke_mortality)*-1
rate_non_stroke_mortality = np.log(1-non_stroke_mortality)*-1

print("Part 1")
print("Annual rate of stroke-associated mortality events:",rate_stroke_mortality)
print("Annual rate of background mortality events:",rate_non_stroke_mortality)

# part 2
first_stroke = 15/1000
rate_first_stroke = np.log(1-15/1000)*-1

print("")
print("Part 2")
print("Annual rate of first stroke:",rate_first_stroke)

# part 3
lambda1 = rate_first_stroke*0.9
lambda2 = rate_first_stroke*0.1

print("")
print("Part 3")
print("Annual rate of transition from well to stroke (lambda1):",lambda1)
print("Annual rate of transition from well to stroke death (lambda2):",lambda2)

# part 4
rate_recurrent_stroke = np.log(1-0.17)*(-1/5)

print("")
print("Part 4")
print("Annual rate of recurrent stroke",rate_recurrent_stroke)

# part 5
lambda3 = rate_recurrent_stroke*0.8
lambda4 = rate_recurrent_stroke*0.2

print("")
print("Part 5")
print("Annual rate of transition from post stroke to stroke (lambda3):",lambda3)
print("Annual rate of transition from post stroke to stroke death (lambda4):",lambda4)

# part 6
lambda5 = 1/(7/365)

print("")
print("Part 6")
print("Annual rate of transition from stroke to post-stroke (lambda5):",lambda5)

RATE_MATRIX = [
    [0, lambda1, 0, lambda2, rate_non_stroke_mortality],
    [0, 0, lambda5, 0, 0],
    [0, lambda3, 0, lambda4, rate_non_stroke_mortality],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print("")
print("Rate matrix for no therapy")
print(RATE_MATRIX[0])
print(RATE_MATRIX[1])
print(RATE_MATRIX[2])
print(RATE_MATRIX[3])
print(RATE_MATRIX[4])

DELTA_T = 0.25

print("")
print("DELTA_T =", DELTA_T)
print("")
print("Transform rate matrix to transition probability matrix")

TRANS_MATRIX = []
TRANS_MATRIX[:], S = MarkovCls.continuous_to_discrete(RATE_MATRIX, DELTA_T)
print(TRANS_MATRIX[0],",")
print(TRANS_MATRIX[1],",")
print(TRANS_MATRIX[2],",")
print(TRANS_MATRIX[3],",")
print(TRANS_MATRIX[4])
