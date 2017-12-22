from pprint import pprint

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('machine_library.csv')[1:]

results = {
    'total count': data.count(),
    'pages': data.pages.describe(),
    'duration': data.duration.describe(),
    'european': data.european.sum(),
    'north american': data.north_american.sum(),
    'asian': data.asian.sum(),
    'fiction': data.fiction.sum(),
    'non-fiction': data.nonfiction.sum(),
    'gender': data.author_gender.sum(),
}

pprint(results)
# {'asian': 4,
#  'duration': count     46.000000
# mean      17.391304
# std       25.590344
# min        0.000000
# 25%        2.000000
# 50%        8.000000
# 75%       21.750000
# max      122.000000
# Name: duration, dtype: float64,
#  'european': 18,
#  'fiction': 21,
#  'gender': 5,
#  'non-fiction': 16,
#  'north american': 24,
#  'pages': count     46.000000
# mean     240.826087
# std      147.711326
# min       33.000000
# 25%      144.250000
# 50%      213.000000
# 75%      292.500000
# max      854.000000
# Name: pages, dtype: float64,
#  'total count': five_star               46
# european                46
# north_american          46
# asian                   46
# other                   46
# author_gender           46
# avg_rating              46
# pages                   46
# org_publication_year    46
# duration                46
# favorite                46
# fiction                 46
# nonfiction              46
# contemporary            46
# philosophy              46
# politics                46
# religion                46
# science_tech_math       46
# short_story             46
# memoir                  46
# war_story               46
# historical              46
# dtype: int64}