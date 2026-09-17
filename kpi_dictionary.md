Loan Portfolio Risk & Early Warning System

Banking-Focused Data Analyst Portfolio Project
Project Starter & Knowledge Blueprint

Version 1.0 • September 2026

1. Project at a Glance

The project simulates a bank's credit-risk analytics environment. The system will monitor a loan portfolio, identify where risk is concentrated, detect deterioration through delinquency and migration patterns, identify early-warning accounts, estimate expected credit loss using PD/LGD/EAD concepts, and present decision-oriented insights in Power BI.

2. The Core Business Question

Every major analysis in the project should help answer one of these questions:

How large is the portfolio and how is exposure distributed?

Where is current delinquency/non-performance concentrated?

Is credit quality improving or deteriorating?

Which borrowers or segments are showing early warning signals?

Are recent loan vintages performing worse than older cohorts?

How are loans migrating between delinquency states?

What is the probability of default?

How much could the bank lose if default occurs?

Which accounts/segments should receive attention first?

3. Learning & Build Roadmap

4. Banking Knowledge Already Covered

5. Remaining Theory Required Before Full Build

5.1 Credit Risk Fundamentals

Probability of Default (PD): probability that a defined default event occurs within a specified horizon.

Observed default rate vs modeled PD: an observed historical rate is not automatically a forecast probability.

Default definition: the target must be defined before modeling; the definition, observation window and performance window must be explicit.

Loss Given Default (LGD): proportion of exposure expected to be lost after considering recoveries and relevant costs/assumptions.

Exposure at Default (EAD): exposure expected to be outstanding when default occurs; for some products it can differ from today's balance.

Recovery rate: proportion recovered after default; recovery timing and costs matter.

Expected Credit Loss (ECL): forward-looking expected loss concept. A simplified portfolio illustration is PD × LGD × EAD, but a production ECL calculation can be considerably more granular and discounted over time.

Unexpected loss: variation around expected loss and a capital/risk-management concept; not the same as ECL.

5.2 Early Warning Systems

Leading indicators vs lagging indicators.

Behavioral deterioration: DPD increase, missed payments, EMI bounce, repeated delinquency, utilization changes.

Credit-profile deterioration: score decline, rising debt burden, new credit exposure.

Trigger design: single triggers vs combinations of signals.

Risk bands and prioritization: low, watch, high, critical — clearly labeled as project-specific unless backed by policy/regulation.

False positives and false negatives: an EWS is a prioritization system, not a guarantee of default.

Monitoring cadence and escalation logic.

5.3 Credit Risk Modeling

Define the observation date and prediction/performance window before creating the target.

Avoid data leakage: features must represent information available at the observation date.

Use a time-aware/out-of-time validation strategy rather than relying only on random train/test splitting.

Understand class imbalance and why accuracy is not a sufficient metric.

Evaluate precision, recall, ROC-AUC, PR-AUC, confusion matrix and probability calibration.

Select a classification threshold based on business consequences, not convenience.

Prefer an interpretable baseline such as logistic regression before comparing more complex models.

Document why the final model is appropriate for a portfolio-risk use case.

5.4 IFRS 9 — Focused Foundation

Understand the three-stage impairment framework conceptually.

Stage 1: performing exposures generally use 12-month ECL.

Stage 2: exposures with significant increase in credit risk generally use lifetime ECL.

Stage 3: credit-impaired exposures generally use lifetime ECL, with interest recognition treatment differing from Stages 1 and 2.

Understand Significant Increase in Credit Risk (SICR) as a change in credit risk since initial recognition, not simply a current delinquency snapshot.

Do not claim that this portfolio project is an IFRS 9 implementation. It is an analytical demonstration inspired by relevant credit-risk concepts.

6. Proposed Data Architecture

The project should use a small relational model rather than one giant flat CSV. The monthly performance table is especially important because migration, vintage and early-warning analytics require time-series observations.

6.1 Core relational structure

