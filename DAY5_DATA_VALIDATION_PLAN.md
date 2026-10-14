# Day 5: Dataset Validation and Quality Assessment Plan

## Project: EconoCausal – Dynamic Pricing via Double Machine Learning

### 1. Objective

The objective of Day 5 is to prepare a systematic approach for validating the Online Retail dataset before performing data cleaning, exploratory data analysis, and causal modelling.

### 2. Dataset Overview

- **Dataset:** Online Retail
- **Source:** UCI Machine Learning Repository
- **Format:** Excel (.xlsx)
- **Records:** 541,909
- **Features:** 8
- **Period:** December 2010 – December 2011

### 3. Dataset Validation Strategy

The following validation tasks have been defined:

1. Verify dataset accessibility and file integrity.
2. Examine dataset dimensions and column names.
3. Validate numerical and datetime data types.
4. Identify missing values in important features.
5. Detect duplicate transaction records.
6. Investigate negative quantities and cancelled invoices.
7. Examine zero or negative unit prices.
8. Generate a structured data-quality summary.

### 4. Key Variables for Analysis

| Variable | Description | Planned Use |
|---|---|---|
| UnitPrice | Price per unit | Candidate treatment variable |
| Quantity | Units purchased | Candidate outcome variable |
| InvoiceDate | Transaction timestamp | Time-based analysis |
| StockCode | Product identifier | Product-level analysis |
| Country | Customer country | Geographic analysis |
| CustomerID | Customer identifier | Customer-level information |

### 5. Planned Python Implementation

The validation process will use:

- Pandas for loading and inspecting the dataset.
- NumPy for numerical operations.
- OpenPyXL for reading Excel files.
- Jupyter Notebook for interactive execution and documenting results.

The implementation will include dataset loading, missing-value analysis, duplicate detection, and transaction-quality checks.

### 6. Data Quality Considerations

Negative quantities may represent returns or transaction adjustments. Cancelled invoices require separate investigation.

Missing customer identifiers may affect customer-level analysis, while unusual unit prices may require further validation.

No records will be removed automatically without reviewing their meaning.

### 7. Relevance to Double Machine Learning

The project aims to investigate whether product prices influence purchasing quantities.

Before applying Double Machine Learning, the dataset must be assessed for sufficient price variation and suitable observed confounding variables.

The presence of price and quantity information alone does not establish a causal relationship.

### 8. Current Development Status

**Completed:**
- Identified the dataset and documented its structure.
- Defined the validation checks and their purpose.
- Prepared the technical approach for Python implementation.

**Pending:**
- Completion of the local Jupyter Notebook setup.
- Execution of the dataset validation code.
- Verification of the actual data-quality results.
- Saving the executed notebook and validation report.

### 9. Next Steps

1. Complete Jupyter Notebook installation.
2. Create the dataset validation notebook.
3. Execute Python validation checks.
4. Review and document the outputs.
5. Commit the executed notebook and generated reports.

### 10. Conclusion

Day 5 establishes the dataset validation methodology for the EconoCausal project.

The validation plan provides a foundation for the next development stage. Actual implementation and verification will follow once the Python environment is available.
