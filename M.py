# import matplotlib.pyplot as plt

# month = ['Jan', 'Feb', 'Mar' , 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
# sales = [150, 200, 180, 200, 250, 270, 300, 320, 280, 270, 300, 350]

# plt.plot(month, sales, marker='o', linesyle='-', color='b', lable='Sales')

# plt.title("Monthly Sales")
# plt.xlable("Month")
# plt.ylabel("Sales")

# plt.grid(False)
# plt.legend()
# plt.show()

import pandas as df
df.groupby('column').mean()
df.groupby(['col1',
            'col2']).agg({'col3':'sum'})
