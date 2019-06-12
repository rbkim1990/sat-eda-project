# SAT/ACT Data Exploration and Analysis

![](./images/cover.jpg)

### Background Information
- _Standardized college tests are crucial for high school seniors to access the world of college. Evaluating students across different locations, demographics, and societies through a standardized test is one of the ways that colleges can get an objective idea of how prepared a student is to succeed in college. There are two main standardized college entrance exams in the United States: the **SAT** (Scholastic Aptitude Test) and the **ACT** (American College Testing)._
- _As a past high school mathematics teacher with great interest in applying my data analyzation skills to the realm of education, analyzing the data on SAT and ACT tests is extremely relevant and meaningful for me, as well as being a great domain in which to hone my data analyzing skills._

### Problem Statement
- _The purpose of this project is to explore the various facets of both SAT and ACT tests from 2017 and 2018, to discover any interesting patterns, as well as focus in on **expanding the SAT participation rate in Alaska.**_

### Executive Summary
- Collect SAT and ACT data from 2017 and 2018 and combine with relevant state information (median income, college bound percent, population, etc.).
- Perform exploratory data analysis to understand relationships and patterns between different facets of data.
- Assess data and choose a state “market” that the College Board can expand in
- Research and analyze information about said state market and present findings

### Data Dictionary
|**Feature**|**Type**|**Dataset**|**Description**|
|---|---|---|---|
|**state**|_object_|---|The state that the average score and subscore for each test was taken|
|**2017_act_part** | _integer_ | 2017 ACT Data | The participation rate (as a percent) for each state (and District of Columbia) on the ACT in 2017|
|**2017_act_eng** | _float_ | 2017 ACT Data | The average English subscore (out of 36) for each state (and District of Columbia) on the ACT in 2017|
|**2017_act_math** | _float_ | 2017 ACT Data | The average Math subscore (out of 36) for each state (and District of Columbia) on the ACT in 2017|
|**2017_act_read** | _float_ | 2017 ACT Data | The average Reading subscore (out of 36) for each state (and District of Columbia) on the ACT in 2017|
|**2017_act_science** | _float_ | 2017 ACT Data | The average Science subscore (out of 36) for each state (and District of Columbia) on the ACT in 2017|
|**2017_act_total** | _float_ | 2017 ACT Data | The average total score (out of 36) on the ACT test for each state in 2017 |
|**2017_sat_part** | _int_ | 2017 SAT Data | The participation rate (as a percent) for each state (and District of Columbia) on the SAT in 2017|
|**2017_sat_read** | _int_ | 2017 SAT Data | The average Evidence-Based Reading and Writing subscore (out of 800) on the SAT test for each state in 2017|
|**2017_sat_math** | _int_ | 2017 SAT Data | The average Math subscore (out of 800) on the SAT test for each state in 2017|
|**2017_sat_total** | _int_ | 2017 SAT Data | The average total score (out of 1600) on the SAT test for each state in 2017|
|**2018_act_part** | _int_ | 2018 ACT Data | The participation rate (as a percent) for each state (and District of Columbia) on the ACT in 2018|
|**2018_act_total** | _float_ | 2018 ACT Data | The average total score (out of 36) on the ACT test for each state in 2018 |
|**2018_sat_part** | _int_ | 2018 SAT Data | The participation rate (as a percent) for each state (and District of Columbia) on the SAT in 2018|
|**2018_sat_read** | _int_ | 2018 SAT Data | The average Evidence-Based Reading and Writing subscore (out of 800) on the SAT test for each state in 2018|
|**2018_sat_math** | _int_ | 2018 SAT Data | The average Math subscore (out of 800) on the SAT test for each state in 2018|
|**2018_sat_total** | _int_ | 2018 SAT Data | The average total score (out of 1600) on the SAT test for each state in 2018|
|**median_income** | _int_ | 2016 US Census Data | The median income per household for each state in 2016|
|**percent_college_bound** | _float_ | 2014 NCES (National Center for Education Statistics) Data  | The percent of college-bound seniors for each state in 2014|
|**education_revenue** | _int_ | 2014-2015 NCES (National Center for Education Statistics) Data  | The total education revenue (in millions of dollars) for each state in 2014-2015|
|**2017_pop_est** | _int_ | US Census | Estimated population for each state in 2017 by extrapolation from 2010 US Census|
|**2017_sat_total_standardized** | _float_ | 2017 SAT Data | The average total score on the SAT test for each state in 2017 standardized by its mean and standard deviation|
|**2018_sat_total_standardized** | _float_ | 2018 SAT Data | The average total score on the SAT test for each state in 2018 standardized by its mean and standard deviation|
|**2017_act_total_standardized** | _float_ | 2017 ACT Data | The average total score on the ACT test for each state in 2017 standardized by its mean and standard deviation|
|**2018_act_total_standardized** | _float_ | 2018 ACT Data | The average total score on the ACT test for each state in 2018 standardized by its mean and standard deviation|
|**sat_score_pct_change** | _float_ | 2017 and 2018 SAT Data | The percent change between 2017 and 2018 SAT scores|
|**act_score_pct_change** | _float_ | 2017 and 2018 ACT Data | The percent change between 2017 and 2018 ACT scores|
|**sat_participation_pct_change** | _float_ | 2017 and 2018 SAT Data | The percent change between 2017 and 2018 SAT participation|
|**act_participation_pct_change** | _float_ | 2017 and 2018 ACT Data | The percent change between 2017 and 2018 ACT participation|

### Repository Structure.
**Folders**
- Data : Data files created and needed for project.
- Images : Image files that either have been produced by the project for presentation or other images added to presentation.

**Notebooks**
- Data Analysis notebook : Adding data, cleaning data, and performing feature engineering
- EDA and Visualizations notebook : Performing exploratory data analysis, creating visualizations, and drawing conclusions.

**Other Files**
- Presentation.pdf : Presentation for Non-Technical Audience
- `simple_functions.py` : Python file that houses simple functions for various purposes used in notebooks