customers
   │
   └──< loans
           │
           ├──< loan_monthly_performance
           ├──< payments
           ├──< recoveries
           └──< risk_outputs

branches ───< loans

6.2 Customer table

6.3 Loan table

6.4 Monthly performance table

7. Synthetic Data Design

The project should use synthetic data so that the full pipeline can be shared publicly without exposing private customer information. The synthetic data should be designed to contain realistic relationships rather than purely random values.

Create enough loans to support segmentation and time-series analysis (for example, tens of thousands of loans rather than a few hundred).

Create multiple origination vintages across at least 24–36 months.

Create monthly performance snapshots so each loan has a longitudinal history.

Include several products with materially different risk profiles.

Include geographic and branch variation.

Create realistic credit-score, income, loan-size and debt-burden distributions.

Inject behavioral deterioration patterns such as rising DPD and repeated EMI bounces before some defaults.

Include cures, prepayments, write-offs and recoveries so the portfolio does not behave unrealistically.

Document every synthetic relationship; do not present generated relationships as empirical banking facts.

8. KPI Dictionary — Initial Version

9. Early Warning System Design

The EWS should combine transparent rule-based indicators first. A predictive model can be added later. This makes the system explainable and useful even before machine learning is introduced.

9.1 Example project scoring framework

Use illustrative points only. These thresholds must be labeled as project assumptions, not bank policy.

Suggested risk bands for demonstration: 0–19 Low, 20–39 Watch, 40–59 High, 60+ Critical. These are project-specific and should be tuned using business logic and validation rather than presented as universal standards.

10. PD, LGD, EAD & Expected Loss

10.1 PD

PD answers: 'What is the probability that this borrower/account experiences our defined default event within the specified horizon?' The definition of default and the prediction horizon must be written before modeling.

10.2 LGD

LGD answers: 'If default occurs, what proportion of the exposure is expected to be lost after considering recoveries and relevant costs/assumptions?' A simplistic 1 – recovery rate relationship can be insufficient because recovery timing, costs, collateral, discounting and exposure definitions can matter.

10.3 EAD

EAD answers: 'How much exposure is expected to be outstanding when default occurs?' It may differ from today's outstanding balance, particularly for products where borrowers can draw additional amounts.

10.4 Expected Loss

Simplified illustration: Expected Loss ≈ PD × LGD × EAD

Example: if PD = 5%, LGD = 40%, and EAD = ₹10,00,000, the simplified expected loss is ₹20,000. In production settings, ECL can be more granular, time-dependent, discounted, scenario-weighted and governed by accounting/regulatory methodology.

11. Predictive Modeling Blueprint

11.1 Target design

Choose an observation date t.

Define a performance window after t (for example, a future 12-month period for demonstration).

Define exactly what counts as default during that window.

Only use features that were available at or before t.

Exclude post-default information from predictors.

11.2 Example target

default_12m = 1
if defined_default_event occurs within 12 months after observation_date
else 0

11.3 Candidate features

Credit score at observation date

Income

Debt-to-income ratio

Loan-to-income ratio

Outstanding balance

Months on book

DPD history

Maximum DPD over previous 3/6 months

Number of EMI bounces

Recent delinquency flag

Number of active loans

Utilization

Product type

Geography

Vintage

Channel

11.4 Modeling sequence

Build a simple baseline.

Train interpretable logistic regression.

Evaluate with a time-aware validation design.

Compare against a nonlinear model such as gradient boosting.

Compare discrimination, calibration and operational usefulness.

Choose a threshold based on business consequences.

Explain the model and its limitations.

12. Model Evaluation

13. SQL Workstream

13.1 SQL skills demonstrated

JOINs and relational modeling

CASE expressions

GROUP BY and conditional aggregation

Window functions such as LAG/LEAD

Date arithmetic

CTEs

Rolling/lagged features

Cohort calculations

Data-quality checks

Exposure-weighted metrics

14. Python Workstream

15. Power BI Dashboard Blueprint

16. Recommended Repository Structure

