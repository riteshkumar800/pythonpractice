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


# import pandas as pd
# df=pd.read_excel("pandas_practice.xlsx")


# # print('Display 10 rows of first')
# # print(df.head())


# # print('Display 10 rows of last')
# # print(df.tail())



# # print(df.info())

##########################################################################################

# import pandas as pd

# data={
#     "Name": ['Ram', 'Shayam', 'Ghanshayam', 'Dhanshayam', 'Aditi', 'Jagdish', 'Raj','Simran'],
#     "Age": [12, 34, 56, 78, 90, 23, 45,67],
#     "Salary":[500000,1000000,200000,30000,700000,40000,10000,30000],
#     "Performenced_scored":[89,69,78,67,68,6,9,45]
# }


# df=pd.DataFrame(data)
# # print(df)

# high_salary=df[df['Salary']>50000]
# print('Employee with salary>50000')
# print(high_salary)


# filtered=df[(df['Age']>30) & (df['Salary']>50000)]
# print('Employee Age>30 + Salary>50000')
# print(filtered)


# filtered_or=df[(df['Age']>30) | df['Performenced_scored']>90]
# print('Employee age greate than 30 or performanced_score>90')
# print(filtered_or)




