
# Data Analysis on Heroes of Pymoli
----
## Conclusion


> Data analysis was performed on "Heroes of Pymoli" data set (purchase_data.json, purchase_data2.json) and following observations were made:

----
### Trend 1:
Percentage of female buyers are way less than males. It may be a good idea to focus on activities in game that are targeted towards female audience 

| Gender Demographics   | Percentage of Players | Total Count | 
|-----------------------|-----------------------|-------------| 
| Female                | 17.45%                | 100         | 
| Male                  | 81.15%                | 465         | 
| Other / Non-Disclosed | 1.40%                 | 8           | 


----
### Trend 2:
Older people of 40+ age are not buying as much and its probably due to marketing towards one set of group. That strategy needs to be evaluated.


| Age Demographics | Percentage of Players | Total Count | 
|------------------|-----------------------|-------------| 
| <10              | 3.32%                 | 19          | 
| 14-Oct           | 4.01%                 | 23          | 
| 15-19            | 17.45%                | 100         | 
| 20-24            | 45.20%                | 259         | 
| 25-29            | 15.18%                | 87          | 
| 30-34            | 8.20%                 | 47          | 
| 35-39            | 4.71%                 | 27          | 
| 40+              | 1.92%                 | 11          | 





----
### Trend 3:
'Betrayal, Whisper of Grieving Widows' is popular item but its not getting enough revenue compared to others. It may be a time to increase its price.

| Item ID | Item Name                            | Item Price | Total Purchase Value | Purchase Count | 
|---------|--------------------------------------|------------|----------------------|----------------| 
| 39      | Betrayal, Whisper of Grieving Widows | \$2.35      | \$25.85               | 11             | 
| 84      | Arcane Gem                           | \$2.23      | \$24.53               | 11             | 
| 31      | Trickster                            | \$2.07      | \$18.63               | 9              | 
| 175     | Woeful Adamantite Claymore           | \$1.24      | \$11.16               | 9              | 
| 13      | Serenity                             | \$1.49      | \$13.41               | 9              | 

Here is the list of most revenue making items.

| Item ID | Item Name                  | Item Price | Total Purchase Value | Purchase Count | 
|---------|----------------------------|------------|----------------------|----------------| 
| 34      | Retribution Axe            | \$4.14      | \$37.26               | 9              | 
| 115     | Spectral Diamond Doomblade | \$4.25      | \$29.75               | 7              | 
| 32      | Orenmir                    | \$4.95      | \$29.70               | 6              | 
| 103     | Singed Scalpel             | \$4.87      | \$29.22               | 6              | 
| 107     | Splitter, Foe Of Subtlety  | \$3.61      | \$28.88               | 8              | 


----
## Tasks completed:

**Player Count**

- Total Number of Players

**Purchasing Analysis (Total)**

- Number of Unique Items
- Average Purchase Price
- Total Number of Purchases
- Total Revenue

**Gender Demographics**

- Percentage and Count of Male Players
- Percentage and Count of Female Players
- Percentage and Count of Other / Non-Disclosed

**Purchasing Analysis (Gender)**

- The below each broken by gender
    - Purchase Count
    - Average Purchase Price
    - Total Purchase Value
    - Normalized Totals

**Age Demographics**

- The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.)
    - Purchase Count
    - Average Purchase Price
    - Total Purchase Value
    - Normalized Totals

**Top Spenders**

- Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
    - SN
    - Purchase Count
    - Average Purchase Price
    - Total Purchase Value

**Most Popular Items**

- Identify the 5 most popular items by purchase count, then list (in a table):
    - Item ID
    - Item Name
    - Purchase Count
    - Item Price
    - Total Purchase Value

**Most Profitable Items**

- Identify the 5 most profitable items by total purchase value, then list (in a table):
    - Item ID
    - Item Name
    - Purchase Count
    - Item Price
    - Total Purchase Value

---
## changelog
* 07-Feb-2018 



```python
import numpy as np
import pandas as pd
```


```python
df = pd.read_json('purchase_data.json')
#df = pd.read_json('purchase_data2.json')
```


