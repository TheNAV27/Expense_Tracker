import pandas as pd

#df = pd.DataFrame({'Calculus':["Failed"],'Object-Oriented Programming':["Passed"]},index=['test1','test2'])
#sr = pd.Series([1,2,3,4,5],index=["one","two","three","four","five"],name='Numbers')
#ucl_matches = pd.read_csv("/Users/nav27/Personal_Projects/Expense_Tracker/Pandas practice/champions_league_matches.csv")
#print(ucl_matches.head())

animals = pd.DataFrame({'Amount': [12, 20,44,67], 
                        'Needed': [22, 19,87,55],
                        'Sold':[12,143,None,73],
                        'Remaining':[4,55,77,56]}, 
                        index=['Dogs','Cats','Cows','Chicken']
                        )
animals_indexed = animals.set_index("Amount")
check_animals = animals.Amount == 12
check_animals_loc = animals.loc[(animals.Needed >50) & (animals.Sold < 77)]
check_animals_isin = animals.loc[animals.Needed.isin([87])]
check_null = animals.loc[animals.Sold.isnull()]
check_not_null = animals.loc[animals.Sold.notnull()]
assigned_value = animals['Amount'] = 13
animals_amount = animals['Amount']
animals_iterable_assigned = animals['Needed'] = range(len(animals),0,-1)

print(animals)









