import pandas as pd
import matplotlib.pyplot as plt


# Query 1: Enrollment growth or decline by institution (2021–2023)
# ---------------------------------------------------------
# Load CSV for Query 1
data_query_1 = pd.read_csv('/Users/andreasanchez/Desktop/sql_project/query_1_enrollment_growth.csv')

# Create a bar chart for an institution (e.g., UT San Antonio)
utsa_data = data_query_1[data_query_1['institution_name'] == 'The University of Texas at San Antonio']
plt.figure(figsize=(8, 6))
plt.plot(utsa_data['academic_year'], utsa_data['total'], marker='o')
plt.title('Enrollment Trends for UT San Antonio (2021-2023)')
plt.xlabel('Academic Year')
plt.ylabel('Total Enrollment')

# Save the plot as an image
plt.savefig('/Users/andreasanchez/Desktop/sql_project/query1.png')
plt.show(block=False)  # Non-blocking plot
plt.close()

# Query 2: Enrollment Growth or Decline by Institution
# ---------------------------------------------------------
# Load CSV for Query 2
data_query_2 = pd.read_csv('/Users/andreasanchez/Desktop/sql_project/query_2_significant_growth_decline.csv')

# Bar chart for enrollment growth or decline
plt.figure(figsize=(12, 8))  # Increase the figure size for better visibility
plt.bar(data_query_2['institution_name'], data_query_2['enrollment_change'], color='lightgreen')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=90, ha='right')  # Rotate labels and align them to the right

# Add labels and title
plt.title('Enrollment Growth or Decline by Institution (2021–2023)')
plt.xlabel('Institution Name')
plt.ylabel('Enrollment Change')

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# Save the plot as an image
plt.savefig('/Users/andreasanchez/Desktop/sql_project/query_2_enrollment_growth.png')
plt.show(block=False)  # Non-blocking plot
plt.close()

# Query 3: Percentage Change in Enrollment
# ---------------------------------------------------------
# Load CSV for Query 3
data_query_3 = pd.read_csv('/Users/andreasanchez/Desktop/sql_project/query_3_percentage_change.csv')

# Bar chart for percentage change
plt.figure(figsize=(12, 8))  # Increase the figure size for better visibility
plt.bar(data_query_3['institution_name'], data_query_3['enrollment_percentage_change'], color='skyblue')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=90, ha='right')  # Rotate labels and align them to the right

# Add labels and title
plt.title('Percentage Change in Enrollment from 2021 to 2023')
plt.xlabel('Institution Name')
plt.ylabel('Percentage Change')

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# Save the plot as an image
plt.savefig('/Users/andreasanchez/Desktop/sql_project/query_3_percentage_change.png')
plt.show(block=False)  # Non-blocking plot
plt.close()

# Query 4: Correlation between enrollment and ethnicity
# ---------------------------------------------------------
# Load CSV for Query 4
data_query_4 = pd.read_csv('/Users/andreasanchez/Desktop/sql_project/query_4_ethnicity_correlation.csv')

# Ethnic groups to plot
ethnic_groups = ['total_white', 'total_african_american', 'total_hispanic', 'total_asian', 'total_international', 'total_other']

# Create a pie chart for each year

for year in ['fall_2021', 'fall_2022', 'fall_2023']:
    # Filter data for the current year
    year_data = data_query_4[data_query_4['academic_year'] == year]
    
    # Sum totals for each ethnicity
    totals = year_data[ethnic_groups].sum()

    # Create the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(totals, labels=ethnic_groups, autopct='%1.1f%%', startangle=140)
    plt.title(f'Ethnicity Distribution in {year}')

    # Save the plot as an image
    plt.savefig(f'/Users/andreasanchez/Desktop/sql_project/query_4_{year}.png')
    
    # Show and close the plot
    plt.show()
    plt.close()
