"""
1.Creating and Inspecting Data
Basics - Series, DataFrame, Reading, Inspecting

"""
#Part One Tasks
#1
import pandas as pd

df = pd.DataFrame({
    'Name': ['Ahmed', 'Sara', 'Mona', 'Ziad'],
    'Score': [92, 78, 90, 85]
})
print(df)

print('--------Seperate--------')

my_series=pd.Series(['Ahmed','Sara','Mona','Ziad'],index=[92,78,90,85])
print(my_series)

print('--------Seperate--------')
#-------------------------------
#2
my_series= pd.Series(0.5,index=["a", "b", "c", "d"])
print(my_series) 

print('--------Seperate--------')

#first 2 elements

print(my_series.head(2))

print('--------Seperate--------')

#By slicing
print(my_series[0:2])

print('--------Seperate--------')

#3
my_dict={
    'Name':["Nora", "Ali", "Laila"],
    'Age':[20,21,19],
    'Score':[90,80,95],
}
df=pd.DataFrame(my_dict)

#first 2 elements
print(df.head(2))

print('--------Seperate--------')
#column name
print(df.columns)
print('--------Seperate--------')
#shape of schedule
print(df.shape)
#----------------------------
#4
# creating a file
import os 
print(os.getcwd())
a_file=open(r"C:\Users\UnItEd\students.csv","w")
df = pd.DataFrame({
    'Name': ['Nora', 'Ali', 'Laila'],
    'Age': [20, 21, 19],
    'Score': [90, 80, 95]
})

# حفظ الملف
df.to_csv("students.csv", index=False)

# قراءته
read_df = pd.read_csv("students.csv")
print(read_df.head())
#---------------------------

print('--------Seperate--------')
#5
my_f= pd.DataFrame({'city':['cairo','Alex', 'Giza'],'Population':[9_500_000, 5_200_000, 4_000_000],'Density':[0,0,0]})
# مش عارفة اضيف عمود ازاى او صف هنا اوتاماتيكى
print(my_f)
print(my_f.columns)
print(my_f.index)
print('--------Seperate--------')
#-----------------------------
#6
# أنشئي Series تمثل كميات الفواكه بالمخزن:
# "Apple": 50, "Banana": 70, "Mango": 30

# المطلوب:
# - عرض السلسلة
# - استخراج عدد الموز فقط باستخدام index

my_series=pd.Series(['Apple','Banana','Mango'],index=[50,70,30])
print(my_series)
print('--------Seperate--------')
print(my_series.index)
print('--------Seperate--------')
print(my_series[1:2]) 
print('--------Seperate--------')
#------------------------------------
#7
data = {
    "Name": ["Alaa", "Omar", "Nour", "Hany"],
    "Math": [90, 85, 88, 92],
    "Science": [88, 90, 85, 95]
}

my_dict=pd.DataFrame(data)
print(my_dict)
print('--------Seperate--------')
print(my_dict.tail())
print('--------Seperate--------')
print(my_dict.shape)
print('--------Seperate--------')
print(my_dict.info())
print('--------Seperate--------')
print(my_dict['Math'][0:2])
print('--------Seperate--------')
#-----------------------------------
#1
dat={
    'Name':['NauRaa','Ali','Laila'],
    'Age':[20,21,19],
    'Score':[90,80,95],
}
my_d=pd.DataFrame(dat)
print(my_d)
print('--------Seperate--------')

my_new={'Name': "Sara", 'Age': 23, 'Score': 88}
my_pC=pd.concat([my_d,pd.DataFrame([my_new])],ignore_index=True)
print(my_pC)
print('--------Seperate--------')
#-----------------------------------
#2
my_series=pd.Series(['Nora','Ali','Laila'],index=[5,3,4])
my_series = pd.Series(['Nora', 'Ali', 'Laila'], index=[5, 3, 4])
new_series = pd.Series(['Sara'], index=[6])
result = pd.concat([my_series, new_series])
print(result)
print(result.sort_index())  
print(result.sort_values())  
print('--------Seperate--------')

#------------------------------------
#3
import numpy as np
my_dict={
  'Product': ['Pen', 'Book', 'Bag'],
  'Price': [5, 20, 100],
  'Quantity': [10, 3, 1]
}

arr1=np.array(my_dict['Price'])
print(arr1)
arr2=np.array(my_dict['Quantity'])
print(arr2)
total=arr1 * arr2
my_dict['Total'] = total
df = pd.DataFrame(my_dict)
print(df)
print('--------Seperate--------')

