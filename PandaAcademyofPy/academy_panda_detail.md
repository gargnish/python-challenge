
# Data Analysis on School Academy
----
## Conclusion


> Data analysis was performed on school data set (schools_complete.csv, students_complete.csv) and following observations were made:

----
### Trend 1:
If number of students per school is less then the '% overall Passing rate' is high. 
That means it makes sense to break schools with higher number of students into smaller schools. 

|     School Size    | Average Math Score | Average Reading Score | % Passing Math | % Passing Reading | % Overall Passing Rate | 
|--------------------|-----------------------|----------------|-------------------|------------------------|--------| 
|        |                       |                |                   |                        |        | 
| Small <(1000)      | 83.83                 | 83.97          | 91.36%            | 92.37%                 | 91.86% | 
| Medium (1000-3000) | 80.45                 | 82.63          | 78.66%            | 86.61%                 | 82.64% | 
| Large (3000-5000)  | 77.07                 | 80.93          | 64.34%            | 78.42%                 | 71.38% | 


----
### Trend 2:
Higher grade students have lower scores. This means schools should focus on curriculum for higher grades. 


| grade/school          | 10th  | 11th  | 12th  | 9th    | 
|-----------------------|-------|-------|-------|--------| 
| Bailey High School    | 95399 | 96972 | 78634 | 112388 | 
| Cabrera High School   | 38750 | 39893 | 31812 | 43874  | 
| Figueroa High School  | 58400 | 54511 | 47911 | 65401  | 
| Ford High School      | 54992 | 50689 | 41061 | 64442  | 
| Griffin High School   | 34197 | 30267 | 24340 | 33556  | 
| Hernandez High School | 94893 | 83924 | 72401 | 107020 | 
| Holden High School    | 9511  | 8755  | 6877  | 10641  | 
| Huang High School     | 58222 | 55118 | 45177 | 65011  | 
| Johnson High School   | 94100 | 92835 | 71944 | 108063 | 
| Pena High School      | 20843 | 21588 | 15226 | 22997  | 
| Rodriguez High School | 79677 | 76854 | 61298 | 89465  | 
| Shelton High School   | 37147 | 34354 | 31082 | 44213  | 
| Thomas High School    | 34980 | 34652 | 28222 | 38535  | 
| Wilson High School    | 50737 | 49834 | 37117 | 52427  | 
| Wright High School    | 40829 | 36469 | 30865 | 42465  | 





----
### Trend 3:
Charter schools performance is better. School district should analyze charter schools programs and consider implementing them in district schools.

| School Type | Average Math Score | Average Reading Score | % Passing Math | % Passing Reading | % Overall Passing Rate | 
|-------------|--------------------|-----------------------|----------------|-------------------|------------------------| 
| Charter     | 83.41              | 83.9                  | 90.28%         | 93.15%            | 91.72%                 | 
| District    | 76.99              | 80.96                 | 64.31%         | 78.37%            | 71.34%                 | 




----
## Tasks completed:
**District Summary**

- Create a high level snapshot (in table form) of the district's key metrics, including:
    - Total Schools
    - Total Students
    - Total Budget
    - Average Math Score
    - Average Reading Score
    - % Passing Math
    - % Passing Reading
    - Overall Passing Rate (Average of the above two)

**School Summary**

- Create an overview table that summarizes key metrics about each school, including:
    - School Name
    - School Type
    - Total Students
    - Total School Budget
    - Per Student Budget
    - Average Math Score
    - Average Reading Score
    - % Passing Math
    - % Passing Reading
    - Overall Passing Rate (Average of the above two)

**Top Performing Schools (By Passing Rate)**

- Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:
    - School Name
    - School Type
    - Total Students
    - Total School Budget
    - Per Student Budget
    - Average Math Score
    - Average Reading Score
    - % Passing Math
    - % Passing Reading
    - Overall Passing Rate (Average of the above two)

**Top Performing Schools (By Passing Rate)**

- Create a table that highlights the bottom 5 performing schools based on Overall Passing Rate. Include all of the same metrics as above.

**Math Scores by Grade**

- Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

**Reading Scores by Grade**

- Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

**Scores by School Spending**

- Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
    - Average Math Score
    - Average Reading Score
    - % Passing Math
    - % Passing Reading
    - Overall Passing Rate (Average of the above two)

**Scores by School Size**

- Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).

**Scores by School Type**

- Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).


---
## changelog
* 07-Feb-2018 






```python
import numpy as np
import pandas as pd
```