loan-portfolio-risk-ews/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── dictionary/
│
├── sql/
│   ├── 01_data_quality.sql
│   ├── 02_portfolio_metrics.sql
│   ├── 03_segmentation.sql
│   ├── 04_roll_rates.sql
│   ├── 05_vintage.sql
│   ├── 06_ews_features.sql
│   ├── 07_model_dataset.sql
│   └── 08_risk_outputs.sql
│
├── python/
│   ├── 01_data_generation.py
│   ├── 02_data_quality.py
│   ├── 03_eda.py
│   ├── 04_feature_engineering.py
│   ├── 05_ews_scoring.py
│   ├── 06_pd_model.py
│   ├── 07_model_evaluation.py
│   └── 08_expected_loss.py
│
├── notebooks/
│
├── powerbi/
│   └── Loan_Risk_EWS.pbix
│
├── docs/
│   ├── concepts.md
│   ├── kpi_dictionary.md
│   ├── data_dictionary.md
│   ├── methodology.md
│   ├── assumptions.md
│   └── limitations.md
│
└── outputs/
    ├── figures/
    └── model_results/

17. Modeling & Analytical Decisions We Must Justify

18. Limitations — Must Be in the README

The dataset is synthetic and does not represent any real bank, customer or portfolio.

Synthetic relationships are designed for analytical demonstration and should not be interpreted as empirical banking findings.

The project is not a production credit-risk model.

PD estimates are illustrative and require real bank data, robust default definitions, sufficient sample sizes, out-of-time validation, calibration and model governance in production.

LGD and EAD assumptions are simplified unless a richer recovery/drawdown simulation is implemented.

ECL is an analytical demonstration, not a claim of IFRS 9 compliance.

Regulatory classifications and thresholds must be checked against the applicable, current regulatory framework before being presented as regulatory facts.

A production EWS would require governance, monitoring, data lineage, model validation, policy ownership, access controls and operational integration.

19. Regulatory & Accounting Reference Notes

Because the project is banking-focused and the user is based in India, use RBI material for Indian prudential terminology and official IFRS Foundation material for IFRS 9 concepts. Do not rely on memory for current regulatory thresholds.

RBI material describes SMA categories and NPA classification under its prudential framework. The current RBI regulatory framework should be checked before implementation or publication.

RBI's published handbook material describes SMA-0, SMA-1 and SMA-2 and shows the >90-day overdue criterion for NPA for relevant loan categories, with special rules for certain facilities. This project should simplify only after explicitly documenting the simplification.

IFRS 9 uses a forward-looking expected-credit-loss impairment model and a three-stage approach in its general impairment framework.

IFRS 9 Stage 1 generally uses 12-month ECL, while Stages 2 and 3 use lifetime ECL; Stage 3 is credit-impaired and has different interest-revenue treatment.

Primary references used while preparing this guide:

Reserve Bank of India — Handbook on Regulations at a Glance (IRACP/SMA/NPA reference): https://website.rbi.org.in/documents/d/rbi/handbookg27022025d0f3f53f5d3c4310a6bb2f8ac2175d3a

Reserve Bank of India — Prudential norms / asset classification reference: https://www.rbi.org.in/upload/notification/pdfs/59027.pdf

IFRS Foundation — IFRS 9 Financial Instruments: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/

IFRS Foundation — IFRS 9 supporting material: https://www.ifrs.org/supporting-implementation/supporting-materials-by-ifrs-standards/ifrs-9/

20. Interview Preparation Questions

Why isn't NPA ratio alone sufficient to assess portfolio risk?

What is the difference between account delinquency and exposure delinquency?

Why do we need roll-rate analysis?

What does a migration matrix tell a risk manager?

Why is vintage analysis more informative than a simple monthly trend in some situations?

What is MOB and why do we compare vintages at the same MOB?

What is the difference between PD, default rate and predicted probability?

Why isn't LGD simply 1 minus recovery rate in every practical setting?

What is EAD and why can it differ from current outstanding balance?

Why use PD × LGD × EAD?

How would you define a default target for a predictive model?

