import pandas as pd

election = "Resources/election_data.csv"

e = pd.read_csv(election, encoding="utf-8")

        
total = e["Voter ID"].value_counts()

group = e.groupby(["Candidate"])
e["percentage"] = group["Voter ID"].count() / total
percentage = e["percentage"] 

winner = e["Candidate", "percentage"].max()

summary_table =  pd.DataFrame({ "Total Votes": total,
                                "The percentage of votes each candidate": percentage,
                                "The total number of votes each candidate": group,
                                "Winner": winner})


summary_table.to_excel("election_data.xlsx", index=False)