#--------------------------------
#6
data = {
    "Name": ["Alaa", "Omar", "Nour", "Hany"],
    "Math": [90, 85, 88, 92],
    "Science": [88, 90, 85, 95]
}
df=pd.DataFrame(data)
print(df)
df.to_csv('students_indexed.csv')
#-------------------------------
#7
print('--------Seperate--------')
print(df.loc[df['Name']=='Nour'])
print('--------Seperate--------')
my_series=pd.Series(data)
print(my_series)
#--------------------------------
#8
my_series=pd.Series(100,index=["x", "y", "z"])
print(my_series)
my_series[1]=150
print(my_series)
print('--------Seperate--------')
new_s=pd.Series(50,index=['x','y','z'])
t=pd.concat([my_series,new_s])
print(t)
print('--------Seperate--------')
#--------------------------------
#1
students={
    'Name':['NauRaa','Ali','Laila'],
    'Age':[20,21,15],
    'Grade':[90,80,95],
    'Gender':['female','male','female'],

}
#reading a file in data frame
df=pd.DataFrame(students)
df.to_csv('students.csv',index=False)
my_file=pd.read_csv('students.csv')
print(my_file.head())
print('--------Seperate--------')
#first 3 rows
print(my_file.head(2))
print('--------Seperate--------')
#students have ages > 18
print(my_file.loc[my_file['Age']>18])
print('--------Seperate--------')
#how many female in
print(my_file.loc[my_file['Gender']=='female'])
print('--------Seperate--------')
#---------------------------------
#2
data = {
    "Name": ["Ali", "Sara", "Omar", "Laila"],
    "Score": [88, 92, 75, 90],
    "Age": [22, 20, 23, 19]
}
df = pd.DataFrame(data)
print(df)
print('--------Seperate--------')
print(df.sort_values('Age'))
print('--------Seperate--------')
print(df.sort_index())
print('--------Seperate--------')
#-------------------------------
#3
#delete a column ('Age')
print(df.drop('Age',axis=1 ,inplace=False))
print('--------Seperate--------')
#delete a row 'Omar'
print(df.drop(2))
print('--------Seperate--------')
#4
#name as index
print(df.set_index('Name'))
print('--------Seperate--------')
#sara data
print(df.loc[df['Name']=='Sara'])
print('--------Seperate--------')
#last row
print(df.iloc[-1])
print('--------Seperate--------')
#edit value 'Score'
df.at[0,'Score']=95
print(df)
print('--------Seperate--------')
#------------------------------
#5
df_update=df.copy()
df_update['Score'] = df_update['Score'] + 5
print(df_update)
print('--------Seperate--------')
#------------------------------
#1
data_r={
   'Name':['Ali','Mona','Youssef','Rana','Omar'] ,
   'Age':[19,20,18,21,20],
   'Grade':[88,92,76,85,90],
   'City':['Cairo','Giza','Cairo','Alexandria','Giza'],

}
df=pd.DataFrame(data_r)
#first 2 rows
print(df.head(2))
print('--------Seperate--------')
#last 3 rows
print(df.tail(3))
print('--------Seperate--------')
#names of columns
print(df.columns)
print('--------Seperate--------')
print(df.info())
print(df)
print('--------Seperate--------')
#------------------------------
#2
#make name as index
print(df.set_index('Name'))
print('--------Seperate--------')
#rana Data
print(df.loc[df['Name']=='Rana'])
print('--------Seperate--------')
#students ages >19
print(df.loc[df['Age']>19])
print('--------Seperate--------')
df_between = df[(df['Grade'] > 80) & (df['Grade'] < 90)]
print(df_between)
print('--------Seperate--------')
#---------------------------
#3
#sorting Ages
print(df.sort_values('Age'))
print('--------Seperate--------')
#sorting grades
print(df.sort_values('Grade', ascending=False))
print('--------Seperate--------')
df.to_csv('students.csv',index=False)
my_file=pd.read_csv('students.csv')
print(my_file.head())
print('--------Seperate--------')
#------------------------------
#4
df['Passed'] = df['Grade'] >= 85  
print(df)
print('--------Seperate--------')
#------------------------------
#1
print('Hi##############3########3n')
students = {
    "Name": ["Nada", "Khaled", "Rana", "Ahmed", "Laila"],
    "Age": [19, 21, 20, 22, 18],
    "Grade": [88, 90, 75, 95, 84],
    "City": ["Cairo", "Alexandria", "Giza", "Cairo", "Giza"]
}

