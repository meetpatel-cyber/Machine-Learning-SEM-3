#Convert Categorical data into Numeric using Label Encoder
'''
from sklearn.preprocessing import LabelEncoder

categorical_feature = ['cat','dog','dog','cat','bird']

encoder = LabelEncoder()

encoded_feature = encoder.fit_transform(categorical_feature)

print("Encoded feature:",encoded_feature)
'''
#########################################################################

#Convert Categorical data into Numeric using One-Hot Encoder

import numpy as np
from sklearn.preprocessing import OneHotEncoder

categorical_feature = ['cat','dog','dog','cat','bird']

categorical_feature = np.array(categorical_feature).reshape(-1,1)

encoder = OneHotEncoder(sparse_output=False)

encoded_feature = encoder.fit_transform(categorical_feature)

print("Encoded feature:",encoded_feature)