Why is random train/test splitting potentially problematic for credit-risk data?

Why isn't accuracy an adequate model metric for default prediction?

When would precision matter more than recall, and vice versa?

Why did you use logistic regression as a baseline?

How did you choose the EWS thresholds?

What is data leakage in a credit-risk model?

What is SICR in IFRS 9?

How is Stage 2 different from Stage 1?

What are the limitations of your synthetic dataset?

What would you need to change before deploying this system in a real bank?

21. Definition of Done

22. First Build Sprint — Exact Sequence

Finalize project scope and business questions.

Create the data dictionary before generating data.

Design customers, loans, branches, monthly performance, payments and recoveries tables.

Generate synthetic data with 24–36 months of origination/performance history.

Run data-quality checks and create a clean analytical layer.

Write SQL for portfolio exposure, delinquency and segmentation.

Create roll-rate and migration analyses.

Create vintage/MOB analyses.

Design the rule-based EWS and validate whether it surfaces deliberately injected deterioration.

Build PD target definition and point-in-time modeling dataset.

Train logistic regression baseline.

Evaluate against a nonlinear model.

Build simplified PD/LGD/EAD expected-loss layer.

Create Power BI dashboard.

Write README, methodology, assumptions and limitations.

Prepare portfolio findings and interview answers.

Appendix A — Quick Glossary

Purpose of this document / This is the master guide for building the project from scratch. It combines the banking concepts already covered, the remaining theory required, the analytical methodology, data architecture, KPI definitions, SQL/Python/Power BI plan, modeling strategy, assumptions, limitations, and interview preparation. Treat it as the project specification and study guide.

Layer | Purpose | Primary tools

Business problem | Define what the bank needs to know and why | Documentation

Data foundation | Create realistic synthetic customer, loan and monthly performance data | Python / SQL

Portfolio analytics | Measure exposure, delinquency, NPA, concentration and trends | SQL / Python

Migration & vintage | Understand movement between risk states and cohort performance | SQL / Python

Early warning | Flag deterioration before severe default | SQL / Python

Credit risk model | Estimate probability of default | Python / statistics / ML

Expected loss | Translate risk into potential monetary loss | Python / SQL

Decision layer | Communicate portfolio health and actions | Power BI

Documentation | Explain methodology, assumptions, limitations and decisions | Markdown / README

Central project question / Where is credit risk building in the loan portfolio, why is it building, which exposures are showing early signs of deterioration, how much exposure could be affected, and what should the bank prioritize?

Stage | Status / objective | What you must know

1. Banking fundamentals | Completed | Banking, loans, principal, interest, EMI, portfolio, credit risk

2. Loan performance | Completed | DPD, delinquency, default, NPA, SMA, cure, recovery, write-off

3. Portfolio analytics | Completed / finalizing | Exposure, delinquency ratios, segmentation, concentration, roll rates, migration, vintage, MOB

4. Credit risk fundamentals | Next | PD, LGD, EAD, recovery, expected loss, default definitions

5. Early Warning System | Next | Leading indicators, triggers, risk scoring, watchlists, thresholds

6. Credit risk modeling | Next | Target definition, logistic regression, imbalance, AUC, precision/recall, calibration, OOT validation

7. IFRS 9 concepts | Focused foundation | ECL, Stage 1/2/3, SICR, 12-month vs lifetime ECL

8. Data architecture | Build | Tables, keys, monthly snapshots, data dictionary

9. Analytics implementation | Build | SQL, Python, QA, features, EWS, PD, ECL

10. Dashboard & portfolio story | Build | Power BI pages, drilldowns, decisions, actions

11. Documentation & interview prep | Final | README, methodology, limitations, why-questions

Recommended approach / Do not finish all banking theory before touching the project. Learn each concept, immediately connect it to the dataset and analysis, then implement it. This prevents the project from becoming either a tutorial clone or a theory-only exercise.

Concept | Meaning | How it will appear in the project

Loan portfolio | Collection of loans held by the bank | Portfolio exposure and segmentation