```python
df_school = pd.read_csv('schools_complete.csv')
df_student = pd.read_csv('students_complete.csv')
pd.options.display.float_format = '{:,.2f}'.format
```


```python
# Preparing data school
df_school = df_school.rename(columns={'name' : 'school' , 'type' : 'School Type' , 'budget' : 'Total School Budget' })
df_school.head()
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
      <th>School ID</th>
      <th>school</th>
      <th>School Type</th>
      <th>size</th>
      <th>Total School Budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# More preparing : adding school size range 

#--------
bin_precison = 1000
upper_school_size_bin = int(bin_precison*np.ceil(df_school['size'].max()/bin_precison))
lower_school_size_bin = int(bin_precison*np.ceil(df_school['size'].min()/bin_precison))
mid_school_size_bin = int((lower_school_size_bin + upper_school_size_bin)/2)

school_size_bin = [0,lower_school_size_bin,mid_school_size_bin,upper_school_size_bin]
school_size_bin_label = ['Small <('+str(lower_school_size_bin)+')' ,'Medium ('+ str(lower_school_size_bin) +'-'+ str(mid_school_size_bin)+ ')', 'Large ('+ str(mid_school_size_bin) +'-'+ str(upper_school_size_bin)+ ')']
df_school['School Size'] = pd.cut(df_school['size'],school_size_bin, labels = school_size_bin_label,precision=0,include_lowest=False)

df_school.head()

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
      <th>School ID</th>
      <th>school</th>
      <th>School Type</th>
      <th>size</th>
      <th>Total School Budget</th>
      <th>School Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>Medium (1000-3000)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>Medium (1000-3000)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>Medium (1000-3000)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>Large (3000-5000)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>Medium (1000-3000)</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Preparing data  continue : student --calculation of pass/fail 

# fail = 0 and pass = 1 define as integer so it will be easier to find passing using sum 
pass_fail_label = [0,1]

# Assumed 70 and above is passing
df_student['math_pass_fail'] = pd.cut(df_student['math_score'],[0,70,200], labels = pass_fail_label, include_lowest=True)
df_student['reading_pass_fail'] = pd.cut(df_student['reading_score'],[0,70,200], labels = pass_fail_label, include_lowest=True)
df_student['overall_pass_fail'] = pd.to_numeric(0)
df_student.loc[(df_student['math_pass_fail']==1) & (df_student['reading_pass_fail']==1), 'overall_pass_fail'] = 1

df_student['math_pass_fail'] =pd.to_numeric(df_student['math_pass_fail'])
df_student['reading_pass_fail'] =pd.to_numeric(df_student['reading_pass_fail'])
df_student['overall_pass_fail'] =pd.to_numeric(df_student['overall_pass_fail'])

df_student.head()

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
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>math_pass_fail</th>
      <th>reading_pass_fail</th>
      <th>overall_pass_fail</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
#preperaring more data : Aggregating student data by school

agg_dict = { 'Student ID' : ['count'] , 'math_pass_fail' : ['sum']  , 'reading_pass_fail' : sum ,'math_score' : sum  , 'reading_score' : sum  }
df_student_sagg_type = df_student.groupby(['school'])
df_student_sagg = df_student_sagg_type.agg(agg_dict)
df_student_sagg.columns = ["_".join(x) for x in df_student_sagg.columns.ravel()]
df_student_sagg.head()

df_student_sagg = df_student_sagg.rename(columns={ 'Student ID_count' : 'Total Students' ,'math_score_sum' : 'Total Math Score' , 'reading_score_sum' : 'Total Reading Score', 'math_pass_fail_sum' : 'Total Math Pass' , 'reading_pass_fail_sum' : 'Total Reading Pass'})

df_student_sagg.reset_index(inplace=True)

df_student_sagg.head()
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
      <th>school</th>
      <th>Total Students</th>
      <th>Total Math Pass</th>
      <th>Total Reading Pass</th>
      <th>Total Math Score</th>
      <th>Total Reading Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>4976</td>
      <td>3216</td>
      <td>3946</td>
      <td>383393</td>
      <td>403225</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>1858</td>
      <td>1664</td>
      <td>1744</td>
      <td>154329</td>
      <td>156027</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>2949</td>
      <td>1880</td>
      <td>2313</td>
      <td>226223</td>
      <td>239335</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>2739</td>
      <td>1801</td>
      <td>2123</td>
      <td>211184</td>
      <td>221164</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>1468</td>
      <td>1317</td>
      <td>1371</td>
      <td>122360</td>
      <td>123043</td>
    </tr>
  </tbody>
</table>
</div>




```python

