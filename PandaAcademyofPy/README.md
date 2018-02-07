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
