# -*- coding: UTF-8 -*-
"""Employee Email Script.


This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import pandas as pd

e = "Resources/employees.csv"

# Read the modified GoodReads csv and store into Pandas DataFrame
employees = pd.read_csv(e, encoding="utf-8")

        
email = str(employees["first_name"]+"."+employees["last_name"]+"@example.com")

employees["Email"] = email



employees.to_excel("employees.xlsx", index=False)
