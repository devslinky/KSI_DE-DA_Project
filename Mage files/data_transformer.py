import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    df = df.drop_duplicates().reset_index(drop=True)
    df['DATE'] = pd.to_datetime(df['DATE'])

    ## Time was formated as an integer
    ## i.e. 2:36 AM would be entered as '236'

    def convert_to_time_format(time_int):
        # Convert to string and pad with zeros to ensure four digits
        time_str = str(time_int).zfill(4)
        # Extract hours and minutes
        hours = int(time_str[:-2])
        minutes = int(time_str[-2:])
        # Return formatted time as a string
        return f"{hours:02}:{minutes:02}"

    # Apply the function to the DataFrame
    df['TIME'] = df['TIME'].apply(convert_to_time_format)

    # date will be year-month-day
    df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')

    # time will be hour-minute
    df['TIME'] = pd.to_datetime(df['TIME'], format='%H:%M')

    df['PEDESTRIAN'] = df['PEDESTRIAN'].fillna('No')
    df['CYCLIST'] = df['CYCLIST'].fillna('No')
    df['AUTOMOBILE'] = df['AUTOMOBILE'].fillna('No')
    df['MOTORCYCLE'] = df['MOTORCYCLE'].fillna('No')
    df['TRSN_CITY_VEH'] = df['TRSN_CITY_VEH'].fillna('No')
    df['EMERG_VEH'] = df['EMERG_VEH'].fillna('No')

    df['SPEEDING'] = df['SPEEDING'].fillna('No')
    df['AG_DRIV'] = df['AG_DRIV'].fillna('No')
    df['REDLIGHT'] = df['REDLIGHT'].fillna('No')
    df['ALCOHOL'] = df['ALCOHOL'].fillna('No')
    df['DISABILITY'] = df['DISABILITY'].fillna('No')

    df['temp_col'] = df['TIME'].astype(str) + df['DATE'].astype(str) + df['LATITUDE'].astype(str) + df['LONGITUDE'].astype(str)
    df['accident_num'] = pd.factorize(df['temp_col'])[0]
    df = df.drop(columns=['temp_col'])

    new_df = df.groupby('accident_num').agg({
        'SPEEDING': lambda x: 'Yes' if 'Yes' in x.values else 'No',
        'AG_DRIV': lambda x: 'Yes' if 'Yes' in x.values else 'No',
        'REDLIGHT': lambda x: 'Yes' if 'Yes' in x.values else 'No',
        'ALCOHOL': lambda x: 'Yes' if 'Yes' in x.values else 'No',
        'DISABILITY': lambda x: 'Yes' if 'Yes' in x.values else 'No',
        'ACCLASS': lambda x: 'Fatal' if 'Fatal' in x.values else 'Non-Fatal Injury',
        'PEDESTRIAN': lambda x: 'Yes' if 'Yes' in x.values else 'No',
        'CYCLIST': lambda x: 'Yes' if 'Yes' in x.values else 'No',
        'AUTOMOBILE': lambda x: 'Yes' if 'Yes' in x.values else 'No',
        # Include all other columns using 'first' aggregation:
        **{col: 'first' for col in df.columns if col not in [ 'ACCNUM',"accident_num",
            'SPEEDING', 'AG_DRIV', 'REDLIGHT', 'ALCOHOL', 'DISABILITY',
            'ACCLASS', 'PEDESTRIAN', 'CYCLIST', 'AUTOMOBILE', 'OBJECTID', 'INDEX'
        ]}
    }).reset_index()

    # dropping null values in ACCNUM
    new_df = new_df.dropna(subset=['accident_num'])

    # making ACCNUM an int
    new_df['accident_num'] = new_df['accident_num'].astype(int)

    Datetime_df = new_df[["DATE","TIME"]].drop_duplicates().dropna().reset_index(drop=True)

    Datetime_df['hour'] = Datetime_df['TIME'].dt.hour
    Datetime_df['day'] = Datetime_df['DATE'].dt.day
    Datetime_df['month'] = Datetime_df['DATE'].dt.month
    Datetime_df['year'] = Datetime_df['DATE'].dt.year
    Datetime_df['minute'] = Datetime_df['TIME'].dt.minute


    # datetime table key
    Datetime_df['datetime_id'] = Datetime_df.index

    Datetime_df['date_time'] = pd.to_datetime(Datetime_df['DATE']).dt.date

    Datetime_df = Datetime_df[['datetime_id', 'hour', 'minute', 'day', 'month', 'year', "DATE","TIME"]]

    # Creating Location Table

    Location_df = new_df[["LATITUDE","LONGITUDE", "ROAD_CLASS","DISTRICT","NEIGHBOURHOOD_158"]].drop_duplicates().dropna().reset_index(drop=True)

    # Location table key
    Location_df['location_id'] = Location_df.index

    Location_df = Location_df[['location_id', 'LATITUDE', 'LONGITUDE', 'ROAD_CLASS', 'DISTRICT', 'NEIGHBOURHOOD_158']]

    # Environmental Condition Table

    Env_Con_df = new_df[["VISIBILITY","LIGHT", "RDSFCOND","TRAFFCTL"]].drop_duplicates().dropna().reset_index(drop=True)

    # Environmental table key
    Env_Con_df['env_id'] = Env_Con_df.index

    Env_Con_df = Env_Con_df[['env_id', 'VISIBILITY', 'LIGHT', 'RDSFCOND', 'TRAFFCTL']]

    # Driver Condition

    Driver_Condition_df = new_df[["SPEEDING","AG_DRIV","ALCOHOL","DISABILITY"]].drop_duplicates().dropna().reset_index(drop=True)

    # Location table key
    Driver_Condition_df['driver_con_id'] = Driver_Condition_df.index

    Driver_Condition_df = Driver_Condition_df[["driver_con_id",'SPEEDING', 'AG_DRIV',"ALCOHOL","DISABILITY"]]

    # Creating Collision Table
    collision_df = new_df.merge(Env_Con_df, on= ["VISIBILITY","LIGHT", "RDSFCOND","TRAFFCTL"], how = "inner") \
                    .merge(Location_df, on= ["LATITUDE","LONGITUDE"], how = "inner") \
                    .merge(Datetime_df, on= ["DATE","TIME"], how = "inner") \
                    .merge(Driver_Condition_df, on= ["SPEEDING","AG_DRIV","ALCOHOL","DISABILITY"], how = "inner")\
                [["accident_num","env_id", "location_id", "datetime_id","driver_con_id" ,"ACCLASS"]]

    collision_df.drop_duplicates(subset=["accident_num","env_id", "location_id", "datetime_id","driver_con_id" ,"ACCLASS"], inplace=True)
    collision_df.reset_index(drop=True, inplace=True)

    participant_df = {1:"CYCLIST", 2:"AUTOMOBILE", 3:"PEDESTRIAN"}
    participant_df = pd.DataFrame(list(participant_df.items()), columns=['participant_id', 'participant_type'])

    involvement_df = pd.melt(new_df, id_vars=['accident_num'],
                     value_vars=['CYCLIST', 'AUTOMOBILE', 'PEDESTRIAN'],
                     var_name='participant_type')

    involvement_df = involvement_df.merge(participant_df, on= ["participant_type"], how = "inner")\
                [["accident_num","participant_id"]]
    involvement_df.drop_duplicates().reset_index(drop=True, inplace=True)


    return {"Datetime_df":Datetime_df.to_dict(orient="records"),
    "Location_df":Location_df.to_dict(orient="records"),
    "Env_Con_df":Env_Con_df.to_dict(orient="records"),
    "Driver_Condition_df":Driver_Condition_df.to_dict(orient="records"),
    "collision_df":collision_df.to_dict(orient="records"),
    "participant_df":participant_df.to_dict(orient="records"),
    "involvement_df":involvement_df.to_dict(orient="records")}




@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
