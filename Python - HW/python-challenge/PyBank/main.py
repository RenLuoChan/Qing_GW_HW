import pandas as pd

bank = "Resources/budget_data.csv"

b = pd.read_csv(bank, encoding="utf-8")

        
totalmonth = b["Date"].value_counts()

b["Profit/Losses"] = b["Profit/Losses"].map("${:.2f}".format)
total = b["Profit/Losses"].sum()
average = b["Profit/Losses"].mean()


sort = b.sort_values("Date")
b[['Date','allele']] = b['Date'].str.split('-',expand=True)
gp = b.groupby('Date')


increase = b["Date", "Profit/Losses"].max()
decrease = b["Date", "Profit/Losses"].min()


# Place all of the data found into a summary DataFrame
summary_table = pd.DataFrame({"Total month": totalmonth,
                              "Total": total,
                              "Average  Change": average,
                              "Greatest Increase in Profits": increase,
                              "Greatest Decrease in Profits": decrease})

xdf = summary_table.transpose()
xdf

xdf.to_excel("budget_data.xlsx", index=False)


