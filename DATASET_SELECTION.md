# EconoCausal: Dynamic Pricing via Double Machine Learning

# Day 2: Dataset Selection and Analysis Plan

## 1. Introduction

Dataset selection is a critical step in the EconoCausal project. The quality, completeness, and relevance of the dataset directly influence the reliability of causal effect estimation.

This project aims to investigate how product prices influence sales using Causal Inference and Double Machine Learning (DML).

The selected dataset should provide information about product prices, sales outcomes, and relevant variables that may influence both pricing decisions and customer purchasing behavior.

## 2. Objective of Dataset Selection

The main objective is to identify a suitable dataset for estimating the causal effect of product prices on sales.

The specific objectives are:

- Identify publicly available pricing and sales datasets.
- Evaluate the availability of treatment, outcome, and control variables.
- Assess dataset size, completeness, and data quality.
- Identify potential confounding variables.
- Ensure the dataset is suitable for exploratory data analysis.
- Prepare a foundation for implementing Double Machine Learning.
- Document the dataset source, structure, limitations, and selection rationale.

## 3. Dataset Requirements

The preferred dataset should contain the following information:

| Variable | Description | Role |
|---|---|---|
| Product Price | Price of a product | Treatment |
| Sales Quantity | Number of units sold | Outcome |
| Product ID | Unique product identifier | Identifier |
| Date | Date of observation | Time variable |
| Discount | Discount applied to a product | Potential control |
| Promotion | Promotional activity | Potential control |
| Competitor Price | Price charged by competitors | Potential control |
| Product Category | Category of the product | Potential control |
| Inventory Level | Available stock | Potential control |
| Demand Indicators | Variables related to customer demand | Potential control |

The actual variables will depend on the dataset selected. Not every dataset will contain all the variables listed above.

## 4. Treatment, Outcome, and Confounding Variables

### 4.1 Treatment Variable

The treatment variable represents the price of a product.

For this project, product price will be investigated as the main treatment variable.

### 4.2 Outcome Variable

The outcome variable represents the business result affected by pricing decisions.

Sales quantity is the preferred outcome variable. Revenue may also be considered if the dataset supports it.

### 4.3 Potential Confounding Variables

Confounding variables may influence both product prices and sales.

Examples include:

- Discounts and promotional campaigns
- Product category
- Seasonality
- Competitor pricing
- Inventory availability
- Marketing activity
- Day of the week
- Customer demand conditions

The final selection of control variables will depend on domain knowledge, data availability, and the causal assumptions of the analysis.

## 5. Dataset Selection Criteria

The candidate dataset will be evaluated using the following criteria:

### 5.1 Relevance

The dataset should contain meaningful information about pricing and sales.

### 5.2 Data Completeness

Important variables should have sufficient non-missing observations.

### 5.3 Data Quality

The dataset should be checked for duplicate records, inconsistent values, incorrect data types, and implausible observations.

### 5.4 Sample Size

The dataset should contain enough observations to support exploratory analysis and model estimation.

### 5.5 Feature Availability

The dataset should ideally contain variables that help explain differences in pricing and purchasing behavior.

### 5.6 Suitability for Causal Inference

The dataset should provide a reasonable basis for defining the treatment, outcome, and relevant confounders.

Observational data alone does not guarantee that causal effects can be identified. The assumptions required for causal interpretation must be evaluated.

## 6. Double Machine Learning Requirements

Double Machine Learning combines machine learning methods with causal inference to estimate treatment effects while accounting for observed confounding variables.

For this project, the dataset should ideally support the following components:

- Treatment variable: product price
- Outcome variable: sales quantity
- Covariates: relevant observed confounding variables
- Nuisance models: models used to estimate conditional relationships between covariates, treatment, and outcome
- Cross-fitting: a procedure used to reduce overfitting bias in nuisance-model estimation
- Treatment effect estimation: estimation of the effect of price on sales

The exact DML estimator and nuisance models will be selected after inspecting the dataset.

## 7. Data Quality Assessment Plan

After identifying a candidate dataset, the following checks will be performed:

1. Inspect the number of rows and columns.
2. Review column names and data types.
3. Calculate missing-value counts and percentages.
4. Identify duplicate records.
5. Check invalid or implausible price and sales values.
6. Examine numerical variable distributions.
7. Review categorical variables and their unique values.
8. Investigate potential outliers.
9. Check whether the treatment and outcome variables have sufficient variation.
10. Document any limitations that may affect the analysis.

These checks will help determine whether the dataset is suitable for further preprocessing.

## 8. Data Sources to Investigate

Potential sources of public datasets include:

- Kaggle datasets related to retail sales and product pricing.
- UCI Machine Learning Repository datasets related to retail or sales.
- Government or open-data portals containing relevant economic or retail information.
- Research datasets that provide pricing, sales, and relevant covariates.

The availability and suitability of a dataset from these sources must be verified before selection.

## 9. Dataset Comparison Framework

Candidate datasets will be compared using the following criteria:

| Criterion | Evaluation |
|---|---|
| Pricing information | Availability of product price |
| Sales information | Availability of quantity sold or revenue |
| Confounders | Availability of relevant control variables |
| Data completeness | Amount of missing data |
| Sample size | Number of usable observations |
| Documentation | Availability of a data dictionary |
| Causal suitability | Whether assumptions can reasonably be assessed |

The final dataset will be selected after comparing candidate datasets against these criteria.

## 10. Expected Outcomes

The expected outcomes of this stage are:

- Identification of one or more candidate datasets.
- A documented dataset evaluation framework.
- Identification of potential treatment, outcome, and control variables.
- Preliminary assessment of data quality.
- Documentation of dataset limitations.
- A clear plan for data preprocessing and exploratory analysis.

These are planned outcomes and will be confirmed after the dataset has been inspected.

## 11. Risks and Limitations

Potential challenges include:

- Missing pricing or sales information.
- Lack of important confounding variables.
- Limited variation in product prices.
- Inconsistent observations across dates or products.
- Selection bias and unobserved confounding.
- Insufficient information to support causal interpretation.

These limitations will be documented and considered during model development.

## 12. Next Steps

After completing dataset selection, the next stage will involve:

1. Downloading the selected dataset.
2. Recording its source and licence information.
3. Inspecting the dataset structure.
4. Performing data quality checks.
5. Cleaning missing and inconsistent values where appropriate.
6. Conducting Exploratory Data Analysis.
7. Preparing the variables required for Double Machine Learning.

## 13. Conclusion

Dataset selection provides the foundation for the EconoCausal project. A suitable dataset should contain relevant pricing, sales, and confounding information.

A systematic evaluation of data quality and causal suitability will help establish a reliable foundation for subsequent exploratory analysis and Double Machine Learning.

The final dataset and modelling strategy will be documented after the candidate data has been examined.
