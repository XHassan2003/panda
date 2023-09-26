import pandas as pd

data = {
    'Country': ['Pakistan', 'India', 'China', 'Germany', 'United Kingdom', 'Canada', 'France'],
    'Population': [231.4, 1408, 1412, 83.2, 67.33, 38.25, 67.75],
    'Area': [796095, 3287, 9597, 357588, 243610, 9985, 551695],
    'GDP': [348.3, 3.176, 17.73, 4.26, 3.131, 1.988, 2.958],
    'Capitals': ['Islamabad', 'New Delhi', 'Beijing', 'Berlin', 'London', 'Ottawa', 'Paris']
}

df = pd.DataFrame(data)
print("This is raw data:\n")
print(df, "\n")

df['Density'] = df['Population'] / (df['Area'] / 1000000)
print("This is the changed data after a new column 'Density' is added:\n")
print(df, "\n")

p_table = pd.pivot_table(df, index=['Capitals'], values=['Population', 'Area', 'GDP'], aggfunc='mean')
print("Data sorted according to the Capitals, all values in these columns are mean values:\n")
print(p_table)
