import pandas as  pd
import matplotlib.pyplot as mplt

df = pd.read_csv('university_students.csv')

df['Credits completed'] = [90,80,88,70,95,86,92,89,67,75]

grouped = df.groupby('Program')['Credits completed'].sum()

mplt.bar(grouped.index, grouped.values)

mplt.title('Credits completed by proram')
mplt.xlabel('Program')
mplt.ylabel('credits completed')

mplt.show()