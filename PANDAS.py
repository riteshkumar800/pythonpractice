# import pandas as pd


# # df=pd.read_csv("pandas_practice.csv", on_bad_lines='skip')|| encoding="UTF-8 OR latin1"

# # print(df)

# df = pd.read_excel("pandas_practice.xlsx")
# print(df)



##########################################################################################
# import pandas as pd

# data={
#     "Name":['Ram','Shayam','Ghanshayam'],
#     "Age":[10,20,30],
#     "City":['Nagpur', 'Mumbai','Delhi']
# }

# df=pd.DataFrame(data)
# print(df)


# # df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
# # df.to_json("output.json", index=False)

##########################################################################################


import pandas as pd
df=pd.read_excel("pandas_practice.xlsx")


print('Display 10 rows of first')
print(df.head())


print('Display 10 rows of last')
print(df.tail())


