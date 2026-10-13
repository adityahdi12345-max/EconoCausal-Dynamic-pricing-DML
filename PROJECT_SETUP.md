# Day 4: Project Environment and Setup

## 1. Objective

The objective of Day 4 is to establish a structured and reproducible development environment for the EconoCausal project.

The project will use Python for data processing, exploratory data analysis, machine learning, and causal inference.

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualizations |
| Scikit-learn | Machine learning and cross-validation |
| DoubleML | Double Machine Learning estimation |
| Statsmodels | Statistical analysis |
| Jupyter | Interactive data exploration |
| GitHub | Version control and project documentation |

## 3. Project Structure

```text
EconoCausal-Dynamic-pricing-DML/
├── data/
├── notebooks/
├── src/
├── results/
├── reports/
├── tests/
├── docs/
├── requirements.txt
├── .gitignore
├── PROJECT_OBJECTIVES.md
├── DATASET_SELECTION.md
├── DATA_DICTIONARY.md
└── PROJECT_SETUP.md
```

The data directory will contain local datasets. The notebooks directory will be used for exploratory analysis, while src will contain reusable Python scripts.

The results and reports directories will store generated outputs and project findings.

## 4. Dataset Handling

The selected candidate dataset is the Online Retail dataset from the UCI Machine Learning Repository.

The original dataset will be stored locally and excluded from Git tracking to avoid uploading a large raw data file.

The dataset must be validated before data cleaning and modelling.

## 5. Planned Development Workflow

1. Configure the Python environment.
2. Install the dependencies listed in requirements.txt.
3. Load and validate the dataset.
4. Inspect missing values, duplicates, returns, and unusual prices.
5. Perform exploratory data analysis.
6. Develop a baseline machine learning model.
7. Assess the suitability of the data for Double Machine Learning.
8. Evaluate results and document limitations.

## 6. Reproducibility

Project dependencies will be documented in requirements.txt. Analysis scripts, preprocessing decisions, and modelling assumptions will be maintained in version control.

The final project should provide clear instructions for installing dependencies and reproducing the analysis.

## 7. Expected Outcome

By the end of this setup stage, the repository will have a documented technical environment, a dependency list, and rules for excluding local datasets and temporary files.

The next stage will implement dataset loading and validation using Python and pandas.
