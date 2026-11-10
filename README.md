# Zomato Data Analysis Using Python

## Project Overview

This project focuses on analyzing Zomato restaurant data to explore restaurant categories, customer reviews, ratings, and geographical distribution across Bangalore.

The main objective is to perform data cleaning, exploratory data analysis, text analysis, and geographical analysis to discover meaningful patterns and generate business insights.

## Project Objectives

- Understand the structure and quality of the Zomato dataset.
- Clean and preprocess restaurant data.
- Analyze restaurant categories and ratings.
- Explore customer review patterns using text analysis.
- Identify frequently used words in customer reviews.
- Analyze the geographical distribution of North Indian restaurants across Bangalore.
- Generate meaningful business insights from the analysis.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- NLTK
- SQLite
- Geopy

## Project Workflow

### 1. Data Loading and Exploration

- Loaded restaurant data from an SQLite database.
- Explored dataset dimensions, columns, and data types.
- Identified missing values and duplicate records.
- Examined the overall structure of the dataset.

### 2. Data Cleaning and Preprocessing

- Handled missing and inconsistent values.
- Cleaned restaurant rating data.
- Converted rating values into numerical format.
- Prepared the dataset for further analysis.

### 3. Exploratory Data Analysis (EDA)

- Analyzed restaurant category distribution using percentage-based analysis.
- Explored restaurant types.
- Examined online ordering patterns against restaurant ratings.
- Explored restaurant locations and cuisine information.

### 4. Customer Review Analysis

- Processed customer reviews using NLTK.
- Tokenized review text.
- Removed stopwords and unwanted characters.
- Identified the most frequently used words.
- Explored common word combinations using bigrams and trigrams.

### 5. Geographical Analysis

- Extracted restaurant locations across Bangalore.
- Used Geopy to obtain geographical coordinates.
- Analyzed the distribution of North Indian restaurants by location.
- Created a geographical bubble scatter plot using Matplotlib.

## Visualizations

### 1. Restaurant Category Distribution (100% Percentage Chart)

This visualization represents the percentage distribution of restaurants across different categories, making it easier to compare their proportions.

![Restaurant Category Distribution](category_100_percentage.png)

### 2. Most Frequently Used Words in Customer Reviews

This visualization highlights the most frequently used words in customer reviews and helps identify common discussion topics.

![Most Frequently Used Words](visuals/top_words.png)

### 3. North Indian Restaurant Distribution Across Bangalore

This geographical bubble scatter plot represents the distribution of North Indian restaurants across different locations in Bangalore.

- **X-axis:** Longitude
- **Y-axis:** Latitude
- **Bubble size:** Number of North Indian restaurants
- Larger bubbles indicate locations with more restaurants.

![North Indian Restaurant Distribution](visuals/north_indian_restaurant_distribution.png)

## Key Business Insights

- Percentage-based category analysis helps understand the distribution of restaurants across different categories.
- Customer review analysis helps identify frequently discussed topics and common customer expressions.
- Geographical analysis highlights locations with higher concentrations of North Indian restaurants.
- Areas with a higher concentration of restaurants may experience stronger competition.
- Restaurant concentration can help identify potential business opportunities, but customer demand requires additional data for confirmation.

## Conclusion

This project demonstrates how Python can be used for data cleaning, exploratory data analysis, text analysis, and geographical analysis.

By analyzing restaurant categories, customer reviews, and geographical distribution, the project provides useful insights into restaurant patterns across Bangalore and demonstrates how data analysis can support business decision-making.

## Skills Demonstrated

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization
- Text Analysis and Natural Language Processing
- Geographical Data Analysis
- Business Insight Generation

## Repository Structure

```text
zomato-data-analysis-python/
│
├── visuals/
│   ├── category_100_percentage.png
│   ├── top_words.png
│   └── north_indian_restaurant_distribution.png
│
├── zomato_analysis.py
└── README.md
```