#preperaring more data : Aggregating student data by school-- adding more columns

df_school_summary = pd.merge(df_school, df_student_sagg, on ='school')

df_school_summary.head()

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
      <th>School ID</th>
      <th>school</th>
      <th>School Type</th>
      <th>size</th>
      <th>Total School Budget</th>
      <th>School Size</th>
      <th>Total Students</th>
      <th>Total Math Pass</th>
      <th>Total Reading Pass</th>
      <th>Total Math Score</th>
      <th>Total Reading Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>Medium (1000-3000)</td>
      <td>2917</td>
      <td>1847</td>
      <td>2299</td>
      <td>223528</td>
      <td>236810</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>Medium (1000-3000)</td>
      <td>2949</td>
      <td>1880</td>
      <td>2313</td>
      <td>226223</td>
      <td>239335</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>Medium (1000-3000)</td>
      <td>1761</td>
      <td>1583</td>
      <td>1631</td>
      <td>146796</td>
      <td>147441</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>Large (3000-5000)</td>
      <td>4635</td>
      <td>3001</td>
      <td>3624</td>
      <td>358238</td>
      <td>375131</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>Medium (1000-3000)</td>
      <td>1468</td>
      <td>1317</td>
      <td>1371</td>
      <td>122360</td>
      <td>123043</td>
    </tr>
  </tbody>
</table>
</div>




