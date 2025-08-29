# Wafer Sensor Fault Detection

**Predict faulty semiconductor wafers using a modular ML pipeline and sensor data.**

This project develops an end-to-end solution for identifying defective wafers using sensor readings—a critical step in semiconductor manufacturing to reduce waste and automate quality control. This project helps to reduce thousand manhours of testing sensors manually.

##  Problem Statement
Semiconductor wafers go through rigorous testing to ensure quality. Faulty wafers often require costly inspection and rework. This project aims to **automate fault detection** using sensor data, enabling proactive quality assurance and efficiency gains.

##  Project Highlights & Features
- **Modular ML pipeline** with stages for data ingestion, validation, preprocessing, training, and model evaluation.
- Supports multiple classifiers (**XGBoost**, **Random Forest**, **Gradient Boosting**, **SVM**) with hyperparameter tuning via `GridSearchCV`.
- Designed for real-world application—includes configuration management, exception handling, and automated model saving for seamless deployment.

##  Architecture Overview
1. **Data Ingestion**  
   Batch-wise sensor data (wafer name + sensor readings + Good/Bad label) is ingested and validated against a schema.

2. **Data Validation**  
   - Filename and schema validation (regex-based checks)  
   - Column count, datatype, and null-value checks  
   - Segregates good/bad files for quality control

3. **Data Processing**  
   - Scaling and feature engineering for sensor metrics  
   - Prepares data for training and evaluation

4. **Model Training & Selection**  
   - Trains multiple classifiers  
   - Selects the best model using hyperparameter optimization  
   - Outputs accuracy score and saves the model as `model.pkl`

5. **Deployment-Ready**  
   - Trained model can be loaded for predictions in future pipelines or services  
   - Full CI/CD readiness through logging, robust error handling, and configuration-driven execution
