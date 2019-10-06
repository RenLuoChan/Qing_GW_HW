import pandas as pd
# Initial variable to track shopping status
shopping = 'y'

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

pie_purchases = [0 for p in pie_list]

pie_dict = {"Pie": pie_list, "Purchases": pie_purchases}

pie_df = pd.DataFrame(pie_dict)

print("Welcome to the House of Pies! Here are our pies:\n")

for index, row in pie_df.iterrows():
    print(f"({index + 1}) {row['Pie']}")
          
while shopping == "y":

    pie_choice = input("Which would you like? ")

    # Get index of the pie from the selected number
    choice_index = int(pie_choice) - 1
          
    # Find the record to increment
    pie_df.loc[choice_index, "Purchases"] += 1 
          
    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_df.loc[choice_index, "Pie"] + " right out for you.")
          
    # Provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

print("You purchased\n")

pie_df = pie_df.set_index("Pie")

pie_df

pie_df.reset_index()