```python
# More preparing : adding spending range to summary data 

budget_per_student_series = df_school_summary['Total School Budget']/df_school_summary['Total Students']

bin_precison = 10
upper_bps_bin = int(bin_precison*np.ceil(budget_per_student_series.max()/bin_precison))
lower_bps_bin = int(bin_precison*np.ceil(budget_per_student_series.min()/bin_precison))
mid1_bps_bin = int(lower_bps_bin +(budget_per_student_series.max() -lower_bps_bin  )/3)
mid2_bps_bin = int(lower_bps_bin +2*(budget_per_student_series.max() -lower_bps_bin  )/3)
bps_bin = [0,lower_bps_bin,mid1_bps_bin,mid2_bps_bin,upper_bps_bin]
bps_bin_label = ['<'+str(lower_bps_bin) ,str(lower_bps_bin) +'-'+ str(mid1_bps_bin),str(mid1_bps_bin) +'-'+ str(mid2_bps_bin), str(mid2_bps_bin) +'-'+ str(upper_bps_bin)]

#df_school['Spending Ranges(Per Student)'] = pd.cut(budget_per_student_series,bps_bin, labels = bps_bin_label,precision=0,include_lowest=False)
df_school_summary['Spending Ranges(Per Student)'] = pd.cut(budget_per_student_series,bps_bin, labels = bps_bin_label,precision=0,include_lowest=False)

df_school_summary.head()
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
      <th>School ID</th>
      <th>school</th>
      <th>School Type</th>
      <th>size</th>
      <th>Total School Budget</th>
      <th>School Size</th>
      <th>Total Students</th>
      <th>Total Math Pass</th>
      <th>Total Reading Pass</th>
      <th>Total Math Score</th>
      <th>Total Reading Score</th>
      <th>Spending Ranges(Per Student)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>Medium (1000-3000)</td>
      <td>2917</td>
      <td>1847</td>
      <td>2299</td>
      <td>223528</td>
      <td>236810</td>
      <td>630-660</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>Medium (1000-3000)</td>
      <td>2949</td>
      <td>1880</td>
      <td>2313</td>
      <td>226223</td>
      <td>239335</td>
      <td>630-660</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>Medium (1000-3000)</td>
      <td>1761</td>
      <td>1583</td>
      <td>1631</td>
      <td>146796</td>
      <td>147441</td>
      <td>580-605</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>Large (3000-5000)</td>
      <td>4635</td>
      <td>3001</td>
      <td>3624</td>
      <td>358238</td>
      <td>375131</td>
      <td>630-660</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>Medium (1000-3000)</td>
      <td>1468</td>
      <td>1317</td>
      <td>1371</td>
      <td>122360</td>
      <td>123043</td>
      <td>605-630</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Run Aggregation on school data 

TotalSchools = df_school['School ID'].count() 
TotalBudget = df_school['Total School Budget'].sum() 

d1 ={ 'Total Schools' : TotalSchools,'Total Budget' : TotalBudget}
df_distinct_summary = pd.DataFrame([d1])
df_distinct_summary
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
      <th>Total Budget</th>
      <th>Total Schools</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>24649428</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Run Aggregation on student data 
df_distinct_summary['Total Students'] = df_student['Student ID'].count() 
df_distinct_summary['Total Math Pass'] = df_student['math_pass_fail'].sum() 
df_distinct_summary['Total Reading Pass'] = df_student['reading_pass_fail'].sum() 
df_distinct_summary['Total Overall Pass'] = df_student['overall_pass_fail'].sum() 
df_distinct_summary['Total Math Score'] = df_student['math_score'].sum() 
df_distinct_summary['Total Reading Score'] = df_student['reading_score'].sum()
df_distinct_summary['Average Math Score'] = df_distinct_summary['Total Math Score']/df_distinct_summary['Total Students']
df_distinct_summary['% Passing Math'] = 100*df_distinct_summary['Total Math Pass']/df_distinct_summary['Total Students']
df_distinct_summary['Average Reading Score'] = df_distinct_summary['Total Reading Score']/df_distinct_summary['Total Students']
df_distinct_summary['% Passing Reading'] = 100*df_distinct_summary['Total Reading Pass']/df_distinct_summary['Total Students']
df_distinct_summary['% Overall Passing Rate'] = 100*df_distinct_summary['Total Overall Pass']/df_distinct_summary['Total Students']

df_distinct_summary.head()



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
      <th>Total Budget</th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Math Pass</th>
      <th>Total Reading Pass</th>
      <th>Total Overall Pass</th>
      <th>Total Math Score</th>
      <th>Total Reading Score</th>
      <th>Average Math Score</th>
      <th>% Passing Math</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>24649428</td>
      <td>15</td>
      <td>39170</td>
      <td>28356</td>
      <td>32500</td>
      <td>23816</td>
      <td>3093857</td>
      <td>3207155</td>
      <td>78.99</td>
      <td>72.39</td>
      <td>81.88</td>
      <td>82.97</td>
      <td>60.80</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Result district_summary

result_list = ['Total Schools','Total Students','Total Budget','Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','% Overall Passing Rate']
result_district_summary = df_distinct_summary.loc[:,result_list]


result_district_summary["% Passing Math"] = result_district_summary["% Passing Math"].map("{0:,.2f}%".format)
result_district_summary["% Passing Reading"] = result_district_summary["% Passing Reading"].map("{0:,.2f}%".format)
result_district_summary["% Overall Passing Rate"] = result_district_summary["% Overall Passing Rate"].map("{0:,.2f}%".format)

result_district_summary["Total Budget"] = result_district_summary["Total Budget"].map("$ {:,.2f}".format)
result_district_summary["Total Students"] = result_district_summary["Total Students"].map("{0:,.0f}".format)

result_district_summary



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
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39,170</td>
      <td>$ 24,649,428.00</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>72.39%</td>
      <td>82.97%</td>
      <td>60.80%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Result school summary 
result_list = ['school','School Type','Total Students','Total School Budget','Per Student Budget']
df_school_summary1 = df_school_summary.loc[:,result_list]

df_school_summary1['Average Math Score'] = df_school_summary['Total Math Score']/df_school_summary['Total Students']
df_school_summary1['% Passing Math'] = 100*df_school_summary['Total Math Pass']/df_school_summary['Total Students']
df_school_summary1['Average Reading Score'] = df_school_summary['Total Reading Score']/df_school_summary['Total Students']
df_school_summary1['% Passing Reading'] = 100*df_school_summary['Total Reading Pass']/df_school_summary['Total Students']
df_school_summary1['% Overall Passing Rate'] = (df_school_summary1['% Passing Math']+df_school_summary1['% Passing Reading'])/2
df_school_summary1['Per Student Budget'] = (df_school_summary['Total School Budget']/df_school_summary['Total Students'])



df_school_summary1.set_index("school" , inplace=True)

df_school_summary1["% Passing Math"] = df_school_summary1["% Passing Math"].map("{0:,.2f}%".format)
df_school_summary1["% Passing Reading"] = df_school_summary1["% Passing Reading"].map("{0:,.2f}%".format)
df_school_summary1["% Overall Passing Rate"] = df_school_summary1["% Overall Passing Rate"].map("{0:,.2f}%".format)

df_school_summary1["Total School Budget"] = df_school_summary1["Total School Budget"].map("$ {:,.2f}".format)
df_school_summary1["Total Students"] = df_school_summary1["Total Students"].map("{0:,.0f}".format)


df_school_summary1



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
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>% Passing Math</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2,917</td>
      <td>$ 1,910,635.00</td>
      <td>655.00</td>
      <td>76.63</td>
      <td>63.32%</td>
      <td>81.18</td>
      <td>78.81%</td>
      <td>71.07%</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2,949</td>
      <td>$ 1,884,411.00</td>
      <td>639.00</td>
      <td>76.71</td>
      <td>63.75%</td>
      <td>81.16</td>
      <td>78.43%</td>
      <td>71.09%</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1,761</td>
      <td>$ 1,056,600.00</td>
      <td>600.00</td>
      <td>83.36</td>
      <td>89.89%</td>
      <td>83.73</td>
      <td>92.62%</td>
      <td>91.25%</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4,635</td>
      <td>$ 3,022,020.00</td>
      <td>652.00</td>
      <td>77.29</td>
      <td>64.75%</td>
      <td>80.93</td>
      <td>78.19%</td>
      <td>71.47%</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1,468</td>
      <td>$ 917,500.00</td>
      <td>625.00</td>
      <td>83.35</td>
      <td>89.71%</td>
      <td>83.82</td>
      <td>93.39%</td>
      <td>91.55%</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2,283</td>
      <td>$ 1,319,574.00</td>
      <td>578.00</td>
      <td>83.27</td>
      <td>90.93%</td>
      <td>83.99</td>
      <td>93.25%</td>
      <td>92.09%</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1,858</td>
      <td>$ 1,081,356.00</td>
      <td>582.00</td>
      <td>83.06</td>
      <td>89.56%</td>
      <td>83.98</td>
      <td>93.86%</td>
      <td>91.71%</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>District</td>
      <td>4,976</td>
      <td>$ 3,124,928.00</td>
      <td>628.00</td>
      <td>77.05</td>
      <td>64.63%</td>
      <td>81.03</td>
      <td>79.30%</td>
      <td>71.97%</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>$ 248,087.00</td>
      <td>581.00</td>
      <td>83.80</td>
      <td>90.63%</td>
      <td>83.81</td>
      <td>92.74%</td>
      <td>91.69%</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>$ 585,858.00</td>
      <td>609.00</td>
      <td>83.84</td>
      <td>91.68%</td>
      <td>84.04</td>
      <td>92.20%</td>
      <td>91.94%</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1,800</td>
      <td>$ 1,049,400.00</td>
      <td>583.00</td>
      <td>83.68</td>
      <td>90.28%</td>
      <td>83.95</td>
      <td>93.44%</td>
      <td>91.86%</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3,999</td>
      <td>$ 2,547,363.00</td>
      <td>637.00</td>
      <td>76.84</td>
      <td>64.07%</td>
      <td>80.74</td>
      <td>77.74%</td>
      <td>70.91%</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4,761</td>
      <td>$ 3,094,650.00</td>
      <td>650.00</td>
      <td>77.07</td>
      <td>63.85%</td>
      <td>80.97</td>
      <td>78.28%</td>
      <td>71.07%</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2,739</td>
      <td>$ 1,763,916.00</td>
      <td>644.00</td>
      <td>77.10</td>
      <td>65.75%</td>
      <td>80.75</td>
      <td>77.51%</td>
      <td>71.63%</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1,635</td>
      <td>$ 1,043,130.00</td>
      <td>638.00</td>
      <td>83.42</td>
      <td>90.21%</td>
      <td>83.85</td>
      <td>92.91%</td>
      <td>91.56%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Result top performing schools by passing rate 

df_school_summary_top_5 = df_school_summary1.sort_values(['% Overall Passing Rate'], ascending=False)
df_school_summary_top_5.head(5)
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
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>% Passing Math</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2,283</td>
      <td>$ 1,319,574.00</td>
      <td>578.00</td>
      <td>83.27</td>
      <td>90.93%</td>
      <td>83.99</td>
      <td>93.25%</td>
      <td>92.09%</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>$ 585,858.00</td>
      <td>609.00</td>
      <td>83.84</td>
      <td>91.68%</td>
      <td>84.04</td>
      <td>92.20%</td>
      <td>91.94%</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1,800</td>
      <td>$ 1,049,400.00</td>
      <td>583.00</td>
      <td>83.68</td>
      <td>90.28%</td>
      <td>83.95</td>
      <td>93.44%</td>
      <td>91.86%</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1,858</td>
      <td>$ 1,081,356.00</td>
      <td>582.00</td>
      <td>83.06</td>
      <td>89.56%</td>
      <td>83.98</td>
      <td>93.86%</td>
      <td>91.71%</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>$ 248,087.00</td>
      <td>581.00</td>
      <td>83.80</td>
      <td>90.63%</td>
      <td>83.81</td>
      <td>92.74%</td>
      <td>91.69%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Result worst performing schools by passing rate 

df_school_summary_bottom_5 = df_school_summary1.sort_values(['% Overall Passing Rate'], ascending=True).head(5)
df_school_summary_bottom_5
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
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>% Passing Math</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3,999</td>
      <td>$ 2,547,363.00</td>
      <td>637.00</td>
      <td>76.84</td>
      <td>64.07%</td>
      <td>80.74</td>
      <td>77.74%</td>
      <td>70.91%</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2,917</td>
      <td>$ 1,910,635.00</td>
      <td>655.00</td>
      <td>76.63</td>
      <td>63.32%</td>
      <td>81.18</td>
      <td>78.81%</td>
      <td>71.07%</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4,761</td>
      <td>$ 3,094,650.00</td>
      <td>650.00</td>
      <td>77.07</td>
      <td>63.85%</td>
      <td>80.97</td>
      <td>78.28%</td>
      <td>71.07%</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2,949</td>
      <td>$ 1,884,411.00</td>
      <td>639.00</td>
      <td>76.71</td>
      <td>63.75%</td>
      <td>81.16</td>
      <td>78.43%</td>
      <td>71.09%</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4,635</td>
      <td>$ 3,022,020.00</td>
      <td>652.00</td>
      <td>77.29</td>
      <td>64.75%</td>
      <td>80.93</td>
      <td>78.19%</td>
      <td>71.47%</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Preparing for scores by grade 
gradeagg_dict_student = {'math_score' : sum , 'reading_score' : sum}
df_student_gradeagg= df_student.groupby(['school','grade']).agg(gradeagg_dict_student)
df_student_gradeagg.reset_index(inplace=True)
df_student_gradeagg.head(10)

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
      <th>school</th>
      <th>grade</th>
      <th>math_score</th>
      <th>reading_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>10th</td>
      <td>95399</td>
      <td>100244</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bailey High School</td>
      <td>11th</td>
      <td>96972</td>
      <td>101263</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bailey High School</td>
      <td>12th</td>
      <td>78634</td>
      <td>83178</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bailey High School</td>
      <td>9th</td>
      <td>112388</td>
      <td>118540</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cabrera High School</td>
      <td>10th</td>
      <td>38750</td>
      <td>39262</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Cabrera High School</td>
      <td>11th</td>
      <td>39893</td>
      <td>40386</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>12th</td>
      <td>31812</td>
      <td>32198</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Cabrera High School</td>
      <td>9th</td>
      <td>43874</td>
      <td>44181</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Figueroa High School</td>
      <td>10th</td>
      <td>58400</td>
      <td>62115</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Figueroa High School</td>
      <td>11th</td>
      <td>54511</td>
      <td>57174</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Result math scores by grade 
df_student_gradeagg_math= df_student_gradeagg.pivot(index='school', columns='grade', values='math_score')
df_student_gradeagg_math

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
      <th>grade</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>95399</td>
      <td>96972</td>
      <td>78634</td>
      <td>112388</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>38750</td>
      <td>39893</td>
      <td>31812</td>
      <td>43874</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>58400</td>
      <td>54511</td>
      <td>47911</td>
      <td>65401</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>54992</td>
      <td>50689</td>
      <td>41061</td>
      <td>64442</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>34197</td>
      <td>30267</td>
      <td>24340</td>
      <td>33556</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>94893</td>
      <td>83924</td>
      <td>72401</td>
      <td>107020</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>9511</td>
      <td>8755</td>
      <td>6877</td>
      <td>10641</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>58222</td>
      <td>55118</td>
      <td>45177</td>
      <td>65011</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>94100</td>
      <td>92835</td>
      <td>71944</td>
      <td>108063</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>20843</td>
      <td>21588</td>
      <td>15226</td>
      <td>22997</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>79677</td>
      <td>76854</td>
      <td>61298</td>
      <td>89465</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>37147</td>
      <td>34354</td>
      <td>31082</td>
      <td>44213</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>34980</td>
      <td>34652</td>
      <td>28222</td>
      <td>38535</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>50737</td>
      <td>49834</td>
      <td>37117</td>
      <td>52427</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>40829</td>
      <td>36469</td>
      <td>30865</td>
      <td>42465</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Result reading  scores by grade 

df_student_gradeagg_reading= df_student_gradeagg.pivot(index='school', columns='grade', values='reading_score')
df_student_gradeagg_reading

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
      <th>grade</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>100244</td>
      <td>101263</td>
      <td>83178</td>
      <td>118540</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>39262</td>
      <td>40386</td>
      <td>32198</td>
      <td>44181</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>62115</td>
      <td>57174</td>
      <td>50540</td>
      <td>69506</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>57534</td>
      <td>52986</td>
      <td>43477</td>
      <td>67167</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>33985</td>
      <td>30428</td>
      <td>24532</td>
      <td>34098</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>98970</td>
      <td>88559</td>
      <td>75844</td>
      <td>111758</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>9499</td>
      <td>8633</td>
      <td>7030</td>
      <td>10627</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>62520</td>
      <td>58702</td>
      <td>46979</td>
      <td>68609</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>99109</td>
      <td>96578</td>
      <td>76029</td>
      <td>113765</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>20903</td>
      <td>21590</td>
      <td>15311</td>
      <td>23047</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>83855</td>
      <td>81350</td>
      <td>63417</td>
      <td>94276</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>37382</td>
      <td>34762</td>
      <td>30712</td>
      <td>44585</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>35471</td>
      <td>34688</td>
      <td>28335</td>
      <td>38599</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>50917</td>
      <td>50175</td>
      <td>37690</td>
      <td>52966</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>40733</td>
      <td>36608</td>
      <td>31023</td>
      <td>42755</td>
    </tr>
  </tbody>
</table>
</div>




```python
#result scores by school spending 