df = pd.DataFrame(students)
print('--------Seperate--------')
print(df)
print('--------Seperate--------')
print('--------Seperate--------')
print(df.head(2))
print('--------Seperate--------')
print(df.tail(3))
print('--------Seperate--------')
#columns
print(df.columns)
print('--------Seperate--------')
#rows 
print(df.index)
print('--------Seperate--------')
print(df.describe())
print('--------Seperate--------')
#------------------------------
#2
""""Accessing"""
#Reaching to specific column
print(df['Grade'])
print('--------Seperate--------')
#Raching to row data of ahmed
print(df.loc[df['Name']=='Ahmed'])
print('--------Seperate--------')
#Reacing to Grade of nada
print(df.loc[df['Name']=='Nada','Grade'])
print('--------Seperate--------')
#Row 3 By iloc
print(df.iloc[3])
print('--------Seperate--------')
#by loc
print(df.loc[3,])
print('--------Seperate--------')
#Data of laila
print(df.loc[df['Name']=='Laila'])
print('--------Seperate--------')
#-------------------------------------
#3
"""Modification"""
#Editing Age of ahmed
df.loc[df['Name']=='Ahmed','Age']=23
#for sure!
print(df.loc[df['Name']=='Ahmed','Age'])
print('--------Seperate--------')
#For Adding a column
df['Passed']=df['Grade']>=85
print(df.loc[df['Passed']])
#to sure 
print(df.loc[df['Name']=='Rana','Passed'])
print('--------Seperate--------')
#deleting city column
print(df.drop('City',axis=1))
print('--------Seperate--------')
#deleting data of rana row
print(df.loc[df['Name']=='Rana'].index)
print(df.drop(2,axis=0))
print('--------Seperate--------')
#------------------------------------
"""Sorting"""
#4
#تصاعديا
print(df.sort_values('Name',axis=0,ignore_index=False))
print('--------Seperate--------')
#تنازليا
print(df.sort_values('Name',axis=0,ascending=False,ignore_index=True))
print('--------Seperate--------')
#change the index to name
print(df.set_index('Name'))
print('--------Seperate--------')
#print(df.sort_index())
print(df.reset_index())
#------------------------------------
"""Filtering"""
#5 Students have degrees more than 85
print(df.loc[df['Grade']>85])
print('--------Seperate--------')
#students in giza
print(df.loc[df['City']=='Giza'])
print('--------Seperate--------')
# Ages >18 &  Degree <90
print(df.loc[(df['Age']>18) & (df['Grade']<90)] )
# student have 'a' in their name
print('--------Seperate--------')
#-------------------------------
"""Files"""
#6
df.to_csv('students.csv',index=False)
my_file=pd.read_csv('students.csv')
print(my_file.head(5))
print('--------Seperate--------')
#------------------------------
#تطبيق شامل 
new_line={'Name': "Omar", 'Age': 20, 'Grade': 91, 'City': "Cairo"}

connec_t=pd.concat([df,pd.DataFrame([new_line])],ignore_index=True)

df=connec_t.copy()
df['Passed']=df['Grade']>=85
print(df)
print('--------Seperate--------')
#-----------------------------
#1
employes={
    'Name':['NauRaa','Ahmed','Abbas'],
    'Department':['IT','Data scientist','Banking'],
    'Salary':[20000,15000,10000],
    'Experiences':[10,5,1],
}
df=pd.DataFrame(employes)
#Show 2 first row
print(df.head(2))
print('--------Seperate--------')
#show columns
print(df.columns)
#numbers of column & rows
print(df.columns.size)
print('--------Seperate--------')
print(df.index.size)
print('--------Seperate--------')
#Mean of salary for each empolyee
print(df['Salary'].mean())
print('--------Seperate--------')
#---------------------------------
#2
employes={
    "Name": ["Sara", "Mona", "Ali", "Ziad", "Nour"],
    "Age": [22, 24, 23, 25, 21],
    "Department": ["IT", "HR", "IT", "Marketing", "IT"],
    "Salary": [7000, 8000, 7500, 6000, 7200]
}
df=pd.DataFrame(employes)
#show employes in IT Department
print(df.loc[df['Department']=='IT','Name'])
print('--------Seperate--------')
#Show emplyes have salary more than 7000
print(df.loc[df['Salary']>7000,'Name'])
print('--------Seperate--------')
#Changing salary of ali
df.loc[df['Name']=='Ali','Salary']=7700
print(df)
print('--------Seperate--------')
#ترتيب تصاعدى حسب العمر
print(df.sort_values(by='Age',ascending=True))
print('--------Seperate--------')
#adding a new column 
df['Bonus']=df['Salary']*0.1
print(df)
print('--------Seperate--------')
#-----------------------------------
#3
my_dict={
    'Product':['Bag','Labtop','Table','TV'],
    'Category':['Clothes','Device','Home','Home'],
    'Price':[100,150,1000,20000],
    'Stock':[2,10,8,15],
}
df=pd.DataFrame(my_dict)
#show products have prices between 100,200
print(df.loc[(df['Price']>=100) & (df['Price']<=200)])
print('--------Seperate--------')
#show stocks less than 10
print(df.loc[df['Stock']<10])
print('--------Seperate--------')
#تنازليا حسب السعر
print(df.sort_values(by='Price',ascending=False))
print('--------Seperate--------')
#احسب المتوسط والسعر الأعلى والأقل لكل الأسعار.
print(df['Price'].mean())
print(df['Price'].min())
print(df['Price'].max())
print('--------Seperate--------')
#---------------------------------
#4
students={
    "Student": ["Amina", "Ahmed", "Khaled", "Nada", "Hussein"],
    "Math": [90, 70, 85, 60, 95],
    "English": [80, 60, 75, 65, 88],
    "Passed": [True, False, True, False, True]
}
df=pd.DataFrame(students)
#for knowing how many subjects
print(df.columns)
print('--------Seperate--------')
print(df['Math'].mean())
print(df['English'].mean())
print('--------Seperate--------')
#show only passed students
print(df.loc[df['Passed']==True,'Student'])
print('--------Seperate--------')
df['Total']=(df['Math']) + (df['English'])
print(df)
print('--------Seperate--------')
#تصاعديا
print(df.sort_values(by='Total',ascending=False))
print('--------Seperate--------')
#---------------------------------
#5
my_dict={
    'City':['Alex','Tanta','Cairo'],
    'Population':[10042521421,50000,3543455164121],
    'Area':[50,50,70],
    'Region':[10,20,0],
}
df=pd.DataFrame(my_dict)
#show City have pop more than 500*10**3
print(df.loc[df['Population']>500000, 'City'])
print('--------Seperate--------')
#احسب الكثافة السكانية = Population / Area، وأضفها كعمود جديد.
df['Th']=(df['Population'])/(df['Area'])
print(df)
print('--------Seperate--------')

