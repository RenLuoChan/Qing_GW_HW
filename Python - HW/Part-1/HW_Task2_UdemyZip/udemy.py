import pandas as pd

web = "web_starter.csv"

# Read the modified GoodReads csv and store into Pandas DataFrame
web_s = pd.read_csv(web, encoding="utf-8", header=None)
web_s.columns = ["id","title","url","isPaid","price","numSubscribers",
                  "numReviews","numPublishedLectures","instructionalLevel",
                  "contentInfo","publishedTime"]
web_s.head()
        
total = web_s["numSubscribers"].sum()
total

percentage_sub = web_s["numSubscribers"]/total
web_s["percentage_sub"] = percentage_sub

web_s.head()

#web_s.astype({'contentInfo': 'int32'}).dtypes
web_s.to_numeric("contentInfo", errors='coerce')

web_s.to_excel("output/web_starter.xlsx", index=False)