agg_dict_budget_per_student_bin = {'Total Students' : sum , 'Total Math Score' : sum ,'Total Reading Score' : sum ,'Total Math Pass' : sum ,'Total Reading Pass' : sum  }
df_budget_per_student_bin_agg= df_school_summary.groupby(['Spending Ranges(Per Student)']).agg(agg_dict_budget_per_student_bin)
df_budget_per_student_bin_agg['Average Math Score'] = df_budget_per_student_bin_agg['Total Math Score']/df_budget_per_student_bin_agg['Total Students']
df_budget_per_student_bin_agg['% Passing Math'] = 100*df_budget_per_student_bin_agg['Total Math Pass']/df_budget_per_student_bin_agg['Total Students']
df_budget_per_student_bin_agg['Average Reading Score'] = df_budget_per_student_bin_agg['Total Reading Score']/df_budget_per_student_bin_agg['Total Students']
df_budget_per_student_bin_agg['% Passing Reading'] = 100*df_budget_per_student_bin_agg['Total Reading Pass']/df_budget_per_student_bin_agg['Total Students']
df_budget_per_student_bin_agg['% Overall Passing Rate'] = (df_budget_per_student_bin_agg['% Passing Math']+df_budget_per_student_bin_agg['% Passing Reading'])/2

result_list = ['Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','% Overall Passing Rate']
df_budget_per_student_bin_agg = df_budget_per_student_bin_agg.loc[:,result_list]


