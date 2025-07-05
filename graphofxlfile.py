import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('university_students.csv')

age = df['Age']
gpa = df['GPA']

plt.bar(age, gpa)

plt.title('GPA vs Age')
plt.xlabel('Age')
plt.ylabel('GPA')

plt.show()