#------------------------------
"""Part Two
Filtering / Subsetting , 
Sortiing ,
Missing Data ,
Grouping and Aggregation,
Datetime Handling,
Pivot Table & Crosstab,
Map / Apply / Lambda
Merging / Joining / Concatination

"""
# Part Two Tasks
#1
employees={
    "Name": ["Omar", "Nada", "Khaled", "Rana", "Ahmed", "Sara"],
    "Age": [28, 35, 40, 22, 30, 27],
    "Salary": [5000, 8000, 12000, 4000, 9000, 7500],
    "Department": ["IT", "HR", "IT", "Marketing", "IT", "HR"]
}
df=pd.DataFrame(employees)
print(df.loc[df['Age']>30,'Name'])
print('--------Seperate--------')
cond=df.loc[(df['Age']>30) & (df['Salary']>7000)]
print(cond)
print('--------Seperate--------')
#By Query
print(df.query('Age>30 and Salary>7000'))
print('--------Seperate--------')
#employees in IT and HR
print(df.loc[(df['Department']=='IT') | (df['Department']=='HR')])
print('--------Seperate--------')
#----------------------------------
#2
#تصاعديـا حسب العمر
print(df.sort_values(by='Age'))
print('--------Seperate--------')
#تنازليـا حسب الراتب 
print(df.sort_values(by='Salary' ,ascending=False))
print('--------Seperate--------')
print(df.sort_values(['Age','Salary'],ascending=[True,False]))
print('--------Seperate--------')
#---------------------------------
#3
test_d={
    "Name": ["Ali", "Hala", "Tamer", "Mona", None],
    "Age": [25, None, 35, 29, 40],
    "Salary": [7000, 8500, None, 6000, 9000]
}

df=pd.DataFrame(test_d)
#Missing Values pos..
print(df.isnull())
print('--------Seperate--------')
#deleting null values
print(df.dropna())
print('--------Seperate--------')
#filling null with Ages mean()
print(df.fillna(df['Age'].mean()))
print('--------Seperate--------')
#filling with zero
print(df.fillna(0))
print('--------Seperate--------')
#---------------------------------
#4 According to 1 

employees={
    "Name": ["Omar", "Nada", "Khaled", "Rana", "Ahmed", "Sara"],
    "Age": [28, 35, 40, 22, 30, 27],
    "Salary": [5000, 8000, 12000, 4000, 9000, 7500],
    "Department": ["IT", "HR", "IT", "Marketing", "IT", "HR"]
}
df=pd.DataFrame(employees)
#counting departments
print(df['Department'].unique().size)
print('--------Seperate--------')
# mean salary for each department
print(df.groupby('Department')['Salary'].mean())
print('--------Seperate--------')
#sum of salary and mean of ages
print(df.groupby(['Salary','Age']).aggregate({'Salary':'sum','Age':'mean'}))
print('--------Seperate--------')
#counting employees for each department
print(df.groupby('Department').size())
print('--------Seperate--------')
#--------------------------------------
#5
customers={
    "OrderID": [1, 2, 3, 4, 5],
    "OrderDate": ["2025-01-15", "2025-02-10", "2025-02-15", "2025-03-01", "2025-03-12"],
    "Amount": [250, 450, 300, 500, 150]
}

