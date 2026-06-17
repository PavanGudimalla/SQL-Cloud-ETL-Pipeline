# SQL-Cloud-ETL-Pipeline

## Project Overview
This project involves the development of a scalable, automated ETL (Extract, Transform, Load) pipeline designed to process and integrate traffic and weather data. By leveraging cloud infrastructure, the pipeline provides a reliable stream of processed data for downstream analytics and predictive modeling, enabling insights into the correlation between weather patterns and traffic congestion.

## Tech Stack & Tools
- **Python**: Used for data extraction from APIs and for implementing complex transformation logic.
- **SQL**: Utilized for data modeling and managing the structured data storage within the cloud environment.
- **Microsoft Azure**: The primary cloud platform, utilizing services like Azure Data Factory, Azure SQL Database, and Azure Functions for orchestration and storage.
- **APIs**: Sourced real-time data from various traffic and weather service providers.

## Methodology
The pipeline architecture follows a robust data engineering workflow:
1. **Data Ingestion**: Automated Python scripts scheduled as Azure Functions to fetch real-time data from external APIs.
2. **Staging**: Storing raw data in Azure Blob Storage before processing.
3. **Transformation**: Using SQL and Python to clean, normalize, and aggregate traffic and weather datasets into a unified schema.
4. **Loading**: Efficiently loading processed data into a production-ready Azure SQL Database.
5. **Orchestration**: Managing the end-to-end workflow using Azure Data Factory to ensure high availability and error handling.
6. **Scalability Testing**: Optimizing the pipeline to handle increasing data volumes and peak ingestion rates.
