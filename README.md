# Automated ETL Pipeline using Apache Airflow

This project is an **Automated ETL Pipeline** built using **Apache Airflow, Python, PostgreSQL, and Docker**.

The pipeline extracts e-commerce order data from a CSV file, loads it into a PostgreSQL staging table, and transforms it into a **star schema** for analytics and reporting.

## 🚀 Technologies Used
- Apache Airflow
- Python
- PostgreSQL
- Docker
- Pandas
- SQL

## 📌 Project Workflow
1. **Extract** raw order data from CSV  
2. **Load** data into PostgreSQL staging table  
3. **Transform** data into star schema tables  
4. **Analyze** data using SQL queries  

## 📂 Project Structure
- `dags/` → Airflow DAG files  
- `scripts/` → Python ETL scripts  
- `data/` → Raw CSV data  
- `sql/` → SQL schema creation files  
- `docker-compose.yml` → Docker setup file  

## ⭐ Features
- Automated ETL process
- Workflow scheduling with Airflow
- PostgreSQL staging and warehouse tables
- Star schema design for analytics
- Easy containerized setup using Docker

## 📊 Output
The final output is a structured data warehouse with:
- **Fact table** for order transactions
- **Dimension tables** for customer, product, date, and location

## 🎯 Purpose
This project demonstrates how to build a basic **data engineering pipeline** that automates data flow from raw files to an analytics-ready database.

## 📚 Learning Outcome
Through this project, I learned:
- ETL/ELT pipeline concepts
- Workflow orchestration using Airflow
- Data warehouse design
- SQL-based transformations
- Dockerized project setup