df=pd.DataFrame(customers)
df['OrderDate']=pd.to_datetime(df['OrderDate'])
#هو مش كدا معناه انى بحط عمود جديد ولا هيعدل بس
print(df)
print('--------Seperate--------')
#Adding year,month,day name columns
df['Year']=df['OrderDate'].dt.year
df['Month']=df['OrderDate'].dt.month
df['Weekday']=df['OrderDate'].dt.day_name()
print(df)
print('--------Seperate--------')
#orders in feb month
print(df.loc[df['Month']==2,'OrderID']) 
print('--------Seperate--------')
print(df.groupby('Month')['Amount'].sum())
print('--------Seperate--------')
#------------------------------------
#1
employees = {
    "Name": ["Omar", "Nada", "Khaled", "Rana", "Ahmed", "Sara"],
    "Age": [28, 35, 40, 22, 30, 27],
    "Salary": [5000, 8000, 12000, 4000, 9000, 7500],
    "Department": ["IT", "HR", "IT", "Marketing", "IT", "HR"]
}
df = pd.DataFrame(employees)
#employees older than 30
print(df.loc[df['Age']>30])
print('--------Seperate--------')
#employees older than 30 and salary
#by query
print(df.query('Age >30 and Salary >7000'))
print('--------Seperate--------')
#by & sign
print(df.loc[(df['Age']>30) & (df['Salary']>7000),'Name'])
print('--------Seperate--------')
#employees in HR and IT
print(df.loc[df['Department'].isin(['IT', 'HR']), 'Name'])
print('--------Seperate--------')
#employees not in HR
print(df.loc[df['Department']!='HR','Name'])
print('--------Seperate--------')
#--------------------------------
#2
#تصاعديا 
print(df.sort_values(by='Age'))
#تنازليا
print(df.sort_values(by='Salary',ascending=False))
print('--------Seperate--------')
print(df.sort_values(by=['Age','Salary'],ascending=[True,False]))
print('--------Seperate--------')
#----------------------------------
#3
test_d = {
    "Name": ["Ali", "Hala", "Tamer", "Mona", None],
    "Age": [25, None, 35, 29, 40],
    "Salary": [7000, 8500, None, 6000, 9000]
}
df = pd.DataFrame(test_d)
#missing values pos..
print(df.isnull())
print('--------Seperate--------')
#deleting null rows
print(df.dropna())
print('--------Seperate--------')
#fill with mean()
print(df.fillna(df['Age'].mean()))
print('--------Seperate--------')
#fill with zero
print(df.fillna(0))
print('--------Seperate--------')
#--------------------------------
#4
employees = {
    "Name": ["Omar", "Nada", "Khaled", "Rana", "Ahmed", "Sara"],
    "Age": [28, 35, 40, 22, 30, 27],
    "Salary": [5000, 8000, 12000, 4000, 9000, 7500],
    "Department": ["IT", "HR", "IT", "Marketing", "IT", "HR"]
}
df = pd.DataFrame(employees)
print(df.groupby('Department')['Salary'].mean())
print('--------Seperate--------')
#employees in every section
print(df.groupby('Department').size())
print('--------Seperate--------')
# highest salary
print(df.groupby('Department')['Salary'].max())
print('--------Seperate--------')
# sum and mean
print(df.groupby(['Department','Age']).aggregate({'Salary':'sum','Age':'mean'}))
print('--------Seperate--------')
#----------------------------------
#5
orders = {
    "OrderID": [1, 2, 3, 4, 5],
    "OrderDate": ["2025-01-15", "2025-02-10", "2025-02-15", "2025-03-01", "2025-03-12"],
    "Amount": [250, 450, 300, 500, 150]
}
df = pd.DataFrame(orders)
df['OrderDate']=pd.to_datetime(df['OrderDate'])
print(df)
print('--------Seperate--------')
df['Year']=pd.to_datetime(df['OrderDate']).dt.year
df['Month']=pd.to_datetime(df['OrderDate']).dt.month
df['Weekday']=pd.to_datetime(df['OrderDate']).dt.day_name()
print('--------Seperate--------')
print(df)
#----------------------------------
print(df.loc[df['Month']==2,'OrderID'])
print('--------Seperate--------')
print(df.groupby('Month')['Amount'].sum())
print('--------Seperate--------')
#----------------------------------
#6
sales = {
    "Department": ["IT", "HR", "IT", "Marketing", "IT", "HR"],
    "Gender": ["Male", "Female", "Male", "Female", "Female", "Male"],
    "Salary": [5000, 8000, 12000, 4000, 9000, 7500]
}
df = pd.DataFrame(sales)
print(pd.pivot_table(df,values='Salary',index='Department',columns='Gender',aggfunc='mean'))
print('--------Seperate--------')

df_a = {
    "ID": [1, 2, 3],
    "Name": ["Omar", "Nada", "Khaled"]
}
df_b = {
    "ID": [1, 2, 4],
    "Salary": [5000, 8000, 6000]
}
df1 = pd.DataFrame(df_a)
df2 = pd.DataFrame(df_b)
print(pd.merge(df1,df2,on='ID',how='inner'))
print('--------Seperate--------')
print(pd.merge(df1,df2,on='ID',how='left'))
print('--------Seperate--------')
print(pd.concat([df1,df2],axis=1)) 
print('--------Seperate--------')
#----------------------------------
# 1 - Filtering
students = {
    'Name': ['Naura', 'Omar', 'Ali'],
    'Age': [30, 20, 22],
    'Grade': [100, 90, 70],
    'City': ['Tanta', 'Alex', 'Giza']
}
df = pd.DataFrame(students)

