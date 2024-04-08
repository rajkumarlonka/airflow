# Define the default arguments for the DAG
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG('dbt_dag_with_params', default_args=default_args, schedule_interval=timedelta(days=1))
# Define the dbt run command with a parameter named "dataset"
run_dbt_model_with_params = BashOperator(
    task_id='run_dbt_model_with_params',
    bash_command='dbt run --var dataset=my_dataset',
    dag=dag
)