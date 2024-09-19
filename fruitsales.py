import pandas as pd

#Create DataFrame
fruit_sales = pd.DataFrame([[35, 21], [41, 34]],
                           columns=['Apples', 'Bananas'],
                           index=['2017 Sales', '2018 Sales'])


#Write DataFrame to csv file
fruit_sales.to_csv("fruit.csv")

print("DataFrame has been written to fruit.csv")

