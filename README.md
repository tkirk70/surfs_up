# surfs_up :surfer:
OSU Module 9 - SQLite and Flask



Overview of the analysis: 
- We want temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.
- Gather temperature trends for Winter and Summer months over a seven-year span.
   - Specifically for the months of December and June from nine different weather stations across the island of Oahu.

Results:
- Gather temperature trends for Winter and Summer months over a seven-year span.


```python

# 1. Import the sqlalchemy extract function.
from sqlalchemy import extract
# 2. Write a query that filters the Measurement table to retrieve the temperatures for the month of June. )
jun_results = session.query(Measurement.date, Measurement.tobs).filter(func.strftime("%m", Measurement.date) == "06")
# 3. Create a DataFrame from the list of temperatures for the month of June. 
jun_df = pd.DataFrame(jun_results, columns=['Date','June Temps'])
jun_df.set_index(jun_df['Date'], inplace=True)
jun_df.describe()

```
| Statistic | June Temps |       
| --- | --- |                    
|count|  1700.000000 |
|mean|  74.944118 |
|std|  3.257417 |
|min|  64.000000 |
|25%|  73.000000 |
|50%|  75.000000 |
|75%|  77.000000 |
|max|  85.000000 |

```python

# 1. Import the sqlalchemy extract function.
from sqlalchemy import extract
# 2. Write a query that filters the Measurement table to retrieve the temperatures for the month of December. )
dec_results = session.query(Measurement.date, Measurement.tobs).filter(func.strftime("%m", Measurement.date) == "12")
# 3. Create a DataFrame from the list of temperatures for the month of December. 
dec_df = pd.DataFrame(dec_results, columns=['Date','December Temps'])
dec_df.set_index(dec_df['Date'], inplace=True)
dec_df.describe()

```

| Statistic | December Temps |       
| --- | --- |                    
|count|  1517.000000 |
|mean|  71.041529 |
|std|  3.745920 |
|min|  56.000000 |
|25%|  69.000000 |
|50%|  71.000000 |
|75%|  74.000000 |
|max|  83.000000 |



Summary:
- Temperatures are slightly lower in December as compared with June, but it should not effect the business.
- A deeper analysis would investigate precipitation in the Winter versus the Summer to see if that could have an impact on the business.

<!-- ![](surfing_dogs.gif) -->

<img src="surfing_dogs.gif" width="700" height="500">


<!-- Special Thanks to @hmlanden for syntax and formatting help. -->
