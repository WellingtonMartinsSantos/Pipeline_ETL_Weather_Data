# 🌦️ Weather ETL Pipeline – Apache Airflow

## 📋 Overview

This project implements a production-style **ETL (Extract, Transform, Load) pipeline** that collects weather data from an external [API](https://openweathermap.org/api), processes it, and stores it in a PostgreSQL database.

The workflow is fully orchestrated using **Apache Airflow** and containerized with **Docker**, following modern Data Engineering best practices.

This project demonstrates real-world data pipeline architecture suitable for analytics, reporting, and scalable data platforms.

---

## 🎯 Project Objective

The main goal of this project is to showcase:

- API data ingestion
- Modular ETL design
- Workflow orchestration with Airflow
- Containerized environments using Docker
- Data persistence in PostgreSQL
- Production-oriented configuration management

---

## 🏗️ Architecture

<img src='Modern ETL Pipeline.png' alt='Modern ETL Pipeline'>

---
- Extract: Pulls live weather data from a public API.

- Transform: Cleans and normalizes the JSON response into a tabular format.

- Load: Inserts prepared data into a Postgres table.

- Airflow: Automates and schedules the workflow.


## 🧠 Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python |
| Orchestration | Apache Airflow |
| Data Processing | Pandas |
| Database | PostgreSQL |
| Containerization | Docker & Docker Compose |
| API Integration | Requests |

---

## 📁 Project Structure
```bash
.
├── dags/
│   └── weather_data.py       # Airflow DAG definition
├── src/
│   ├── extract_data.py       # Extraction logic
│   ├── transform_data.py     # Transformation logic
│   ├── load_data.py          # Load logic
├── data/                     # Raw and output datasets
├── config/
│   └── .env                 # Environment variables
├── docker-compose.yml        # Dev & Airflow environment
└── README.md                # Project documentation
```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone git@github.com:WellingtonMartinsSantos/Pipeline_ETL_Weather_Data.git
cd Pipeline_ETL_Weather_Data
```

### 2️⃣ Configure Environment Variables

Create a .env file in the root directory:
```bash
API_KEY=YOUR_API_KEY
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=weather_db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

### 3️⃣ Start the Environment
```bash
docker compose up -d
```

### 4️⃣ Access Airflow

Open your browser and go to:
```bash
http://localhost:8080
```
Enable and trigger the DAG to start the pipeline.

---

📊 Data Output

- The pipeline stores structured weather data including:

- Timestamp

- Temperature

- Humidity

- Weather description

- City name

This data can be used for:

- Analytical dashboards

- Historical weather analysis

- Forecast modeling

- Reporting systems

---

💡 Key Data Engineering Concepts Demonstrated

- Modular ETL pipeline design

- Task orchestration with Airflow DAGs

- API integration and JSON normalization

- Containerized development environments

- Database connectivity and persistence

- Environment-based configuration

- Scalable workflow architecture

---

🚀 Potential Improvements

- Add unit and integration testing

- Implement logging and monitoring

- Add retry policies and failure alerts

- Parameterize multiple cities

- Deploy to a cloud environment (AWS/GCP/Azure)

- Add CI/CD pipeline with GitHub Actions

---

📌 Final Notes

This project reflects real-world data engineering workflows and demonstrates practical experience with:

- Airflow orchestration
- Docker-based environments
- API ingestion pipelines
- PostgreSQL integration
- Production-ready ETL structure

Designed to simulate industry-standard data engineering practices.

---

📞 Contact

#### 👨‍💻 Author : Wellington Martins Santos
#### Linkedin: [wellington-martins-santos](https://www.linkedin.com/in/wellington-martins-santos/?locale=pt)
