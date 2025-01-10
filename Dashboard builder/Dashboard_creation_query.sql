CREATE OR REPLACE TABLE `ksi-project-447300.ksi_de_proj.tbl_analytics` AS (
SELECT 
c.accident_num,
c.ACCLASS,
dc.SPEEDING,
dc.AG_DRIV,
dc.ALCOHOL,
dc.DISABILITY,
e.VISIBILITY,
e.LIGHT,
e.RDSFCOND,
e.TRAFFCTL,
l.LATITUDE,
l.LONGITUDE,
l.ROAD_CLASS,
l.DISTRICT,
l.NEIGHBOURHOOD_158,
d.year,
d.month,
d.day,
d.hour,
d.minute,

FROM 

`ksi-project-447300.ksi_de_proj.collision_df` c
JOIN `ksi-project-447300.ksi_de_proj.Datetime_df` d  ON d.datetime_id=c.datetime_id
JOIN `ksi-project-447300.ksi_de_proj.Driver_Condition_df` dc  ON dc.driver_con_id=c.driver_con_id  
JOIN `ksi-project-447300.ksi_de_proj.Env_Con_df` e  ON e.env_id=c.env_id  
JOIN `ksi-project-447300.ksi_de_proj.Location_df` l ON l.location_id=c.location_id  )
;