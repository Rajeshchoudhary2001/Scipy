# What is interpolation: it is a method for generating points between the given points. and the method of filling the values is called imputation.

# now how we can implement it in scipy.? -  via module scipy.interpolate
# 1D interpolation: interp1d()
# here for given xs and ys interpolate values from 2.1, 2.2, 2.3........2.9:
from scipy.interpolate import interp1d
import numpy as np
xs = np.arange(10)
ys = 2*xs + 1
interp_func = interp1d(xs, ys)
sharad = interp_func(np.arange(2.1, 3, 0.1))
print(sharad)
# output: [5.2  5.4  5.6  5.8  6.   6.2  6.4  6.6  6.8]



# spline interpolation:
# example: here now we will find the univariate spline interpolation for 2.1, 2.2, 2.3.....2.9 .

from scipy.interpolate import UnivariateSpline
import numpy as np
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs,ys)
sharad = interp_func(np.arange(2.1, 3, 0.1))

print(sharad)
# output: [5.62826474 6.03987348 6.47131994 6.92265019 7.3939103  7.88514634
#    8.39640439 8.92773053 9.47917082]



# Interpolation with Radial basis Function(RBF)

from scipy.interpolate import Rbf
import numpy as np
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs,ys)
sharad = interp_func(np.arange(2.1, 3, 0.1))

print(sharad)

# output:  [6.25748981  6.62190817  7.00310702  7.40121814  7.8161443   8.24773402
#    8.69590519  9.16070828  9.64233874]
 

