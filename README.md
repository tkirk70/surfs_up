# surfs_up :surfer:
OSU Module 9 - SQLite and Flask



Overview of the analysis: 
- Explain the purpose of this analysis.


Results:
Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.


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


Summary:
- Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.

<!-- ![](surfing_dogs.gif) -->

<img src="surfing_dogs.gif" width="700" height="500">


<!-- Special Thanks to @hmlanden for syntax and formatting help. -->