Outstanding principal | Principal still owed | Exposure denominator / EAD inputs

DPD | Days past due | Monthly performance and risk states

Delinquency | Payment obligation not met on time | 30+/60+/90+ metrics and EWS

NPA | Non-performing classification under applicable framework | Portfolio asset-quality monitoring

SMA | Early-stress classification under applicable Indian regulatory framework | Early warning / regulatory context

Default | Defined credit event under a chosen framework | Model target variable

Cure | Movement from delinquency toward performing/current | Migration and collections analysis

Recovery | Cash/exposure recovered after stress/default | LGD/recovery analysis

Write-off | Accounting/operational recognition that an exposure is written off | Loss and recovery lifecycle

Segmentation | Grouping loans into meaningful categories | Product, geography, score, vintage, branch

Concentration | Share of exposure in a segment | Concentration-risk analysis

Roll rate | Movement from one delinquency bucket to another | Migration matrices

Vintage | Origination cohort used for performance comparison | Vintage curves

MOB | Months on book / age since origination | Fair cohort comparisons

Table | Grain | Purpose | Key fields

customers | 1 row per customer | Customer demographics and financial profile | customer_id

loans | 1 row per loan | Origination and contractual information | loan_id, customer_id

loan_monthly_performance | 1 row per loan per month | Repayment behavior and risk state | loan_id, snapshot_date

payments | 1 row per payment/transaction | Payment history and bounce behavior | payment_id, loan_id

recoveries | 1 row per recovery event | Recovery after default/stress | recovery_id, loan_id

branches | 1 row per branch | Geographic/organizational hierarchy | branch_id

risk_outputs | 1 row per loan per observation date | EWS and model outputs | loan_id, observation_date

Field | Type | Description

customer_id | string | Unique customer identifier

age | integer | Customer age at origination

employment_type | category | Salaried / self-employed / business etc.

annual_income | numeric | Annual income used for analytical features

employment_tenure_months | integer | Employment tenure

city | string | Customer city

state | string | Customer state

credit_score_at_origination | integer | Score at origination

existing_customer_flag | boolean | Existing vs new-to-bank indicator

Field | Type | Description

loan_id | string | Unique loan identifier

customer_id | string | Customer foreign key

loan_type | category | Home / personal / auto / education / consumer etc.

loan_amount | numeric | Original sanctioned/disbursed amount depending on definition

interest_rate | numeric | Contractual annual rate

tenure_months | integer | Contractual tenure

origination_date | date | Loan origination date

maturity_date | date | Contractual maturity date

branch_id | string | Origination/servicing branch

channel | category | Branch / digital / partner etc.

Field | Type | Description

loan_id | string | Loan foreign key

snapshot_date | date | Month-end observation date

principal_outstanding | numeric | Outstanding principal at snapshot

interest_outstanding | numeric | Interest outstanding, if modeled

emi_due | numeric | Scheduled payment due

payment_received | numeric | Payment received in the relevant period

dpd | integer | Days past due under project definition

dpd_bucket | category | Current / 1-30 / 31-60 / 61-90 / 90+

emi_bounce_flag | boolean | Payment attempt failed

credit_score | integer | Current/available score for monitoring

employment_status | category | Current employment state

loan_status | category | Current / delinquent / default / closed etc.

Synthetic-data rule / We should deliberately create patterns that are analytically discoverable, but we must never claim that those patterns represent actual Indian banking behavior. The README must clearly state that the data is synthetic.

KPI | Definition | Analytical use

Outstanding Exposure | Sum of relevant outstanding loan exposure at a snapshot | Portfolio size / denominator

Account Count | Number of active loans/accounts in the population | Scale and account-based rates

Average Ticket Size | Exposure divided by account count | Loan-size profile

30+ DPD Exposure | Exposure associated with loans at least 30 days past due under the project definition | Early/severe delinquency monitoring

60+ DPD Exposure | Exposure associated with loans at least 60 DPD | More severe delinquency

