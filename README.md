# **Customer Churn Prediction System 🚀**

## 📌 Project Overview
This project predicts customer churn for a subscription-based service using an **Automated ML Pipeline** With `Frontend` and `Backend`.

## 📂 Project Structure
- `datahub/` - Machine Learning pipeline (data processing, training, monitoring)
- `app/` - Backend API (FastAPI) and Frontend (React)
- `env/` - Conda environments for ML and backend
- `deployment/` - Docker, CI/CD setup
- `docs/` - Project documentation

## 🔥 Tech Stack
- **ML & Data**: Python, Pandas, Scikit-Learn, MLflow, DVC
- **Backend**: FastAPI, PostgreSQL, Pytest
- **Frontend**: React, Chart.js, Tailwind CSS
- **Pipeline & Deployment**: Apache Airflow, Docker, GitHub Actions

## **Project Structure**:

```bash
    churnprediction-system/
    │
    ├── README.md                        # Project overview, setup instructions
    ├── pyproject.toml                    # Package installation script
    ├── .gitignore                        # Files to be ignored by git
    ├── .env-example                      # Example environment variable file
    ├── Dockerfile                        # Container definition
    ├── docker-compose.yml                # Multi-container setup
    ├── Makefile                          # Automation commands
    ├── setup_env.bat                     # Automated Conda environment setup (Windows)
    │ 
    ├── exception/
    │    ├──customException.py            # custom exception for entire project
    │
    ├── utils/
    │    ├──customLogger.py                # custom logging for entire project
    │
    ├── env/                               # Conda environments (auto-created)
    │   ├── datahub_env/                   # DataHub Conda environment
    │   └── backend_env/                   # Backend Conda environment
    │
    ├── datahub/                           # Data science components
    │   ├── environment.yml                # Conda environment file for DataHub
    │   ├── config/                         # Configuration files
    │   │   ├── model_config.yaml           # Model hyperparameters
    │   │   └── pipeline_config.yaml        # Pipeline parameters
    │   │
    │   ├── data/                           # Data storage (often gitignored)
    │   │   ├── raw/                        # Original immutable data
    │   │   ├── processed/                  # Cleaned, transformed data
    │   │   ├── interim/                    # Intermediate processing data
    │   │   └── external/                    # External data sources
    │   │
    │   ├── notebooks/                      # Jupyter notebooks
    │   │   ├── exploratory/                # EDA notebooks
    │   │   ├── modeling/                   # Model experimentation
    │   │   └── reporting/                   # Results & visualizations
    │   │
    │   ├── scripts/                        # Utility scripts
    │   │   ├── data_pipelines/             # Data processing scripts
    │   │   │   ├── ingestion.py            # Data loading
    │   │   │   ├── validation.py           # Data validation
    │   │   │   ├── cleaning.py             # Data cleaning
    │   │   │   └── feature_engineering.py  # Feature creation
    │   │   │
    │   │   ├── training_pipelines/         # Model training scripts
    │   │   │   ├── train.py                # Main training script
    │   │   │   ├── hyperparameter_tuning.py # Hyperparameter optimization
    │   │   │   └── model_selection.py      # Model comparison
    │   │   │
    │   │   ├── evaluation_pipelines/       # Model evaluation scripts
    │   │   │   ├── evaluate.py             # Metrics calculation
    │   │   │   ├── interpretation.py       # Model interpretation
    │   │   │   └── benchmark.py            # Comparison to baselines
    │   │   │
    │   │   ├── monitoring_pipelines/       # Production monitoring scripts
    │   │   │   ├── drift_detection.py      # Data/prediction drift
    │   │   │   ├── performance_tracking.py # Model performance over time
    │   │   │   └── alerting.py             # Alert system for issues
    │   │
    │   ├── src/                            # Source code package
    │   │   ├── __init__.py
    │   │   ├── data/                       # Data processing modules
    │   │   ├── models/                     # Model modules
    │   │   ├── visualization/              # Visualization modules
    │   │   └── utils/                      # Utility modules
    │   │
    │   ├── pipelines/                      # Orchestration definitions
    │   │   ├── training_pipeline.py        # Training workflow
    │   │   ├── inference_pipeline.py       # Inference workflow
    │   │   └── retraining_pipeline.py      # Retraining workflow
    │   │
    │   ├── tests/                          # Automated tests
    │   │   ├── test_data.py                # Data tests
    │   │   ├── test_models.py              # Model tests
    │   │   └── test_pipelines.py           # Pipeline tests
    │   │
    │   ├── logs/                           # Log files
    │   │   ├── training/                   # Training logs
    │   │   └── production/                 # Production logs
    │   │
    │   ├── mlflow/                         # MLflow tracking
    │   │   └── mlruns/                     # MLflow experiment runs
    │   │
    │   └── airflow/                        # Airflow workflows
    │       ├── dags/                       # DAG definitions
    │       └── plugins/                    # Plugins
    │
    ├── app/                                # Application code
    │   ├── environment.yml                 # Conda environment file for Backend
    │   ├── config/                         # App configuration
    │   │   └── app_config.yaml             # Application settings
    │   │
    │   ├── backend/                        # Backend API
    │   │   ├── __init__.py
    │   │   ├── main.py                     # FastAPI application
    │   │   ├── routes/                     # API endpoints
    │   │   ├── models/                     # Data models
    │   │   ├── services/                   # Business logic
    │   │   └── utils/                      # Utility functions
    │   │
    │   └── frontend/                        # Frontend application
    │       ├── public/                      # Static assets
    │       ├── src/                         # React source code
    │       │   ├── components/              # UI components
    │       │   ├── pages/                   # Page definitions
    │       │   ├── services/                # API integration
    │       │   └── utils/                    # Utility functions
    │       ├── package.json                 # NPM configuration
    │       └── README.md                     # Frontend documentation
    │
    ├── deployment/                          # Deployment configuration
    │   ├── docker/                          # Docker configurations
    │   ├── kubernetes/                      # Kubernetes manifests (if needed)
    │   └── scripts/                         # Deployment scripts
    │
    └── docs/                                # Documentation
        ├── architecture/                    # System architecture
        ├── data/                             # Data dictionaries
        ├── models/                           # Model documentation
        ├── pipelines/                        # Pipeline documentation
        ├── api/                              # API documentation
        ├── user_guide/                       # User documentation
```

## **Mermaid Design:**
```bash
    A User Input (Frontend - Html, Css, Js)] -->|Uploads Data / Requests Predictions| B[Backend (FastAPI API)]
    B -->|Forwards Data| C[Machine Learning Pipeline (DataHub)]
    B -->|Stores Data| D[Database (PostgreSQL)]
    C -->|Processes & Predicts| B
    C -->|Stores Predictions| D
    C -->|Tracks Model Performance| E[Monitoring & Logging (MLflow, Airflow)]
    E -->|Detects Drift & Retrains Models| C
    B -->|Sends Predictions Back| A
    B -->|Deploys Services| F[Deployment (Docker/Kubernetes/Cloud)]
```