print(df.query('Age > 20 and Grade > 80'))
print(df.query('City == "Alex" or City == "Cairo"'))
print(df.loc[df['City'] != 'Giza'])
print(df.query('Age > 18 and Age < 25'))
print('--------Seperate--------')

# 2 - Sorting
df = pd.DataFrame(employees)
print(df.sort_values(by='Salary'))
print(df.sort_values(by=['Age', 'Salary'], ascending=[False, True]))
print('--------Seperate--------')

# 3 - Missing values
products = {
    'Product': ['Mobile', 'Laptop', 'TV'],
    'Price': [1000, None, 1500],
    'Quantity': [1, 5, None],
}
df = pd.DataFrame(products)
print(df.isnull())
print(df.dropna())
print(df.fillna(df['Price'].mean()))
print(df.fillna(0))
print('--------Seperate--------')

# 4 - Grouping
sales = {
    'Seller': ['Ahmed', 'Ali', 'Amr'],
    'Region': ['Tanta', 'Cairo', 'Giza'],
    'Sales': [20000, 5000, 90000],
}
df = pd.DataFrame(sales)
print(df.groupby('Seller')['Sales'].sum())
print(df.groupby('Region')['Sales'].mean())
print(df.groupby('Seller')['Sales'].max())
print('--------Seperate--------')

# 5 - DateTime
df = pd.DataFrame(orders)
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Y'] = df['OrderDate'].dt.year
df['M'] = df['OrderDate'].dt.month_name()
df['D'] = df['OrderDate'].dt.day_name()
print(df)
print('--------Seperate--------')

# 6 - Pivot & Crosstab
employes = {
    'Department': ['IT', 'HR', 'IT'],
    'Gender': ['Female', 'Female', 'Male'],
    'Salary': [10000, 12000, 11000]
}
df = pd.DataFrame(employes)
print(pd.pivot_table(df, values='Salary', index='Department', columns='Gender', aggfunc='mean'))
print(pd.crosstab(df['Department'], df['Gender']))
print('--------Seperate--------')

# 7 - Map / Apply / Lambda
data = {
    'City': ['Cairo', 'Alex', 'Giza'],
    'Price': [1000, 2000, 1500]
}
df = pd.DataFrame(data)
df['Price_in_K'] = df['Price'].apply(lambda x: x/1000)
city_map = {'Cairo': 1, 'Alex': 2, 'Giza': 3}
df['City_Code'] = df['City'].map(city_map)
df['City_Len'] = df['City'].apply(len)
print(df)
print('--------Seperate--------')

# 8 - Merge / Concat
df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Omar", "Nada", "Khaled"]})
df2 = pd.DataFrame({"ID": [1, 2, 4], "Salary": [5000, 8000, 6000]})
print(pd.merge(df1, df2, on='ID', how='inner'))
print(pd.concat([df1, df2], axis=1))
print('--------Seperate--------')
#-----------------------------------
"""Advanced Pandas"""
#1
my_dict={
  'Country':['Egypt','America','Greece'],
  'City':['Cairo','California','Tanta'],
  'Population':[100000000,5000000,100000],
  'Area':[1,5,6],
}
df=pd.DataFrame(my_dict)
print(df.set_index(['City','Country']))
print('--------Seperate--------')
print(df.loc[df['City']=='California'])
print(df.reset_index())
print('--------Seperate--------')
#----------------------------------
#2
products={
    'Product':['Mobile','Labtop','Watch'],
    'Month':['March',"April",'August'],
    'Sales':[5212,50255,12000]
}
df= pd.DataFrame(products)
print(pd.pivot(df,values='Sales',columns='Product',index='Month'))
print('--------Seperate--------')
print(pd.pivot_table(df,values='Sales',index='Month',columns='Product').mean())
print('--------Seperate--------')
print(pd.pivot_table(df,values='Sales',index='Month',columns='Product',aggfunc='mean').dropna())
print('--------Seperate--------')
print(pd.melt(df,id_vars='Month',value_vars=['Product','Sales'],ignore_index=True))
print('--------Seperate--------')
#-------------------------------------
#3
orders = {
    "OrderID": [1, 2, 3, 4, 5],
    "OrderDate": ["2025-01-15", "2025-02-10", "2025-02-15", "2025-03-01", "2025-03-12"],
    "Amount": [250, 450, 300, 500, 150]
}

