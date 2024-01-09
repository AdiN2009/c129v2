import pandas as pd


dwarf_csv = pd.read_csv('dwarf_stars.csv')

scraped_csv = pd.read_csv('scarped_data.csv')


columns_to_clean = ['Distance','Mass','Radius']
dwarf_csv[columns_to_clean] = dwarf_csv[columns_to_clean].fillna(0)
dwarf_csv.head()


column_to_multiply = 'Radius'
multiplier = 0.102763

# Check and convert the 'Mass' column in dwarf_csv
if column_to_multiply in dwarf_csv.columns:
    dwarf_csv[column_to_multiply] = pd.to_numeric(dwarf_csv[column_to_multiply], errors='coerce')
    dwarf_csv[column_to_multiply] = dwarf_csv[column_to_multiply].fillna(0)  # Replace NaN with 0
    dwarf_csv[column_to_multiply] *= multiplier
else:
    print(f"Error: Column '{column_to_multiply}' not found in dwarf_csv.")

# Check and convert the 'Mass' column in scraped_csv
if column_to_multiply in scraped_csv.columns:
    scraped_csv[column_to_multiply] = pd.to_numeric(scraped_csv[column_to_multiply], errors='coerce')
    scraped_csv[column_to_multiply] = scraped_csv[column_to_multiply].fillna(0)  # Replace NaN with 0
    scraped_csv[column_to_multiply] *= multiplier
else:
    print(f"Error: Column '{column_to_multiply}' not found in scraped_csv.")

# Display the head of dwarf_csv
dwarf_csv.head()



















column_to_multiply2 = 'Mass'
multiplier2 = 0.000954588


# Check and convert the 'Mass' column in dwarf_csv
if column_to_multiply2 in dwarf_csv.columns:
    dwarf_csv[column_to_multiply2] = pd.to_numeric(dwarf_csv[column_to_multiply2], errors='coerce')
    dwarf_csv[column_to_multiply2] = dwarf_csv[column_to_multiply2].fillna(0)  # Replace NaN with 0
    dwarf_csv[column_to_multiply2] *= multiplier2
else:
    print(f"Error: Column '{column_to_multiply2}' not found in dwarf_csv.")

# Check and convert the 'Mass' column in scraped_csv
if column_to_multiply2 in scraped_csv.columns:
    scraped_csv[column_to_multiply2] = pd.to_numeric(scraped_csv[column_to_multiply2], errors='coerce')
    scraped_csv[column_to_multiply2] = scraped_csv[column_to_multiply2].fillna(0)  # Replace NaN with 0
    scraped_csv[column_to_multiply2] *= multiplier2
else:
    print(f"Error: Column '{column_to_multiply2}' not found in scraped_csv.")

# Display the head of dwarf_csv
dwarf_csv.head()


merge_star_csv=pd.merge(dwarf_csv, scraped_csv, on = "id")
merge_star_csv.shape

merge_star_csv.to_csv('total_stars.csv')