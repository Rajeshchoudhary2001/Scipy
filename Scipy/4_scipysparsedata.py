# What is sparse data: Sparse data is the data that has mostly unused elements. like the elements that dont carry any info. [1,0,2,0,4,5,6,9,2,4]
# Sparse Data: is a data set where most of the item values are zero.
# Dense Array: is the opposite of a sparse array: most of the values are not zero.
# sparse data example [1,0,2,0,0,3,0,0,0,0,0,4]
# Dense Array: [2,5,6,8,9,7,1,2,3,6]

'''How to Work With Sparse Data
SciPy has a module, scipy.sparse that provides functions to deal with sparse data.

There are primarily two types of sparse matrices that we use:

CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.

CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products

We will use the CSR matrix in this tutorial.

CSR Matrix
We can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix().'''


# Example
# Create a CSR matrix from an array:
from scipy.sparse import csr_matrix
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))


# output:
'''
  (0, 5)	1
  (0, 6)	1
  (0, 8)	2 '''

'''From the result we can see that there are 3 items with value.

The 1. item is in row 0 position 5 and has the value 1.

The 2. item is in row 0 position 6 and has the value 1.

The 3. item is in row 0 position 8 and has the value 2.'''


# Sparse Matrix Methods
# Viewing stored data (not the zero items) with the data property:

# Example
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)
# output [1 1 2]


# Counting nonzeros with the count_nonzero() method:
# Example
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).count_nonzero())
# output 3


# Removing zero-entries from the matrix with the eliminate_zeros() method:
# Example
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)
# output (1, 2)	1
#        (2, 0)	1
#        (2, 2)	2


# Eliminating duplicate entries with the sum_duplicates() method:
# Example
# Eliminating duplicates by adding them:
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)
# output    (1, 2)	1
#           (2, 0)	1
#           (2, 2)	2



# Converting from csr to csc with the tocsc() method:
# Example
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr = csr_matrix(arr).tocsc()
print(newarr)
# output:     (2, 0)	1
#             (1, 2)	1
#             (2, 2)	2