df=pd.DataFrame(orders)
df['OrderDate']=pd.to_datetime(df['OrderDate'])
df['Year']=df['OrderDate'].dt.year
df['Month']=df['OrderDate'].dt.month_name()
df['Weekday']=df['OrderDate'].dt.day_name()
print(df.resample('M',on='OrderDate').sum())
print('--------Seperate--------')
print(df['Amount'].rolling(window=3).mean().dropna())
print('--------Seperate--------')
#-------------------------------------
#4
df_a = {
    "ID": [1, 2, 3],
    "Name": ["Omar", "Nada", "Khaled"]
}
df_b = {
    "ID": [1, 2, 4],
    "Salary": [5000, 8000, 6000]
}
df1 = pd.DataFrame(df_a)
df2 = pd.DataFrame(df_b)
print(pd.merge(df1,df2,on='ID',how='inner'))
print('--------Seperate--------')
print(pd.concat([df1,df2],ignore_index=True,axis=1))
print('--------Seperate--------')
df=pd.merge(df1,df2,on='ID',how='outer')
print(df)
print('--------Seperate--------')
#---------------------------------------
#5
print(df.isnull())
print('--------Seperate--------')
print(df.fillna(df['Salary'].mean()))
print('--------Seperate--------')
print(df.dropna())
print('--------Seperate--------')
#--------------------------------------
#1
my_dict={
  'Country':['Egypt','America','Greece'],
  'City':['Cairo','California','Tanta'],
  'Population':[100000000,5000000,100000],
  'Area':[1,5,6],
}
df=pd.DataFrame(my_dict)
print(df.set_index(['Country','City']))
#searching for city in country
print(df.loc[df['City']=='Cairo'])
#take it back 
print(df.reset_index())
print('--------Seperate--------')
#---------------------------------------
#2
products={
    'Product':['Mobile','Labtop','Watch'],
    'Month':['March',"April",'August'],
    'Sales':[5212,50255,12000]
}
df=pd.DataFrame(products)
#make columns => product , rows => months and values is sales
print(pd.pivot(df,values='Sales',index='Month',columns='Product'))
#in the same table calculate the mean of values
print(pd.pivot_table(df,values='Sales',index='Month',columns='Product',aggfunc='mean'))
#make it same table to long table
print(pd.melt(df,id_vars='Month',value_vars=['Product','Sales'],ignore_index=True))
print('--------Seperate--------')
#---------------------------------------
#3
orders = {
    "OrderID": [1, 2, 3, 4, 5],
    "OrderDate": ["2025-01-15", "2025-02-10", "2025-02-15", "2025-03-01", "2025-03-12"],
    "Amount": [250, 450, 300, 500, 150]
}
df=pd.DataFrame(orders)
#convert string date to datetime
df['OrderDate']=pd.to_datetime(df['OrderDate'])
#adding year column
df['Year']=df['OrderDate'].dt.year
df['Month']=df['OrderDate'].dt.month
df['A Day']=df['OrderDate'].dt.day_name()
#collecting sales per month 
print(df.resample('M',on='OrderDate')['Amount'].sum())
#active mean for sales
print(df['Amount'].rolling(window=3).mean())
print('--------Seperate--------')
#---------------------------------------
#4
df_a = {
    "ID": [1, 2, 3],
    "Name": ["Omar", "Nada", "Khaled"]
}
df_b = {
    "ID": [1, 2, 4],
    "Salary": [5000, 8000, 6000]
}
df1 = pd.DataFrame(df_a)
df2 = pd.DataFrame(df_b)
#answer 1 with inner merging
print(pd.merge(df1,df2,on='ID',how='inner'))
print('--------Seperate--------')
#answer 2 with outer
print(pd.merge(df1,df2,on='ID',how='outer'))
print('--------Seperate--------')
#answer 3 with concatination 'Rows'
print(pd.concat([df1,df2],ignore_index=True,axis=0))
#answer 3 with concatination 'columns'
print(pd.concat([df1,df2],ignore_index=True,axis=1))
print('--------Seperate--------')
#---------------------------------------
#5
sales = {
    "Department": ["IT", "HR", "IT", "Marketing", "IT", "HR"],
    "Gender": ["Male", "Female", "Male", "Female", "Female", "Male"],
    "Salary": [5000, None, 12000, None, None, 7500]
}
df=pd.DataFrame(sales)
#fill empty values with mean of salary
print(df.fillna(df['Salary'].mean()))
#delete the rows which is empty
print(df.dropna())
print('--------Seperate--------')
#--------------------------------------
#6
City = ['Cairo', 'Alex', 'Giza'] 
city_map = {'Cairo':1, 'Alex':2, 'Giza':3}

df = pd.DataFrame({'City': City})
df['City_Code'] = df['City'].map(city_map)
print(df)
print('--------Seperate--------')

