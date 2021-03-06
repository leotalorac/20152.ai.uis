import numpy as np
input_conv="""\
{'A': np.array([[1,2,1,2,1,2],[2,3,2,3,2,3],[4,3,4,3,4,3],[6,4,6,4,6,4],[7,5,7,5,7,5]]), 'f':np.array([[2,2,2],[2,2,2]])}
"""

output_conv="""\
[[ 22.  26.  22.  26.]
 [ 36.  36.  36.  36.]
 [ 54.  48.  54.  48.]
 [ 70.  62.  70.  62.]]
"""

input_csad="""\
{"A": np.array([[1,2,1,2,1,2],[2,3,2,3,2,3],[4,3,4,3,4,3],[6,4,6,4,6,4],[7,5,7,5,7,5]]), "f": np.array([[2,2,2],[2,2,2]])}
{"A": np.array([[1,2,1,2,1,2],[2,3,2,9,2,3],[4,-1,4,3,4,3],[6,4,6,4,0,4],[1,5,7,5,7,5]]), "f": np.array([[2,3,1],[3,2,1]])}
"""

output_csad="""\
[[  3.   3.   3.   3.]
 [  6.   6.   6.   6.]
 [ 15.  12.  15.  12.]
 [ 23.  19.  23.  19.]]
[[  5.  11.  11.  11.]
 [  8.  18.  12.  14.]
 [ 19.  14.  11.  10.]
 [ 21.  19.  19.  19.]]
"""

input_msad="""\
{"A": np.array([[5,12,1,2,4,6],[6, 5,2,3,2,1]]), "f": np.array([[2,2],[2,2]])}
{"A": np.array([[5,11,13,2,4,6],[6,5,2,3,2,11], [6,5,2,3,1,11]]), "f": np.array([[2,2],[2,2], [0,1]])}
"""

output_msad="""\
2
3
"""

input_imsad="""\
{"A": np.array([[1, 2, 1, 2, 1, 2], [2, 3, 1, 3, 2, 3], [4, 3, 4, 3, 4, 3], [6, 4, 6, 4, 1, 4], [7, 5, 2, 5, 7, 5]]), "B": np.array([[ 1,  4,  1,  4,  1,  4], [ 4,  9,  1,  9,  4,  9], [16,  9, 16,  9, 16,  9], [36, 16, 36, 16,  1, 16], [49, 25,  4, 25, 49, 25]]), "k":2, "r":2, "c":3 }
{"A": np.array([[1, 2, 1, 2, 1, 2], [2, 3, 1, 3, 2, 3], [4, 3, 4, 3, 4, 3], [6, 4, 6, 4, 1, 4], [7, 5, 2, 5, 7, 5]]),"B": np.array([[6,5,6,5,6,5], [5,4,6,4,5,4], [3,4,3,4,3,4], [1,3,1,3,6,3], [0,2,5,2,0,2]]),  "k":2, "r":2, "c":3 }
{"A": np.array([[1, 2, 1, 2, 1, 2], [2, 3, 1, 3, 2, 3], [4, 3, 4, 3, 4, 3], [6, 4, 6, 4, 1, 4], [7, 5, 2, 5, 7, 5]]),"B": np.array([[6,5,6,5,6,5], [5,4,6,4,5,4], [3,4,3,4,3,4], [1,3,1,3,6,3], [0,2,5,2,0,2]]),  "k":2, "r":1, "c":3 }
"""

output_imsad="""\
3
1
0
"""

input_smatrix="""\
{"A": np.array([[1,2,1,2,1,2],[2,3,1,3,2,3],[4,3,4,3,4,3],[6,4,6,4,1,4],[7,5,2,5,7,5]]), "B": np.array([[ 1,  4,  1,  4,  1,  4], [ 4,  9,  1,  9,  4,  9], [16,  9, 16,  9, 16,  9], [36, 16, 36, 16,  1, 16], [49, 25,  4, 25, 49, 25]]), "k": 2}

{"A": np.array([[1,2,1,2,1,2],[2,3,1,3,2,3],[4,3,4,3,4,3],[6,4,6,4,1,4],[7,5,2,5,7,5]]), "B": np.array([[6, 5, 6, 5, 6, 5], [5, 4, 6, 4, 5, 4], [3, 4, 3, 4, 3, 4], [1, 3, 1, 3, 6, 3], [0, 2, 5, 2, 0, 2]]), "k":2}
"""

output_smatrix="""\
[[ 2.  0.  0.  2.  2.]
 [ 2.  0.  0.  2.  2.]
 [ 3.  3.  1.  0.  0.]
 [ 1.  0.  0.  1.  3.]]
[[ 0.  1.  2.  3.  4.]
 [ 3.  1.  1.  3.  1.]
 [ 4.  2.  2.  2.  4.]
 [ 1.  1.  1.  2.  2.]]
"""


from checks import *
max_score = 5
score     = 0
score += check_function(convolution, input_conv, output_conv) if "convolution" in locals() else 0
score += check_function(convolution_sad, input_csad, output_csad) if "convolution_sad" in locals() else 0
score += check_function(min_sad, input_msad, output_msad) if "min_sad" in locals() else 0
score += check_function(index_min_sad_in_band, input_imsad, output_imsad) if "index_min_sad_in_band" in locals() else 0
score += check_function(min_sad_matrix, input_smatrix, output_smatrix) if "min_sad_matrix" in locals() else 0




print "---"
print "calificacion: %d/%d (%.0f"%(score, max_score, score*100/max_score)+"%)"