df_budget_per_student_bin_agg["% Passing Math"] = df_budget_per_student_bin_agg["% Passing Math"].map("{0:,.2f}%".format)
df_budget_per_student_bin_agg["% Passing Reading"] = df_budget_per_student_bin_agg["% Passing Reading"].map("{0:,.2f}%".format)
df_budget_per_student_bin_agg["% Overall Passing Rate"] = df_budget_per_student_bin_agg["% Overall Passing Rate"].map("{0:,.2f}%".format)


df_budget_per_student_bin_agg

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
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Spending Ranges(Per Student)</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;580</th>
      <td>83.27</td>
      <td>83.99</td>
      <td>90.93%</td>
      <td>93.25%</td>
      <td>92.09%</td>
    </tr>
    <tr>
      <th>580-605</th>
      <td>83.40</td>
      <td>83.88</td>
      <td>89.96%</td>
      <td>93.28%</td>
      <td>91.62%</td>
    </tr>
    <tr>
      <th>605-630</th>
      <td>79.18</td>
      <td>81.98</td>
      <td>73.12%</td>
      <td>83.77%</td>
      <td>78.44%</td>
    </tr>
    <tr>
      <th>630-660</th>
      <td>77.42</td>
      <td>81.15</td>
      <td>66.03%</td>
      <td>79.18%</td>
      <td>72.60%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#result scores by school type

