import csv
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({'title':'', 'date_read': '', 'date_added':'', 'total_pages':0, 'my_rating':0}, index=[0])

with open('library_export.csv', newline='') as csvfile:
    read = csv.reader(csvfile, delimiter=',')
    for row in read:
        #print(row)

        prior_row = data.total_pages[data.shape[0]-1]
        r = dt.time.strptime(row[12], "%m/%d/%y")
        a = dt.time.strptime(row[13], "%m/%d/%y")
        #duration = int(r) - int(a)
        #print(duration)
        data = data.append([{'title':row[1], 'date_read': row[12], 'date_added':row[13], 'total_pages':int(row[9])+int(prior_row), 'my_rating': int(row[7])}], ignore_index=True)

    #print(data)
    data.plot(x='date_read',y='total_pages',title='Total pages read since Oct. 2015')
    data.plot.bar(x='date_read',y='my_rating')
    #print(data.mean())
    plt.show()