90+ DPD Exposure | Exposure associated with loans at least 90 DPD | Severe delinquency / NPA-related monitoring

Exposure Delinquency Rate | Delinquent exposure divided by relevant total exposure | Exposure-weighted asset quality

Account Delinquency Rate | Delinquent accounts divided by relevant account population | Borrower/account breadth of stress

NPA Ratio | NPA exposure divided by relevant loan exposure according to the defined framework | Asset quality

Concentration % | Segment exposure divided by total exposure | Concentration risk

Roll Rate | Share of prior-state population moving to a specified next state | Migration / deterioration

Cure Rate | Share of delinquent population moving to a healthier state | Collections/portfolio healing

Vintage Delinquency | Delinquency measure for a cohort at a given MOB | Origination quality

MOB | Months elapsed since origination | Comparable cohort aging

PD | Probability of a defined default event over a specified horizon | Forward-looking risk

LGD | Expected proportion of exposure lost after default, considering recoveries/cost assumptions | Loss severity

EAD | Exposure expected to be outstanding at default | Exposure base for expected loss

Expected Loss | Forward-looking expected credit loss; simplified illustration PD × LGD × EAD | Monetary risk

EWS Score | Project-specific score combining defined warning signals | Prioritization

Signal family | Example signal | Why it matters

Delinquency | DPD increased materially | Direct behavioral deterioration

Migration | Current → 1–30 or 1–30 → 31–60 | Movement toward worse states

Payment behavior | Repeated EMI bounce | Payment stress

Re-delinquency | Cured then delinquent again | Instability / recurring stress

Credit profile | Credit score decline | Potential deterioration in credit quality

Debt burden | DTI rises | Reduced repayment capacity

Exposure | Rapid outstanding/exposure increase | Potential leverage growth

Utilization | High utilization | Potential liquidity/credit stress

Vintage | New cohort materially worse at same MOB | Origination-quality signal

Signal | Illustrative points

DPD > 0 | 10

DPD > 30 | 20

DPD increased sharply month-over-month | 15

Recent EMI bounce | 15

Repeated delinquency | 15

Credit score decline above project threshold | 10

High DTI | 10

High utilization | 10

Critical distinction / A historical default rate is an observed outcome. PD is a probability estimate for a defined future event and population. A model's predicted PD should not be treated as a universal truth or as the same thing as a raw portfolio default rate.

Metric | What it tells us | Why it matters

Accuracy | Overall proportion correctly classified | Can be misleading with class imbalance

Precision | Of flagged borrowers, how many actually defaulted | Useful when review capacity is limited

Recall | Of actual defaults, how many were captured | Useful when missing risky borrowers is costly

ROC-AUC | Ranking/discrimination across thresholds | Common model comparison metric

PR-AUC | Precision-recall tradeoff | Useful with imbalanced outcomes

Confusion matrix | TP/FP/TN/FN counts | Makes business errors tangible

Calibration | Whether predicted probabilities match observed frequencies | Important when PD is interpreted as a probability

Interview rule / Never say 'the model is good because accuracy is 95%.' Explain the class balance, the cost of false negatives vs false positives, the chosen threshold, and whether probabilities are calibrated.

Script | Purpose

01_data_quality.sql | Duplicates, missing keys, invalid dates, negative/invalid balances, rule checks

02_portfolio_metrics.sql | Exposure, accounts, ticket size, delinquency, NPA-related metrics

03_segmentation.sql | Product, geography, score, income, branch analysis

04_roll_rates.sql | Previous vs current DPD bucket and migration matrix

05_vintage.sql | Vintage, MOB, cohort performance

06_ews_features.sql | Behavioral triggers and monitoring features

07_model_dataset.sql | Point-in-time modeling dataset with leakage controls

08_risk_outputs.sql | Join model/EWS outputs back to portfolio reporting

Script/notebook | Purpose

01_data_generation.py | Generate synthetic customers, loans, payments and monthly performance

02_data_quality.py | Validate and clean data

03_eda.py | Portfolio exploration and distributions

