query4 = f'SELECT s.station,
    s.name,
    AVG(m.tobs),
    AVG(m.prcp),
    COUNT(id) AS observations 
FROM measurement m
JOIN station s
ON m.station = s.station
GROUP BY station ORDER BY COUNT(id) DESC'

new_station_summary = pd.read_sql(query4, engine)
new_station_summary
