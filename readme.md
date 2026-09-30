The project demonstrates the basic airflow pipeline possible utilizations.

Prerequisites:
1. Instal WSL2 (cli that allows communication between windows and linux in docker).
2. Install Docker Desktop version 3.3.2 locally.
Goto https://docs.docker.com/compose/
https://docs.docker.com/desktop/setup/install/windows-install/

Once installed Goto Settings->Resources->WSL Integration
check Enable integration with my default WSL distro
Also enable integration with additional distros


3. Create a the c:\airflow-docker folder
under this folder, create 3 folders: config, dags, logs
4. download the latest docker-compose.yaml 3.3.2 version into the airflow-docker folder
https://airflow.apache.org/docs/apache-airflow/3.3.2/howto/docker-compose/index.html
5. Create the .env file in the same folder with the following values:
AIRFLOW_UID=50000
AIRFLOW_GID=0
FERNET_KEY=_26J0HlKlGVo832g373U3xPnYLMt1zdpSwDVNl9pkuQ= (see on the web how to generate this key )
AIRFLOW_IMAGE_NAME=apache/airflow:3.3.2

Apache Airflow uses FERNET_KEY to encrypt sensitive credentials (like database passwords and API connection strings) 
stored in its metadata database. Leaving it blank means your connections won't be securely encrypted, 
and if Airflow autogenerates one on startup without saving it to .env, 
restarting containers can lead to decryption errors down the line.

Generate a valid Fernet key using Python (bash):
python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
otherwise
python3 -c "import base64, os; print(base64.urlsafe_b64encode(os.urandom(32)).decode())"

6. Create the xxx_dag.py files
7. Initialize airflow on 
-- Execute the next command to run all the services mentioned in the docker_compose.yaml.
-- to prevent collisions with previous airflow installations run the following script for initialization
docker compose --env-file .env down -v --remove-orphans

docker ps -aq | ForEach-Object { docker rm -f $_ }

docker volume ls
docker volume rm airflow-docker_postgres-db-volume 2>$null

docker network ls
docker network prune -f

docker compose --env-file .env up -d --force-recreate
8. Verify the status of the airflow services (processes) by running command 
docker ps

9. to verify the logs of specific services
docker compose --env-file .env ps -a
docker compose --env-file .env logs --tail=100 airflow-init
docker compose --env-file .env logs --tail=100 airflow-apiserver

10. Things to remember when working with Docker locally.
wsl