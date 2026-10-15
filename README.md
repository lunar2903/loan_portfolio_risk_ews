# Loan Portfolio Risk & Early Warning System

### Goal
To analyze loan portfolio risk, identify borrowers showing early signs of potential repayment difficulties, and develop an explainable Early Warning System (EWS) to support proactive credit risk monitoring.

### Code
- [Python analysis and risk monitoring scripts](src/)
- [Dataset and supporting files](data/)
- [KPI Dictionary](kpi_dictionary.md)
- [Project Starter Guide](Loan_Portfolio_Risk_EWS_Project_Starter_Guide.md)

### Description
This project examines loan-level data from a credit risk and data analytics perspective. The workflow focuses on cleaning and validating loan records, analyzing portfolio risk patterns, identifying potential warning indicators, and developing an Early Warning System to help analysts prioritize accounts for further review.

The project combines data preparation, exploratory analysis, risk KPI development, and portfolio reporting to demonstrate how analytics can support more proactive loan monitoring.

### Skills
Data cleaning, exploratory data analysis, credit risk analytics, portfolio monitoring, KPI development, statistical analysis, risk segmentation, data visualization, and business recommendations.

### Technology
Python, Pandas, SQL, statistical analysis, Power BI, DAX, and Git.

### Results
- **Portfolio risk analysis:** Evaluated loan-level data to understand portfolio characteristics and potential risk patterns.
- **Data quality:** Prepared and validated loan records to improve the reliability of downstream analysis.
- **Risk indicators:** Examined potential warning signals that can help identify accounts requiring additional review.
- **Early Warning System:** Structured a risk-monitoring approach to support prioritization of potentially higher-risk accounts.
- **KPI framework:** Documented key portfolio metrics and definitions in a dedicated KPI dictionary.
- **Business reporting:** Designed the project to translate analytical findings into actionable credit risk monitoring insights.

### Recommendations
- Monitor portfolio risk indicators regularly and investigate material changes.
- Prioritize accounts showing multiple warning signals for further review.
- Establish consistent KPI definitions to improve reporting reliability.
- Validate warning indicators against actual repayment outcomes before using them for operational decisions.
- Review flagged accounts periodically and document investigation outcomes to improve monitoring rules.

### Limitations
Risk indicators are intended to support analyst review rather than replace credit decisions. The usefulness of an Early Warning System depends on data quality, the availability of reliable repayment outcomes, and validation of warning signals. Findings should not be interpreted as proof that a borrower will default.

### Repository Structure

```text
loan_portfolio_risk_ews/
├── data/
├── src/
├── .gitignore
├── README.md
├── kpi_dictionary.md
├── kpi_dictionary.txt
├── requirements.txt
└── Loan_Portfolio_Risk_EWS_Project_Starter_Guide.md
```

### How to Run
1. Clone the repository:
   ```bash
   git clone 
   ```
2. Navigate to the project directory.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Review the starter guide for the intended workflow and execution steps.
5. Run the analysis scripts in `src/` according to their documented instructions.
6. Review the resulting risk metrics and reporting outputs.

---

**Project:** Loan Portfolio Risk & Early Warning System

**Focus:** Credit Risk Analytics · Portfolio Monitoring · Early Warning Indicators
