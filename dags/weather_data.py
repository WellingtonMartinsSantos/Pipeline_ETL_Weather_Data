from datetime import datetime, timedelta
from airflow.sdk import dag, task
from pathlib import Path
import sys, os

#sys.path.insert(0,'/opt/aiflow/src')

from src.extract_data import extract_weather_data
from src.transform_data import data_transformations
from src.load_data import load_weather_data
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

APY_KEY = os.getenv('API_KEY')
url =f'http://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={APY_KEY}'

@dag(
        dag_id = 'well_weather_pipeline',
        default_args ={
            'owner' : 'airflow',
            'depends_on_past' : False,
            'retries' : 2,
            'retry_delay' : timedelta(minutes=5)
        },
        description = 'Pipeline ETL - Clime SP',
        schedule = '0 */1 * * * ',
        start_date = datetime(2026,2,7),
        catchup = False,
        tags = ['weather', 'etl', 'Joinha']
    )
def weather_pepiline():

    @task
    def extract():
        extract_weather_data(url)
    
    @task
    def transform():
        df = data_transformations()
        df.to_parquet('/opt/airflow/data/temp_data.parquet', index=False)
    
    @task
    def load():
        import pandas as pd
        df = pd.read_parquet('/opt/airflow/data/temp_data.parquet')
        load_weather_data('sp_weather',df)


    extract() >> transform() >> load()

weather_pepiline()