#---------------------------------------
"""General Pandas"""
#1
dataa = {
    'Country': ['Egypt', 'Egypt', 'USA', 'USA', 'Greece', 'Greece'],
    'City': ['Cairo', 'Alex', 'New York', 'Los Angeles', 'Athens', 'Santorini'],
    'Population': [20_000_000, 5_000_000, 8_000_000, 4_000_000, 700_000, 15_000],
    'Area': [606, 2679, 783, 1302, 39, 28]
}
df=pd.DataFrame(dataa)
#make country and city as indexs
print(df.set_index(['Country','City']))
print('--------Seperate--------')
#data of alex in egypt
d=df.set_index(['Country','City']) #Edit data in indpendent variable
print(d.loc[('Egypt','Alex')]) #Because its a multiindex
print('--------Seperate--------')
#reset basic schedule
print(df.reset_index())
print('--------Seperate--------')
#----------------------------------------
#2
sales = {
    'Product': ['Mobile', 'Mobile', 'Laptop', 'Laptop', 'Watch', 'Watch'],
    'Month': ['Jan', 'Feb', 'Jan', 'Feb', 'Jan', 'Feb'],
    'Sales': [5000, 7000, 8000, 6500, 1200, 1300]
}
df=pd.DataFrame(sales)
#make the rows=> Month , columns=>Product and value=> Sales
print(df.pivot(values='Sales',index='Month',columns='Product'))
print('--------Seperate--------')
#get a mean of sales 
print(df.pivot_table(values='Sales',index='Month',columns='Product',aggfunc='mean'))
print('--------Seperate--------')
#reshape with melt
print(pd.melt(df,id_vars='Month',value_vars=['Product','Sales']))
print('--------Seperate--------')
#-----------------------------------------
#3
orders = {
    'OrderID': [101, 102, 103, 104, 105, 106],
    'OrderDate': ['2025-01-05', '2025-01-20', '2025-02-14', '2025-02-25', '2025-03-10', '2025-03-15'],
    'Amount': [200, 300, 150, 400, 500, 250]
}
df=pd.DataFrame(orders)
#convert orderdate to datetime
df['OrderDate']=pd.to_datetime(df['OrderDate'])
#add year , month and day
df['Year']=df['OrderDate'].dt.year
df['Month']=df['OrderDate'].dt.month_name()
df['Weekday']=df['OrderDate'].dt.day_name()
print('--------Seperate--------')
#collect amounts monthly !
print(df.resample('M',on='OrderDate')['Amount'].sum())
print('--------Seperate--------')
#get the dynamic mean of amounts in 3 rows
print(df['Amount'].rolling(window=3).mean())
print('--------Seperate--------')
#------------------------------------------
#4
employees = {
    'ID': [1, 2, 3],
    'Name': ['Omar', 'Nada', 'Ali']
}

salaries = {
    'ID': [1, 2, 4],
    'Salary': [5000, 7000, 8000]
}
df1=pd.DataFrame(employees)
df2=pd.DataFrame(salaries)
#merging by inner values
print(pd.merge(df1,df2,on='ID',how='inner'))
print('--------Seperate--------')
#merging by outer values
print(pd.merge(df1,df2,on='ID',how='outer'))
print('--------Seperate--------')
#Concatination in columns
print(pd.concat([df1,df2],ignore_index=True,axis=1))
print('--------Seperate--------')
#Concatination in rows
print(pd.concat([df1,df2],ignore_index=True,axis=0))
print('--------Seperate--------')
#---------------------------------------
#5
dataa = {
    'Department': ['IT', 'HR', 'IT', 'Marketing', 'IT', 'HR'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
    'Salary': [5000, None, 12000, None, None, 7500]
}
df=pd.DataFrame(dataa)
#fill none values by salary mean 
print(df.fillna(df['Salary'].mean()))
print('--------Seperate--------')
#delete null rows!
print(df.dropna())
print('--------Seperate--------')
#by numeric
print(pd.to_numeric(df['Salary'],downcast='integer',errors='coerce'))
print('--------Seperate--------')
#----------------------------------------
#6
City = ['Cairo', 'Alex', 'Giza', 'Tanta']
city_map = {'Cairo': 1, 'Alex': 2, 'Giza': 3, 'Tanta': 4}

df=pd.DataFrame({'City':City})
print(df)
print('--------Seperate--------')
#add a column with map 
df['City_code']=df['City'].map(city_map)
print('--------Seperate--------')
df['Name_length']=df['City'].apply(lambda x: len(x))
print(df)
print('--------Seperate--------')
#--------------------------------------
#7
#describe
print(df.describe())
print('--------Seperate--------')
#value counts
print(df['City'].value_counts())
print('--------Seperate--------')
#corr
print(df[['City_code','Name_length']].corr())
print('--------Seperate--------')
print(df.memory_usage(deep=True))
df['City']=df['City'].astype('Category')
print('--------Seperate--------')
print(df.memory_usage(deep=True))
#---------------------------------------






































































































































































































































































































































































































































































































































































































































































