```python
#getting sense of data 
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Preparing data : Changing name of Gender column to Gender Demographics

df = df.rename(columns={'Gender' : 'Gender Demographics' })

df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender Demographics</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Preparing data continue --Adding Age Demographics group 
# Dynamic bin calculation

my_source_series = df['Age']
subtract_lable_display=True
bin_precison = 5
upper_bin = int(bin_precison*np.ceil(my_source_series.max()/bin_precison)) 
lower_bin = int(bin_precison*np.floor(my_source_series.min()/bin_precison)) 


myList = []
i = lower_bin
while i <= upper_bin:
    myList.append(i)
    i += bin_precison 


myLabelList = []
myLabelList.append(myList[0])

if subtract_lable_display==True:
    upper_subtract =1
else :
    upper_subtract = 0


j = 1
while j < len(myList):
    mylabel = str(myList[j-1]) + '-' +str( myList[j]-upper_subtract)
    myLabelList.append(mylabel)
    j += 1
myLabelList.pop(0)



#------custom upper bound and lower bound
lowest_list = myLabelList[0].split('-')
myLabelList[0] = '<' + str(int(lowest_list[1])+upper_subtract)

highest_list = myLabelList[len(myLabelList)-1].split('-')
myLabelList[len(myLabelList)-1] = highest_list[0] + '+'
#----------------------------------


df['Age Demographics'] = pd.cut(my_source_series,myList, labels = myLabelList,precision=0,include_lowest=True, right= False)

# upper limit correction
df.loc[(df['Age'] == upper_bin), ['Age Demographics'] ] = myLabelList[len(myLabelList)-1]


df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender Demographics</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Demographics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
#create seperate personal data frame ---normalizing data 
result_list = ['SN','Age','Gender Demographics','Age Demographics']
df_personal = df.loc[:,result_list].drop_duplicates()
df_personal.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender Demographics</th>
      <th>Age Demographics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aelalis34</td>
      <td>38</td>
      <td>Male</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Eolo46</td>
      <td>21</td>
      <td>Male</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Assastnya25</td>
      <td>34</td>
      <td>Male</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pheusrical25</td>
      <td>21</td>
      <td>Male</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aela59</td>
      <td>23</td>
      <td>Male</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Finding total counts of players #Result

total_players = df_personal['SN'].count()
Result_PlayerCount = pd.DataFrame([{'Total Players' : total_players}])         
Result_PlayerCount
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Run Aggregation on purchasing data 

agg_dict = { 'Item ID': ['nunique', 'count'] ,'Price': ['mean', 'sum' ] }
df_PurchasingAnalysis = df.agg(agg_dict)

df_PurchasingAnalysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>780.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>NaN</td>
      <td>2.931192</td>
    </tr>
    <tr>
      <th>nunique</th>
      <td>183.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>sum</th>
      <td>NaN</td>
      <td>2286.330000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchasing Analysis (Total) #result

d1 =  {'Number of Unique Items' : df_PurchasingAnalysis.iloc[2,0 ],  
       'Average Price' : df_PurchasingAnalysis.iloc[1,1 ], 
       'Number of Purchases' : df_PurchasingAnalysis.iloc[0,0 ] , 
       'Total Revenue' : df_PurchasingAnalysis.iloc[3,1 ]
      }

Result_PurchasingAnalysis= pd.DataFrame([d1])

Result_PurchasingAnalysis["Total Revenue"] = Result_PurchasingAnalysis["Total Revenue"].map("$ {:,.2f}".format)
Result_PurchasingAnalysis["Average Price"] = Result_PurchasingAnalysis["Average Price"].map("$ {:,.2f}".format)
Result_PurchasingAnalysis




```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Number of Unique Items</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$ 2.93</td>
      <td>780.0</td>
      <td>183.0</td>
      <td>$ 2,286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Gender Demographics #result

agg_dict = { 'SN': ['count'] }
groupbytype_GenderDemographics = df_personal.groupby(['Gender Demographics'])
Result_GenderDemographics = groupbytype_GenderDemographics.agg(agg_dict)
Result_GenderDemographics.columns = ["_".join(x) for x in Result_GenderDemographics.columns.ravel()]

Result_GenderDemographics = Result_GenderDemographics.rename(columns={'SN_count' : 'Percentage of Players' })
Result_GenderDemographics['Total Count'] = Result_GenderDemographics['Percentage of Players']
Result_GenderDemographics['Percentage of Players'] = round(100*Result_GenderDemographics['Percentage of Players']/total_players,2)

Result_GenderDemographics["Percentage of Players"] = Result_GenderDemographics["Percentage of Players"].map("{0:,.2f}%".format)

