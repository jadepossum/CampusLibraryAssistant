# from datetime import date, timedelta

# date1 = date.fromisoformat("2023-10-15")
# tdelta = timedelta(days=15)
# returndate = date1 + tdelta
# curdate = date.today()
# if(curdate > returndate):
#     print("fined ",(curdate - returndate).days," rupees as of today")
# else:
#     print("not fined until",returndate)

# import pandas as pd

# df1 = pd.read_excel(r"C:\Users\sai krishna\OneDrive\Desktop\TOTALBOOKS.xlsx")
# df2 = pd.read_excel(r"C:\Users\sai krishna\OneDrive\Desktop\Racks LisTMicrosoft Office Excel Worksheet.xlsx")


# print(df1.dropna(how="all").info())

# print(df2.info())
# df1.fillna({'Title':'-','Author':'-'},inplace=True)
# df2.dropna(subset=['Title'],inplace=True)
# df2.fillna({'Author':'-'},inplace=True)
# df1['Title'] = df1['Title'].map(lambda x:x.split('/')[0])
# df1['Title'] = df1['Title'].map(lambda x:x.strip().upper())
# df1['Author'] = df1['Author'].map(lambda x:x.strip().upper())
# df2['Title'] = df2['Title'].map(lambda x:x.strip().upper())
# df2['Author'] = df2['Author'].map(lambda x:x.strip().upper())
# print(df1.columns)
# print(df2.columns)
# df3=pd.merge(df1.iloc[:4068],df2,on=['Title','Author'],how="left")[['Dept','Title','Author','Location']]
# df3.to_excel("modifiedBooks.xlsx")
# print(df3.head())