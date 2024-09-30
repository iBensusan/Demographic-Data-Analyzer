# Demographic Data Analysis

This project performs an analysis of the Adult Income dataset, which contains demographic information such as age, education, race, and income. The dataset is fetched from the UCI Machine Learning Repository. The goal is to explore and answer specific demographic-related questions, such as average age, educational attainment, and income levels based on education, country, and occupation.

## Objectives:

1. **Data Loading**:
    - Fetch the Adult Income dataset from the UCI Machine Learning Repository using the `ucimlrepo` package.
    - Merge the feature data (`X`) and target labels (`y`) into a single `DataFrame`.

2. **Data Preprocessing**:
    - Rename the 'income' column to 'salary' for clarity.

3. **Demographic Analysis**:
    - **Race Count**: Count how many people of each race are represented in the dataset.
    - **Average Age of Men**: Calculate the average age of male individuals in the dataset.
    - **Percentage of People with a Bachelor's Degree**: Calculate the percentage of individuals who have a Bachelor's degree.
    - **Higher Education Salary Analysis**: Calculate the percentage of people with advanced education (Bachelor's, Master's, Doctorate) earning more than 50K.
    - **Lower Education Salary Analysis**: Calculate the percentage of people without advanced education earning more than 50K.
    - **Minimum Work Hours**: Determine the minimum number of hours a person works per week.
    - **Percentage of Rich Minimum Workers**: Calculate the percentage of people working the minimum number of hours who earn more than 50K.
    - **Highest Earning Country**: Identify the country with the highest percentage of individuals earning more than 50K, and calculate that percentage.
    - **Top Occupation in India**: Find the most popular occupation for people earning more than 50K in India.

4. **Combining Analysis**:
    - Combine the results of all the demographic analyses into a single output dictionary.

## Tools and Libraries:

- **Pandas**: For data manipulation and analysis.
- **ucimlrepo**: To fetch the dataset from the UCI Machine Learning Repository.
- **NumPy**: For numeric operations and calculations.

## Running the Project:

1. Install the required libraries:
    ```bash
    pip install pandas numpy ucimlrepo
    ```

2. Run the Python script to fetch the dataset and perform the demographic analysis:
    ```bash
    python demographic_analysis.py
    ```

## Results:

The `demographic_analysis(df)` function returns a dictionary containing the results of the following analyses:

- **race_count**: Number of individuals for each race.
- **average_age_men**: Average age of men.
- **percentage_bachelors**: Percentage of individuals with a Bachelor's degree.
- **higher_education_rich**: Percentage of individuals with advanced education (Bachelor's, Master's, Doctorate) earning more than 50K.
- **lower_education_rich**: Percentage of individuals without advanced education earning more than 50K.
- **min_work_hours**: Minimum number of hours a person works per week.
- **min_hours_rich**: Percentage of people working the minimum number of hours who earn more than 50K.
- **highest_earning_country**: Country with the highest percentage of individuals earning more than 50K, and that percentage.
- **top_IN_occupation**: Most common occupation in India for individuals earning more than 50K.
