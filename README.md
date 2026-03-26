An end-to-end ELT (Extract, Load, Transform) pipeline built using Apache Airflow, PostgreSQL, Docker, and Python to automate e-commerce data ingestion and transformation into a star schema data warehouse.

This project demonstrates a real-world data engineering workflow where raw CSV order data is extracted, loaded into a staging area, transformed into dimension and fact tables, and made ready for analytics and reporting.

🚀 Project Overview

This pipeline automates the following process:

Raw CSV Data → Staging Table → Star Schema → Analytics

Workflow:
Extract raw e-commerce order data from CSV
Load it into a PostgreSQL staging table
Transform it into a star schema
Analyze business insights using SQL queries
Orchestrate everything using Apache Airflow DAGs
🧰 Tech Stack
Apache Airflow – workflow orchestration
Python – ETL scripting
PostgreSQL – staging + data warehouse
Docker & Docker Compose – containerized setup
Pandas – data extraction and preprocessing
SQL – schema design and transformations
📁 Project Structure
ecommerce_elt_pipeline/
├── dags/
│   └── ecommerce_elt_dag.py
├── data/
│   └── orders.csv
├── scripts/
│   ├── extract.py
│   └── transform.py
├── sql/
│   └── create_star_schema.sql
├── docker-compose.yml
├── requirements.txt
└── .env
⚙️ Architecture
orders.csv
   ↓
EXTRACT (Python)
   ↓
LOAD → staging.raw_orders
   ↓
TRANSFORM (SQL + Python)
   ↓
STAR SCHEMA
   ├── dim_date
   ├── dim_customers
   ├── dim_products
   ├── dim_location
   └── fact_orders
   ↓
ANALYTICS / SQL QUERIES
⭐ Features
Automated daily ELT pipeline
Apache Airflow DAG orchestration
Dockerized environment for easy setup
PostgreSQL staging and warehouse layers
Star schema data modeling
Business-ready analytics queries
Scalable project structure for future enhancements
🗄️ Data Warehouse Design

This project uses a Star Schema for analytical querying.

Staging Layer
staging.raw_orders
Dimension Tables
dwh.dim_date
dwh.dim_customers
dwh.dim_products
dwh.dim_location
Fact Table
dwh.fact_orders
🔄 Airflow DAG Flow

The Airflow DAG runs these tasks in sequence:

init_schema → extract_and_load_staging → transform_to_star_schema
DAG Responsibilities:
Initialize database schema
Load raw CSV data into staging
Transform staging data into dimensional warehouse tables
📊 Sample Business Insights

After the pipeline runs, you can query insights such as:

Revenue by Product Category
SELECT
    p.category,
    COUNT(*) AS total_orders,
    SUM(f.total_amount) AS total_revenue
FROM dwh.fact_orders f
JOIN dwh.dim_products p ON f.product_key = p.product_key
GROUP BY p.category
ORDER BY total_revenue DESC;
Sales by Country
SELECT
    l.country,
    COUNT(*) AS orders,
    SUM(f.total_amount) AS revenue
FROM dwh.fact_orders f
JOIN dwh.dim_location l ON f.location_key = l.location_key
GROUP BY l.country
ORDER BY revenue DESC;
🐳 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/ecommerce_elt_pipeline.git
cd ecommerce_elt_pipeline
2️⃣ Start Docker Desktop

Make sure Docker Desktop is installed and running.

3️⃣ Initialize Airflow
docker-compose up airflow-init
4️⃣ Start All Services
docker-compose up -d
5️⃣ Open Airflow UI

Go to:

http://localhost:8080
Airflow Login
Username: admin
Password: admin
6️⃣ Trigger the DAG
Turn ON the DAG: ecommerce_elt_pipeline
Click Trigger DAG
Monitor task execution in the Graph View
🧪 Verify Data

Connect to PostgreSQL Data Warehouse:

Host: localhost
Port: 5433
Database: ecommerce_dwh
User: dwh_user
Password: dwh_pass
Example Query
SELECT * FROM dwh.fact_orders;
📌 Sample Input Data

The project uses sample e-commerce order data containing:

Order details
Customer information
Product details
Location data
Payment methods
Discounts and quantities
📈 Learning Outcomes

This project helped me understand:

ELT pipeline design
Workflow orchestration with Airflow
Docker-based deployment
Data warehouse modeling
Star schema implementation
SQL-based transformations
Staging vs analytical data layers
🔮 Future Improvements

Possible enhancements for this project:

Add incremental loading
Add data quality checks
Integrate with cloud storage (AWS S3 / GCS)
Add dbt transformations
Build Power BI / Tableau dashboard
Add logging and alerting
Use Apache Spark for large-scale processing
💼 Resume / Portfolio Description

Built an Automated E-Commerce ELT Pipeline using Apache Airflow, PostgreSQL, Docker, and Python to extract raw order data, load it into a staging layer, and transform it into a star schema data warehouse for analytics and reporting.

👩‍💻 Author

Your Name
Data Engineering / Data Analytics Project

📜 License

This project is for learning and portfolio purposes.

✅ Optional Better GitHub Title

If you want your repo to look stronger, use this name:

automated-ecommerce-elt-pipeline-airflow

If you want, I can also give you:

a more attractive README with badges + screenshots section, or
a recruiter-impressive GitHub README version that looks more professional for placements.
