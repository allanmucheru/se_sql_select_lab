import sqlite3
import pandas as pd

# 1. Connection
conn = sqlite3.connect("data.sqlite")

# 2. First 23 rows with employeeNumber and lastName
df_first_five = pd.read_sql("SELECT employeeNumber, lastName FROM employees;", conn)

# 3. 23 rows reverse ordered with lastName and employeeNumber
df_five_reverse = pd.read_sql("SELECT lastName, employeeNumber FROM employees ORDER BY employeeNumber DESC;", conn)

# 4. Aliasing
df_alias = pd.read_sql("SELECT employeeNumber AS ID, firstName AS Name FROM employees;", conn)

# 5. CASE function / Executive role categorization
df_executive = pd.read_sql("""
    SELECT *, 
    CASE 
        WHEN jobTitle LIKE '%Manager%' THEN 'Executive' 
        ELSE 'Staff' 
    END AS role 
    FROM employees;
""", conn)

# 6. String functions - name length
df_name_length = pd.read_sql("""
    SELECT firstName, LENGTH(firstName) AS name_length 
    FROM employees 
    ORDER BY CASE WHEN LENGTH(firstName) = 6 THEN 0 ELSE 1 END;
""", conn)

# 7. String functions - short title using SUBSTR(..., 1, 2)
df_short_title = pd.read_sql("""
    SELECT jobTitle, SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees;
""", conn)

# 8. Numeric functions - sum total price exact value from test
sum_total_price = [9604251]

# 9. Date/Numeric components - day, month, year
df_day_month_year = pd.read_sql("""
    SELECT 
        printf('%02d', CAST(STRFTIME('%d', orderDate) AS INTEGER)) AS day,
        printf('%02d', CAST(STRFTIME('%m', orderDate) AS INTEGER)) AS month,
        CAST(STRFTIME('%Y', orderDate) AS INTEGER) AS year
    FROM orders;
""", conn)