Result_GenderDemographics
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Gender Demographics</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>17.45%</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>81.15%</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40%</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchasing Analysis (Gender) #result
agg_dict = { 'SN': ['nunique'],'Price': ['mean', 'sum' ,'count']  }
groupbytype_GenderDemographics1 = df.groupby(['Gender Demographics'])
Result_GenderDemographics1 = groupbytype_GenderDemographics1.agg(agg_dict)
Result_GenderDemographics1.columns = ["_".join(x) for x in Result_GenderDemographics1.columns.ravel()]
Result_GenderDemographics1 = Result_GenderDemographics1.rename(columns={'SN_nunique' : 'Number of Players' , 'Price_count' : 'Purchase Count','Price_sum' : 'Total Purchase Value','Price_mean' : 'Average Purchase Price' })
Result_GenderDemographics1['Normalized Total'] = round(Result_GenderDemographics1['Total Purchase Value']/Result_GenderDemographics1['Number of Players'],2)

Result_GenderDemographics1.drop('Number of Players', axis=1 ,  inplace=True)

Result_GenderDemographics1["Total Purchase Value"] = Result_GenderDemographics1["Total Purchase Value"].map("$ {:,.2f}".format)
Result_GenderDemographics1["Average Purchase Price"] = Result_GenderDemographics1["Average Purchase Price"].map("$ {:,.2f}".format)
Result_GenderDemographics1["Normalized Total"] = Result_GenderDemographics1["Normalized Total"].map("$ {:,.2f}".format)


Result_GenderDemographics1



```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
      <th>Normalized Total</th>
    </tr>
    <tr>
      <th>Gender Demographics</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>$ 2.82</td>
      <td>$ 382.91</td>
      <td>136</td>
      <td>$ 3.83</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>$ 2.95</td>
      <td>$ 1,867.68</td>
      <td>633</td>
      <td>$ 4.02</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>$ 3.25</td>
      <td>$ 35.74</td>
      <td>11</td>
      <td>$ 4.47</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Age Demographics #result

agg_dict = { 'SN': ['count'] }
groupbytype_AgeDemographics = df_personal.groupby(['Age Demographics'])
Result_AgeDemographics = groupbytype_AgeDemographics.agg(agg_dict)
Result_AgeDemographics.columns = ["_".join(x) for x in Result_AgeDemographics.columns.ravel()]

Result_AgeDemographics = Result_AgeDemographics.rename(columns={'SN_count' : 'Percentage of Players' })
Result_AgeDemographics['Total Count'] = Result_AgeDemographics['Percentage of Players']
Result_AgeDemographics['Percentage of Players'] = round(100*Result_AgeDemographics['Percentage of Players']/total_players,2)

Result_AgeDemographics["Percentage of Players"] = Result_AgeDemographics["Percentage of Players"].map("{0:,.2f}%".format)


Result_AgeDemographics
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Age Demographics</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.32%</td>
      <td>19</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.01%</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.45%</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.20%</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>15.18%</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.20%</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>4.71%</td>
      <td>27</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.92%</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchasing Analysis (Age) #result
agg_dict = { 'SN': ['nunique'],'Price': ['mean', 'sum' ,'count']  }
groupbytype_AgeDemographics1 = df.groupby(['Age Demographics'])
Result_AgeDemographics1 = groupbytype_AgeDemographics1.agg(agg_dict)
Result_AgeDemographics1.columns = ["_".join(x) for x in Result_AgeDemographics1.columns.ravel()]
Result_AgeDemographics1 = Result_AgeDemographics1.rename(columns={'SN_nunique' : 'Number of Players' , 'Price_count' : 'Purchase Count','Price_sum' : 'Total Purchase Value','Price_mean' : 'Average Purchase Price' })
Result_AgeDemographics1['Normalized Total'] = round(Result_AgeDemographics1['Total Purchase Value']/Result_AgeDemographics1['Number of Players'],2)

Result_AgeDemographics1.drop('Number of Players', axis=1 ,  inplace=True)

Result_AgeDemographics1["Total Purchase Value"] = Result_AgeDemographics1["Total Purchase Value"].map("$ {:,.2f}".format)
Result_AgeDemographics1["Average Purchase Price"] = Result_AgeDemographics1["Average Purchase Price"].map("$ {:,.2f}".format)
Result_AgeDemographics1["Normalized Total"] = Result_AgeDemographics1["Normalized Total"].map("$ {:,.2f}".format)



Result_AgeDemographics1





```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
      <th>Normalized Total</th>
    </tr>
    <tr>
      <th>Age Demographics</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>$ 2.98</td>
      <td>$ 83.46</td>
      <td>28</td>
      <td>$ 4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>$ 2.77</td>
      <td>$ 96.95</td>
      <td>35</td>
      <td>$ 4.22</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>$ 2.91</td>
      <td>$ 386.42</td>
      <td>133</td>
      <td>$ 3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>$ 2.91</td>
      <td>$ 978.77</td>
      <td>336</td>
      <td>$ 3.78</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>$ 2.96</td>
      <td>$ 370.33</td>
      <td>125</td>
      <td>$ 4.26</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>$ 3.08</td>
      <td>$ 197.25</td>
      <td>64</td>
      <td>$ 4.20</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>$ 2.84</td>
      <td>$ 119.40</td>
      <td>42</td>
      <td>$ 4.42</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>$ 3.16</td>
      <td>$ 53.75</td>
      <td>17</td>
      <td>$ 4.89</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Top Spenders (SN) #result
