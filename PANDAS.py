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


##########################################################################################


# import pandas as pd

# data={
#     "Name": ['Ram', 'Shayam', 'Ghanshayam', 'Dhanshayam', 'Aditi', 'Jagdish', 'Raj','Simran'],
#     "Age": [12, 34, 56, 78, 90, 23, 45,67],
#     "Salary":[500000,1000000,200000,30000,700000,40000,10000,30000],
#     "Performenced_scored":[89,69,78,67,68,6,9,45]
# }



# df=pd.DataFrame(data)
# print(df)


# df['Bonus']=df['Salary']*0.1
# print(df)


# df.insert(0,"Employee ID", [12,22,33,44,55,34,23,21])
# print(df)


# # print()


##########################################################################################

# import pandas as pd

# data={
#     "Name": ['Ram', 'Shayam', 'Ghanshayam', 'Dhanshayam', 'Aditi', 'Jagdish', 'Raj','Simran'],
#     "Age": [12, 34, 56, 78, 90, 23, 45,67],
#     "Salary":[500000,1000000,200000,30000,700000,40000,10000,30000],    
#     "Performenced_scored":[89,69,78,67,68,6,9,45]
# }


# df=pd.DataFrame(data)
# print(df)


# df.loc[0,'Salary']=5500
# print(df)

##########################################################################################

# import pandas as pd

# data={
#     "Name": ['Ram', 'Shayam', 'Ghanshayam', 'Dhanshayam', 'Aditi', 'Jagdish', 'Raj','Simran'],
#     "Age": [12, None, 56, 78, 90, 23, 45,67],
#     "Salary":[500000,1000000,200000,30000,700000,40000,10000,None],    
#     "Performenced_scored":[89,69,78,67,None,6,9,45]
# }

# df=pd.DataFrame(data)
# print(df)


# # print("Modified")

# # df.fillna(0,inplace=True)
# # print(df)


# df['Age'].fillna(df['Age'].mean(),inplace=True)
# df['Salary'].fillna(df['Salary'].mean(), inplace=True)
# print(df)

##########################################################################################

# import pandas as pd

# data={
#     "Time":[1,2,3,4,5],
#     "Value":[10,None,30,None,50]

# }


# df=pd.DataFrame(data)
# print("Bedore interpolation")
# print(df)


# df['Value']=df['Value'].interpolate(method="linear")
# print("After interpolatio")
# print(df)


##########################################################################################

# import pandas as pd

# data={
#     "Name=":['Arun', 'Varun','Karun'],
#     "Age":[28,22,32],
#     "Salary":[1000,20000,30000]
# }


# df=pd.DataFrame(data)
# df.sort_values(by="Age", ascending=False, inplace=True) #for single column
# df.sort_values(by=["Age","Salary"], ascending=[True,False], inplace=True) #for multiple column
# print("Sorted age by descending")
# print(df)

##########################################################################################


# import pandas as pd

# data={
#     "Name=":['Arun', 'Varun','Karun','Narun','Marun'],
#     "Age":[28,22,32,34,22],
#     "Salary":[1000,20000,30000,40000,530000]
# }


# df=pd.DataFrame(data)
# # grouped=df.groupby("Age")["Salary"].sum()

# grouped=df.groupby(["Age","Name"])["Salary"].sum()#for multiple
# print(grouped)


##########################################################################################


import pandas as pd

df_customers=pd.DataFrame({
    'Custumer_Id':[1,2,3],
    'Name':['Ramesh', 'Suresh', 'Namresh']
})


df_orders=pd.DataFrame({
    'Custumer_Id':[1,2,4],
    'OrderAmount':[250,350,542]
})

# df_merged=pd.merge(df_customers, df_orders, on="Custumer_Id", how="inner")
df_merged=pd.merge(df_customers, df_orders, on="Custumer_Id", how="outer")
df_merged=pd.merge(df_customers, df_orders, on="Custumer_Id", how="left")
df_merged=pd.merge(df_customers, df_orders, on="Custumer_Id", how="right")
print("INner join")
print(df_merged)











































