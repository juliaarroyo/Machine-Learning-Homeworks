#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:23:13 2020

@author: juliaarroyo
"""
import pandas as pd

#training data
train_df = pd.read_csv('/Users/juliaarroyo/Downloads/Titanic/train.csv')
train_df1 = pd.DataFrame(train_df)

#testing data
test_df = pd.read_csv('/Users/juliaarroyo/Downloads/Titanic/test.csv')
test_df1 = pd.DataFrame(test_df)

#combined Data
combine = [train_df1, test_df1]
#print(combine)
combine1 = pd.concat([train_df1, test_df1])


#Printing values:
count = pd.DataFrame(train_df1.count(numeric_only=True),columns=['Counts'])
mean = pd.DataFrame(train_df1.mean(numeric_only=True),columns = ['Means'])
std = pd.DataFrame(train_df1.std(numeric_only=True),columns = ['St. Devs'])
min = pd.DataFrame(train_df1.min(numeric_only=True),columns = ['Mins'])
per25 = pd.DataFrame(train_df1.quantile(q=.25, numeric_only=True))
per50 = pd.DataFrame(train_df1.quantile(q=.5, numeric_only=True))
per75 = pd.DataFrame(train_df1.quantile(q=.75, numeric_only=True))
max = pd.DataFrame(train_df1.max(numeric_only=True),columns = ['Maxs'])

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print(pd.concat([count, mean, std, min, per25, per50, per75, max],axis=1))

#Printing values:
count1 = pd.DataFrame(test_df1.count(numeric_only=True),columns=['Counts'])
mean1 = pd.DataFrame(test_df1.mean(numeric_only=True),columns = ['Means'])
std1 = pd.DataFrame(test_df1.std(numeric_only=True),columns = ['St. Devs'])
min1 = pd.DataFrame(test_df1.min(numeric_only=True),columns = ['Mins'])
per251 = pd.DataFrame(test_df1.quantile(q=.25, numeric_only=True))
per501 = pd.DataFrame(test_df1.quantile(q=.5, numeric_only=True))
per751 = pd.DataFrame(test_df1.quantile(q=.75, numeric_only=True))
max1 = pd.DataFrame(test_df1.max(numeric_only=True),columns = ['Maxs'])

print(pd.concat([count1, mean1, std1, min1, per251, per501, per751, max1],axis=1))

#Printing values:
count2 = pd.DataFrame(combine1.count(numeric_only=True),columns=['Counts'])
mean2 = pd.DataFrame(combine1.mean(numeric_only=True),columns = ['Means'])
std2 = pd.DataFrame(combine1.std(numeric_only=True),columns = ['St. Devs'])
min2 = pd.DataFrame(combine1.min(numeric_only=True),columns = ['Mins'])
per252 = pd.DataFrame(combine1.quantile(q=.25, numeric_only=True))
per502 = pd.DataFrame(combine1.quantile(q=.5, numeric_only=True))
per752 = pd.DataFrame(combine1.quantile(q=.75, numeric_only=True))
max2 = pd.DataFrame(combine1.max(numeric_only=True),columns = ['Maxs'])

#print(combine1)
print(pd.concat([count2, mean2, std2, min2, per252, per502, per752, max2],axis=1))

x = train_df1.select_dtypes(include=[object])
#count
counts2= pd.DataFrame(x.count(),columns = ['Counts'])
#Unique values
unique = pd.DataFrame(x.nunique(),columns = ['Unique'])
#print('*********', counts2.select_dtypes(exclude = ['category']))
print(pd.concat([counts2, unique],axis=1))

y = test_df1.select_dtypes(include=[object])
#count
counts2= pd.DataFrame(y.count(),columns = ['Counts'])
#Unique values
unique = pd.DataFrame(y.nunique(),columns = ['Unique'])
#print('*********', counts2.select_dtypes(exclude = ['category']))
print(pd.concat([counts2, unique],axis=1))

z = combine1.select_dtypes(include=[object])
#count
counts2= pd.DataFrame(z.count(),columns = ['Counts'])
#Unique values
unique = pd.DataFrame(z.nunique(),columns = ['Unique'])
#print('*********', counts2.select_dtypes(exclude = ['category']))
print(pd.concat([counts2, unique],axis=1))


print('++++++++++++++++++++')

freq = train_df1.groupby(['Sex']).size()
max = freq.argmax()
most1 = freq.max()
print('Sex: ' ,max, most1)

freq2 = train_df1.groupby(['Name']).size()
#print(freq2)
most2 = freq2.max()

freq3 = train_df1.groupby(['Ticket']).size()
max = freq3.argmax()
most3 = freq3.max()
print('Ticket: ' ,max, most3)

freq4 = train_df1.groupby(['Cabin']).size()
max = freq4.argmax()
most4 = freq4.max()
print('Cabin: ' ,max, most4)

freq5 = train_df1.groupby(['Embarked']).size()
max = freq5.argmax()
most5 = freq5.max()
print('Embarked: ' ,max, most5)


print('++++++++++++++++++++')
freq = test_df1.groupby(['Sex']).size()
max = freq.argmax()
most1 = freq.max()
print('Sex: ' ,max, most1)

freq2 = test_df1.groupby(['Name']).size()
max = freq2.argmax()
most2 = freq2.max()
#print('Name: ' ,max, most2)

freq3 = test_df1.groupby(['Ticket']).size()
max = freq3.argmax()
most3 = freq3.max()
print('Ticket: ' ,max, most3)

freq4 = test_df1.groupby(['Cabin']).size()
max = freq4.argmax()
most4 = freq4.max()
print('Cabin: ' ,max, most4)

freq5 = test_df1.groupby(['Embarked']).size()
max = freq5.argmax()
most5 = freq5.max()
print('Embarked: ' ,max, most5)

print('++++++++++++++++++++')
freq = z.groupby(['Sex']).size()
max = freq.argmax()
most1 = freq.max()
print('Sex: ' ,max, most1)

freq2 = z.groupby(['Name']).size()
max = freq2.argmax()
most2 = freq2.max()
#print('Name: ' ,max, most2)

freq3 = z.groupby(['Ticket']).size()
max = freq3.argmax()
most3 = freq3.max()
print('Ticket: ' ,max, most3)

freq4 = z.groupby(['Cabin']).size()
max = freq4.argmax()
most4 = freq4.max()
print('Cabin: ' ,max, most4)

freq5 = z.groupby(['Embarked']).size()
max = freq5.argmax()
most5 = freq5.max()
print('Embarked: ' ,max, most5)


#sum of null values for each column
print("Test "     , test_df1.isnull().sum())
print("train "     , train_df1.isnull().sum())
print("combined ",    combine1.isnull().sum())


#print(count.info())