agg_dict_school_type = {'Total Students' : sum , 'Total Math Score' : sum ,'Total Reading Score' : sum ,'Total Math Pass' : sum ,'Total Reading Pass' : sum  }
df_school_type_agg= df_school_summary.groupby(['School Type']).agg(agg_dict_school_type)
df_school_type_agg['Average Math Score'] = df_school_type_agg['Total Math Score']/df_school_type_agg['Total Students']
df_school_type_agg['% Passing Math'] = 100*df_school_type_agg['Total Math Pass']/df_school_type_agg['Total Students']
df_school_type_agg['Average Reading Score'] = df_school_type_agg['Total Reading Score']/df_school_type_agg['Total Students']
df_school_type_agg['% Passing Reading'] = 100*df_school_type_agg['Total Reading Pass']/df_school_type_agg['Total Students']
df_school_type_agg['% Overall Passing Rate'] = (df_school_type_agg['% Passing Math']+df_school_type_agg['% Passing Reading'])/2

result_list = ['Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','% Overall Passing Rate']
df_school_type_agg = df_school_type_agg.loc[:,result_list]

df_school_type_agg["% Passing Math"] = df_school_type_agg["% Passing Math"].map("{0:,.2f}%".format)
df_school_type_agg["% Passing Reading"] = df_school_type_agg["% Passing Reading"].map("{0:,.2f}%".format)
df_school_type_agg["% Overall Passing Rate"] = df_school_type_agg["% Overall Passing Rate"].map("{0:,.2f}%".format)