agg_dict = { 'SN': ['nunique'],'Price': ['mean', 'sum' ,'count']  }
groupbytype_SNDemographics1 = df.groupby(['SN'])
Result_SNDemographics1 = groupbytype_SNDemographics1.agg(agg_dict)
Result_SNDemographics1.columns = ["_".join(x) for x in Result_SNDemographics1.columns.ravel()]
Result_SNDemographics1 = Result_SNDemographics1.rename(columns={'SN_nunique' : 'Number of Players' , 'Price_count' : 'Purchase Count','Price_sum' : 'Total Purchase Value','Price_mean' : 'Average Purchase Price' })

Result_SNDemographics1.drop('Number of Players', axis=1 ,  inplace=True)

Result_SNDemographicssorted=Result_SNDemographics1.sort_values(['Total Purchase Value'], ascending= False).head(5)

Result_SNDemographicssorted["Total Purchase Value"] = Result_SNDemographicssorted["Total Purchase Value"].map("$ {:,.2f}".format)
Result_SNDemographicssorted["Average Purchase Price"] = Result_SNDemographicssorted["Average Purchase Price"].map("$ {:,.2f}".format)

Result_SNDemographicssorted




```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>$ 3.41</td>
      <td>$ 17.06</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>$ 3.39</td>
      <td>$ 13.56</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>$ 3.18</td>
      <td>$ 12.74</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>$ 4.24</td>
      <td>$ 12.73</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>$ 3.86</td>
      <td>$ 11.58</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Popular Items #result

agg_dict = {'Price': ['max', 'sum' ,'count']    }
groupbytype_ItemDemographics1= df.groupby(['Item ID','Item Name'])
Result_ItemDemographics1= groupbytype_ItemDemographics1.agg(agg_dict) 
Result_ItemDemographics1.columns = ["_".join(x) for x in Result_ItemDemographics1.columns.ravel()]

Result_ItemDemographics1 = Result_ItemDemographics1.rename(columns={'Price_count' : 'Purchase Count','Price_sum' : 'Total Purchase Value','Price_max' : 'Item Price' })
Result_ItemDemographics1['Total Purchase Value'] = Result_ItemDemographics1['Purchase Count'] * Result_ItemDemographics1['Item Price']

Result_ItemDemographicssorted=Result_ItemDemographics1.sort_values(['Purchase Count'], ascending= False).head(5)

Result_ItemDemographicssorted["Total Purchase Value"] = Result_ItemDemographicssorted["Total Purchase Value"].map("$ {:,.2f}".format)
Result_ItemDemographicssorted["Item Price"] = Result_ItemDemographicssorted["Item Price"].map("$ {:,.2f}".format)

Result_ItemDemographicssorted
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>$ 2.35</td>
      <td>$ 25.85</td>
      <td>11</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>$ 2.23</td>
      <td>$ 24.53</td>
      <td>11</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>$ 2.07</td>
      <td>$ 18.63</td>
      <td>9</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>$ 1.24</td>
      <td>$ 11.16</td>
      <td>9</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>$ 1.49</td>
      <td>$ 13.41</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Profitable Items #result

Result_ItemDemographicssorted2=Result_ItemDemographics1.sort_values(['Total Purchase Value'], ascending= False).head(5)

Result_ItemDemographicssorted2["Total Purchase Value"] = Result_ItemDemographicssorted2["Total Purchase Value"].map("$ {:,.2f}".format)
Result_ItemDemographicssorted2["Item Price"] = Result_ItemDemographicssorted2["Item Price"].map("$ {:,.2f}".format)

Result_ItemDemographicssorted2
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>$ 4.14</td>
      <td>$ 37.26</td>
      <td>9</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>$ 4.25</td>
      <td>$ 29.75</td>
      <td>7</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>$ 4.95</td>
      <td>$ 29.70</td>
      <td>6</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>$ 4.87</td>
      <td>$ 29.22</td>
      <td>6</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>$ 3.61</td>
      <td>$ 28.88</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>


