import pandas as pd

boss = "employee_data.csv"

b = pd.read_csv(boss, encoding="utf-8")  

b[['Name','Last Name']] = b['Name'].str.split(' ',expand=True)
b.rename(columns={"Name": "First Name"})

formatted_dates = b['DOB'].dt.strftime('%m/%d/%Y')

us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 
                   'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
                   'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

b['State'] = b['State'].map(us_state_abbrev).fillna(b['State'])



# Place all of the data found into a summary DataFrame
summary_table = b.DataFrame({ "First Name", "Last Name",
                              "DOB": formatted_dates,
                              "SSN",
                              "State"})

b.to_excel("employee_data.xlsx", index=False)