df_school_type_agg

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
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.41</td>
      <td>83.90</td>
      <td>90.28%</td>
      <td>93.15%</td>
      <td>91.72%</td>
    </tr>
    <tr>
      <th>District</th>
      <td>76.99</td>
      <td>80.96</td>
      <td>64.31%</td>
      <td>78.37%</td>
      <td>71.34%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#result scores by school size

agg_dict_school_size_bin = {'Total Students' : sum , 'Total Math Score' : sum ,'Total Reading Score' : sum ,'Total Math Pass' : sum ,'Total Reading Pass' : sum  }
df_school_size_bin_agg= df_school_summary.groupby(['School Size']).agg(agg_dict_school_size_bin)
df_school_size_bin_agg['Average Math Score'] = df_school_size_bin_agg['Total Math Score']/df_school_size_bin_agg['Total Students']
df_school_size_bin_agg['% Passing Math'] = 100*df_school_size_bin_agg['Total Math Pass']/df_school_size_bin_agg['Total Students']
df_school_size_bin_agg['Average Reading Score'] = df_school_size_bin_agg['Total Reading Score']/df_school_size_bin_agg['Total Students']
df_school_size_bin_agg['% Passing Reading'] = 100*df_school_size_bin_agg['Total Reading Pass']/df_school_size_bin_agg['Total Students']
df_school_size_bin_agg['% Overall Passing Rate'] = (df_school_size_bin_agg['% Passing Math']+df_school_size_bin_agg['% Passing Reading'])/2

result_list = ['Average Math Score','Average Reading Score','% Passing Math','% Passing Reading','% Overall Passing Rate']
df_school_size_bin_agg = df_school_size_bin_agg.loc[:,result_list]


df_school_size_bin_agg["% Passing Math"] = df_school_size_bin_agg["% Passing Math"].map("{0:,.2f}%".format)
df_school_size_bin_agg["% Passing Reading"] = df_school_size_bin_agg["% Passing Reading"].map("{0:,.2f}%".format)
df_school_size_bin_agg["% Overall Passing Rate"] = df_school_size_bin_agg["% Overall Passing Rate"].map("{0:,.2f}%".format)

df_school_size_bin_agg
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
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small &lt;(1000)</th>
      <td>83.83</td>
      <td>83.97</td>
      <td>91.36%</td>
      <td>92.37%</td>
      <td>91.86%</td>
    </tr>
    <tr>
      <th>Medium (1000-3000)</th>
      <td>80.45</td>
      <td>82.63</td>
      <td>78.66%</td>
      <td>86.61%</td>
      <td>82.64%</td>
    </tr>
    <tr>
      <th>Large (3000-5000)</th>
      <td>77.07</td>
      <td>80.93</td>
      <td>64.34%</td>
      <td>78.42%</td>
      <td>71.38%</td>
    </tr>
  </tbody>
</table>
</div>


