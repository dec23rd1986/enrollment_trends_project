USE texas_enrollment_db;

# drop table if it already exists
DROP TABLE IF EXISTS fall_enrollment_ethnicity;

# Creating table in database that corresponds to CSV file import
CREATE TABLE fall_enrollment_ethnicity (
    institution_id INT,
    institution_name VARCHAR(255),
    academic_year VARCHAR(10),
    white INT,
    african_american INT,
    hispanic INT,
    asian INT,
    international INT,
    other INT,
    total INT
);

SELECT institution_id, institution_name, academic_year, total 
FROM fall_enrollment_ethnicity
WHERE institution_name IS NULL OR institution_name = '';


# Loading CSV file (replacing any cells with NA > NULL)
LOAD DATA LOCAL INFILE '/Users/andreasanchez/Downloads/Enroll_by_Eth1.csv'
INTO TABLE fall_enrollment_ethnicity
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(institution_id, institution_name, academic_year, white, african_american, hispanic, asian, @international, other, total)
SET international = NULLIF(@international, 'NA');

# Confirm data loaded correctly with first 10 rows
SELECT * FROM fall_enrollment_ethnicity LIMIT 10;

# Query 1: Enrollment growth or decline by institution (2021–2023)
SELECT institution_name, academic_year, total
FROM fall_enrollment_ethnicity
WHERE academic_year IN ('fall_2021', 'fall_2022', 'fall_2023')
ORDER BY institution_name, academic_year;

# Query 2: Identify institutions with significant growth or decline
SELECT institution_name, 
       MAX(total) AS max_enrollment, 
       MIN(total) AS min_enrollment, 
       (MAX(total) - MIN(total)) AS enrollment_change
FROM fall_enrollment_ethnicity
WHERE academic_year IN ('fall_2021', 'fall_2022', 'fall_2023')
GROUP BY institution_name
ORDER BY enrollment_change DESC;

# Query 3: Calculate the percentage change in enrollment for each university from 2021 to 2023

SELECT institution_name,
    academic_year,
    (total - LAG(total, 1) OVER (PARTITION BY institution_name ORDER BY academic_year)) / LAG(total, 1) OVER (PARTITION BY institution_name ORDER BY academic_year) * 100 AS enrollment_percentage_change
FROM fall_enrollment_ethnicity
WHERE academic_year IN ('fall_2021', 'fall_2023')
ORDER BY institution_name, academic_year;

# Query 4: Correlation between enrollment and ethnicity over time
SELECT academic_year, 
       SUM(white) AS total_white, 
       SUM(african_american) AS total_african_american, 
       SUM(hispanic) AS total_hispanic, 
       SUM(asian) AS total_asian, 
       SUM(international) AS total_international, 
       SUM(other) AS total_other
FROM fall_enrollment_ethnicity
GROUP BY academic_year
ORDER BY academic_year;


