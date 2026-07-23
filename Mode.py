from scipy import stats as st
import numpy as np

a = np.array([1,1,2,2,2,3,4,5])
res = st.mode(a)
print(res)