04_feature_engineering.py | DPD history, MOB, DTI, utilization, behavioral features

05_ews_scoring.py | Rule-based early warning score

06_pd_model.py | Train baseline and comparison models

07_model_evaluation.py | Metrics, threshold analysis, calibration, feature analysis

08_expected_loss.py | PD/LGD/EAD and loss scenarios

Page | Purpose | Core visuals

1. Executive Risk Overview | One-page portfolio health | Exposure, delinquency, NPA, EWS exposure, trends

2. Portfolio Segmentation | Find concentration | Product/geography/branch/score breakdowns

3. Delinquency & Migration | Understand deterioration | DPD trend, migration matrix, roll rates

4. Vintage Analysis | Compare origination cohorts | Vintage curves, MOB heatmap

5. Early Warning | Prioritize risk | High-risk accounts, trigger distribution, exposure at risk

6. PD / Expected Loss | Quantify forward-looking risk | PD bands, LGD, EAD, expected loss

7. Model Performance | Explain model quality | ROC/PR, confusion matrix, calibration, threshold tradeoff

Decision | Recommended project rationale

Synthetic data | Allows public sharing and controlled demonstration of portfolio-risk patterns

Monthly loan snapshots | Required for DPD history, migration, roll rates and vintage analysis

Exposure + account metrics | Avoids misleading conclusions from account counts alone

Logistic regression baseline | Interpretable and suitable as a transparent credit-risk benchmark

Complex model comparison | Tests whether extra predictive performance justifies complexity

Time-aware validation | Reflects temporal nature of credit risk and reduces leakage from future information

Rule-based EWS first | Transparent, auditable and understandable before adding ML

Project-specific thresholds | Avoids falsely presenting invented cutoffs as regulatory/bank policy

Explicit limitations | Signals understanding of the difference between portfolio demo and production risk system

Area | Done when...

Business problem | README clearly states objective, users, questions and decisions

Data | Relational synthetic dataset has documented grain, keys and realistic time-series behavior

Quality | Automated/manual checks cover duplicates, missingness, invalid ranges and business rules

Portfolio metrics | Exposure, delinquency, NPA-related metrics and concentration are reproducible

Migration | Account and exposure migration matrices are reproducible

Vintage | Vintage/MOB analysis compares cohorts at consistent ages

EWS | Signals, scoring logic and assumptions are documented

PD model | Target, features, validation, metrics and threshold are documented

Expected loss | PD/LGD/EAD methodology and assumptions are explicit

Dashboard | Each page answers a business question and supports drilldown

Documentation | Concepts, KPI dictionary, methodology, assumptions and limitations are included

Interview prep | You can explain every major choice and its trade-offs without reading the code

Immediate next step / Before generating any data, we should finish the next theory block: PD, LGD, EAD and Expected Loss. Those concepts determine several fields in the data model and prevent us from designing the dataset incorrectly.

Term | Plain-English meaning

Account | A loan/facility record being monitored.

Advance | Credit extended by a bank; terminology varies by context.

DPD | Days Past Due.

Delinquency | Failure to meet an obligation by its due date.

Default | A defined credit event indicating failure to meet obligations under a specified framework.

NPA | Non-Performing Asset under the applicable prudential classification framework.

SMA | Special Mention Account; early-stress classification in applicable Indian regulatory contexts.

PD | Probability of Default.

LGD | Loss Given Default.

EAD | Exposure at Default.

ECL | Expected Credit Loss.

MOB | Months on Book.

Vintage | Origination cohort used for performance comparison.

Roll Rate | Rate of movement from one delinquency state to another.

Cure | Movement from a delinquent state toward a healthier/current state.

Exposure | Financial amount subject to the risk being measured; exact definition depends on the metric.

Concentration | Share of portfolio exposure concentrated in a segment.

SICR | Significant Increase in Credit Risk.

EWS | Early Warning System.

Out-of-time validation | Validation on a later time period than the training data.

Data leakage | Use of information in model features that would not have been available at the prediction time.