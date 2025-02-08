# **Football-Data-ETL-with-Apache-Airflow-PostgreSQL**

## **Overview**
This project automates the **ETL (Extract, Transform, Load) process** for historical football data using **Apache Airflow** and stores the cleaned data in a **PostgreSQL** database. The transformed data is structured for further analysis and visualization.

## **Tech Stack**
- **Apache Airflow** – Orchestrates the ETL pipeline.
- **PostgreSQL** – Stores the cleaned and processed data.
- **Docker & Docker Compose** – Containerizes and manages the services.
- **Pandas** – Handles data transformation.

## **ETL Pipeline**

### 🔹 **Extraction**
- Extracts football match data from Kaggle (CSV files).
- Loads raw data into a staging area.

### 🔹 **Transformation**
- **Handles Missing Values** – Imputes or removes nulls.
- **Data Normalization** – Scales numerical fields.
- **Feature Engineering** – Adds new metrics like goal difference.
- **Data Aggregation** – Groups data by season, team, and player.
- **Standardization** – Formats dates, team names, and match results.

### 🔹 **Loading**
- Stores the transformed data in a PostgreSQL database running inside Docker.

## **Setup & Execution**

### **Prerequisites**
- Docker & Docker Compose
- Apache Airflow
- PostgreSQL

### **Setting Up the Environment**

1. **Clone the Repository**
   ```bash
   git clone [repository-link]
   cd project-directory
   ```
2. **Run Docker Containers**
   ```bash
   docker-compose up -d --build
   ```
3. **Access Airflow UI**
   - Open [http://localhost:8080](http://localhost:8080)
   - Log in with username: `admin`, password: `admin`
4. **Trigger the ETL Pipeline**
   ```bash
   docker exec -it airflow airflow dags trigger simple_etl
   ```
5. **Verify Data in PostgreSQL**
   ```bash
   docker exec -it football-db psql -U admin -d football
   SELECT * FROM matches LIMIT 10;
   ```

## **Future Enhancements**
✅ Automate data extraction from live football APIs  
✅ Deploy visualizations to a cloud-based dashboard

