# Analyzing Data with Pandas and Visualizing Results with Matplotlib

## Objective

The goal of this assignment was to:

- Load and analyze a dataset using the `pandas` library in Python.
- Perform basic exploratory data analysis (EDA) using statistical functions.
- Visualize the data using both `matplotlib` and `seaborn`.
- Draw meaningful insights from the dataset.

## Dataset Used

I used the **Iris dataset**, which is a well-known dataset often used for classification tasks. It contains measurements for three species of Iris flowers: *setosa*, *versicolor*, and *virginica*.

## Task Breakdown

### 1. Load and Explore the Dataset

- I loaded the dataset using the `load_iris()` function from `sklearn.datasets`.
- I converted it into a pandas DataFrame for easier manipulation.
- I displayed the first few rows using `.head()` and used `.info()` and `.isnull()` to inspect the structure and check for missing values.
- There were no missing values, but I included code to handle them if necessary.

### 2. Basic Data Analysis

- I used `.describe()` to compute summary statistics like mean, median, and standard deviation for the numerical columns.
- I grouped the data by the `species` column to compute the average of various features per species.
- From the grouped data, I identified patterns such as:
  - *Iris virginica* having the longest petals on average.
  - Clear differences in measurements across species which support their separability.

### 3. Data Visualization

I created four types of visualizations to interpret and present the data visually:

1. **Line Chart**  
   - Showed trends in sepal and petal length using the index as a pseudo-time axis.
2. **Bar Chart**  
   - Compared the average petal length across the three species.
3. **Histogram**  
   - Displayed the distribution of sepal width to understand its spread.
4. **Scatter Plot**  
   - Illustrated the relationship between sepal length and petal length, colored by species.

**NB:** *To view each plot, you have to close each individual generated window to view the data from a different plotted perspective*

#### Plot Customization:

- I customized the plots using the `matplotlib` library to add titles, axis labels, and legends.
- I used `seaborn` for additional plotting styles, which made the charts more visually appealing and easier to interpret.

## Observations and Insights

- *Iris virginica* consistently showed the highest values for petal measurements.
- The histogram of sepal width showed a roughly normal distribution.
- The scatter plot clearly showed clustering by species, highlighting potential for effective classification using these features.

## How to Run

To run the analysis:

1. Make sure you have Python installed (3.7+ recommended).
2. Install the required libraries if you haven’t already:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```
3. Run the provided `.ipynb` file using Jupyter Notebook or execute the `.py` file from your terminal:
   ```bash
   python main.py
   ```

---

**Author:** Morgan  
**Course:** Data Analysis with Python  
**Date:** May 2025
