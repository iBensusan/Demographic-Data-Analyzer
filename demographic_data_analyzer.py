from ucimlrepo import fetch_ucirepo 
import pandas as pd
  
# fetch dataset 
adult = fetch_ucirepo(id=2) 
  
# data 
X = adult.data.features 
y = adult.data.targets 
  
# metadata 
#print(adult.metadata) 

# variable information 
#print(adult.variables) 

# Merging into dataframe
df = pd.concat([X, y], axis=1)

df.rename(columns={'income': 'salary'}, inplace=True)

# How many people of each race are represented in this dataset?
def race_count(df):
    return df['race'].value_counts()

# What is the average age of men?
def average_age_men(df):
    return df[df['sex'] == 'Male']['age'].mean().round(1)

# What is the percentage of people who have a Bachelor's degree?
def percentage_bachelors(df):
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    return round((bachelors_count / len(df) * 100), 1)

# What percentage of people with advanced education make more than 50K?
def higher_education_rich(df):
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    rich_people = higher_education[higher_education['salary'] == '>50K']
    return round((len(rich_people) / len(higher_education) * 100), 1)

# What percentage of people without advanced education make more than 50K?
def lower_education_rich(df):
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    rich_people = lower_education[lower_education['salary'] == '>50K']
    return round((len(rich_people) / len(lower_education) * 100),1)

# What is the minimum number of hours a person works per week?
def min_work_hours(df):
    return df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
def min_hours_rich(df):
    min_hours = df['hours-per-week'].min()
    rich_min_workers = df[(df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')]
    return round((len(rich_min_workers) / len(df[df['hours-per-week'] == min_hours]) * 100),1)

# What country has the highest percentage of people that earn >50K and what is that percentage?
def highest_earning_country(df):
    country_stats = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    return country_stats.idxmax(), (country_stats.max() * 100).round(1)

# Identify the most popular occupation for those who earn >50K in India.
def top_IN_occupation(df):
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    return india_rich['occupation'].value_counts().idxmax()

# Combining all the analyses
def demographic_analysis(df):
    return {
        'race_count': race_count(df),
        'average_age_men': average_age_men(df),
        'percentage_bachelors': percentage_bachelors(df),
        'higher_education_rich': higher_education_rich(df),
        'lower_education_rich': lower_education_rich(df),
        'min_work_hours': min_work_hours(df),
        'min_hours_rich': min_hours_rich(df),
        'highest_earning_country': highest_earning_country(df),
        'top_IN_occupation': top_IN_occupation(df)
    }

# Calling demographic_analysis(df) get all values
results = demographic_analysis(df)
print(results)


