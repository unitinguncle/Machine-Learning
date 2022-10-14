"""Problem 02
You're given a file named insurance.csv that contains the information of some people, including age, sex, bmi, children, smoker, region, and charges. The first several rows in the csv file are as follow: ...

age	sex	bmi	children	smoker	region	charges
19	female	27.9	0	yes	southwest	16884.924
50	male	33.7	3	yes	northwest	53744.354
21	female	24.6	1	no	southwest	36245.912
30	male	17.3	5	no	northeast	12343.978
...

However, the data in this file is noisy, with some data missing and some rows duplicated. You task is to write the function rate(filepath, num_of_children) to implement the following steps:

use the given filepath to read the data from the csv file.
drop the rows with NaN.
drop the duplicated rows, except for the LAST occurrence.
select the rows with non-smokers whose children smaller than or equal to the given argument max_children.
for every row selected from (4), calculate the charge-age rate (charge-age rate = charges / age)
for every row selected from (4), calculate the charge-bmi rate (charge-bmi rate = charges / bmi)
add two columns named CHARGE_AGE and CHARGE_BMI to the dataframe selected from (4).
return the dataframe get from (7), but only with these columns age, sex, region, CHARGE_AGE and CHARGE_BMI.
function: rate(filepath, max_children) """

import pandas as pd

def rate(file_path: str, max_children: int) -> pd.DataFrame:
    # Write Code Here
    df = pd.read_csv(file_path)

    df = df.dropna()
    df = df.drop_duplicates(keep = 'last')

    non_smoker = df['smoker'] != 'yes'
    child = df['children'] <= max_children
    df = df[non_smoker & child]

    charge_age = df['charges']/df['age']
    charge_bmi = df['charges']/df['bmi']

    df['CHARGE_AGE'] = charge_age
    df['CHARGE_BMI'] = charge_bmi

    return df[['age','sex','region','CHARGE_AGE','CHARGE_BMI']]

rate('/content/insurance - insurance.csv', 5)
