from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

from random import randint
from datetime import datetime, timedelta

default_args = {
    "owner": "james bensoussan",
    "depends_on_past": False,
    "email": ["james.bensoussan@gmail.com"],
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

with DAG("dag_test"
         ,start_date =datetime(2026,9,28)
         ,schedule = "0 1 * * *"
         ,catchup=False
         ,max_active_runs=1
         ,tags=['dag_test'],) as dag:
    
    start  = EmptyOperator(
        task_id = "start"
    )

    end  = EmptyOperator(
            task_id = "end"
    )

    end << start