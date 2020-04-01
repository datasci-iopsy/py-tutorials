person_list = ["Jonathan", "Cornessial", "male", True, 458]
person_list

# append values to a list
person_list.append(2018)
person_list

# print the last element of the person_list
person_list[-1]

person_dict = {
    "fname": "Jonathan",
    "lname": "Cornessial",
    "sex": "males",
    "bool_value": True,
    "twitter_followers": 458,
}
person_dict

# update the person_dict dictionary with a new date & add new followers
person_dict.update({"date": "2018-06", "twitter_followers": 500})
person_dict

# import the numpy library using an alias
# import numpy as np
from sklearn import datasets
import pandas as pd

boston_data = datasets.load_boston()
df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
df_boston["target"] = pd.Series(boston_data.target)

df_boston.head(10)

df_boston.shape

df_boston.describe()

df_boston.corr()
