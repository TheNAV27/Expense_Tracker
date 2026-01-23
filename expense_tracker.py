import pandas as pd

df = pd.read_csv("expense_data_1.csv")
#print(df.head())
data = df[["Date", "Category", "Note", "Amount", "Income/Expense"]]

def add_expense(date, category, note, amount, exp_type = "Expense"):
    global df #global variable that are accessible from anywhere in the code
    new_entry = {
        "Date" : date,
        "Category": category,
        "Note": note,
        "Amount" : amount,
        "Incomme/Expense" : exp_type
    }
    data.loc[len(df)] = new_entry

    print(f"Added: {note} - {amount} ({category})")
    
add_expense("2026-01-23 19:00","Food","McDonald's cheeseburger",10,"Expense")

#returns the last 5 rows .tail() function
def view_expenses(n=5):
    return data.tail(n)
print(view_expenses(5))

#function for summarizing expenses
def summarize_expenses(by="Category"):
    summary = data[data["Income/Expense"] == "Expense"].groupby(by)["Amount"].sum()
    return summary.sort_values(ascending=False)

print(summarize_expenses())



