# Day 3: Dataset Analysis and Data Dictionary

## 1. Project Overview

*Project Name:* EconoCausal – Dynamic Pricing via Double Machine Learning (DML)

The objective of this project is to investigate the relationship between product prices and purchase quantities and evaluate whether Double Machine Learning can help estimate the causal effect of pricing decisions.

## 2. Dataset Information

- *Dataset Name:* Online Retail
- *Source:* UCI Machine Learning Repository
- *Dataset URL:* https://archive.ics.uci.edu/dataset/352/online+retail
- *File Name:* Online Retail.xlsx
- *File Format:* Excel
- *Total Records:* 541,909
- *Total Columns:* 8
- *Date Range:* 1 December 2010 to 9 December 2011

The dataset contains transaction-level records from an online retailer, including product information, purchase quantities, unit prices, transaction dates, customer identifiers, and countries.

## 3. Dataset Structure

The dataset contains the following columns:

| Column | Description | Potential Role |
|---|---|---|
| InvoiceNo | Invoice or transaction identifier | Identifier |
| StockCode | Product code | Product identifier |
| Description | Product description | Product information |
| Quantity | Number of units in a transaction | Candidate outcome |
| InvoiceDate | Date and time of transaction | Time variable |
| UnitPrice | Unit price in GBP | Candidate treatment |
| CustomerID | Customer identifier | Customer information |
| Country | Customer's country | Geographic information |

## 4. Initial Data Quality Assessment

An initial inspection of the dataset produced the following findings:

- Total records: 541,909
- Total columns: 8
- Missing CustomerID values: 135,080
- Missing Description values: 1,454
- Duplicate rows: 5,268
- Records with negative Quantity: 10,624
- Records with zero UnitPrice: 2,515

These findings indicate that data cleaning and validation are necessary before modelling.

Duplicate rows will be investigated before removal. Negative quantities may represent returns or other transaction adjustments and require further investigation. Zero-price transactions will also be examined.

## 5. Preliminary Research Questions

1. How does UnitPrice vary across products?
2. How does Quantity vary over time?
3. Do prices differ for the same product across transactions?
4. How do purchasing patterns vary across countries?
5. Can the available data support a reliable causal analysis of pricing decisions?

## 6. Relevance to Double Machine Learning

For the initial analysis, UnitPrice is the candidate treatment variable and Quantity is the candidate outcome variable.

Product identity, transaction timing, and other available variables may be considered as covariates, subject to the final causal design.

However, the dataset does not directly include all potentially important factors, such as promotional campaigns, competitor prices, and inventory availability. The relationship between price and quantity alone does not establish causality.

The suitability of this dataset for Double Machine Learning will be assessed after exploratory data analysis and evaluation of the required assumptions.

## 7. Data Cleaning Plan

The following steps are planned:

1. Inspect and validate column data types.
2. Investigate missing CustomerID and Description values.
3. Review duplicate records.
4. Investigate negative quantities and cancelled transactions.
5. Examine zero and unusual UnitPrice values.
6. Analyse price variation within individual products.
7. Create suitable time-based features from InvoiceDate.
8. Document all preprocessing decisions.

## 8. Dataset Limitations

- The data represents historical transactions from 2010–2011.
- The dataset is observational rather than experimental.
- Missing customer identifiers may limit customer-level analysis.
- Returns and cancellations may affect quantity-based analysis.
- Important pricing and demand factors may not be available.
- Causal identification has not yet been established.

## 9. Next Steps

1. Complete data cleaning using Python and pandas.
2. Perform exploratory data analysis (EDA).
3. Visualise price and quantity distributions.
4. Examine variation in prices within products over time.
5. Decide how to handle returns, cancellations, and missing values.
6. Evaluate whether the dataset supports the proposed causal analysis.
7. Document the final treatment, outcome, and covariates.

## 10. Conclusion

The Online Retail dataset contains 541,909 records and eight columns, including UnitPrice, Quantity, and InvoiceDate. Initial inspection identified missing values, duplicate rows, negative quantities, and zero-price transactions.

These issues must be investigated before modelling. The next phase will focus on data cleaning and exploratory data analysis to determine whether the dataset is suitable for the EconoCausal project.

## References

1. UCI Machine Learning Repository, Online Retail Dataset.
2. https://archive.ics.uci.edu/dataset/352/online+retail
