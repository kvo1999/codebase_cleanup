
# READ INVENTORY OF PRODUCTS

#products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
#products_df = read_csv(products_filepath)
#products = products_df.to_dict("records")

import os


from app.utils import to_usd


#def to_usd(my_price):
   # """
    #this is a docstring. it tells us what this function is about,
    #what it's respobsibilities are, 
    #what it's parameters are about, 
    #what this function will return

    #invoke like: to_usd(9.9999)
    #"""
    #return '${:,.2f}'.format(my_price)

filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")

# checks to see if a products.csv file exists. If not, it uses the default
if os.path.isfile(filepath) == True:
    print("USING CUSTOM PRODUCTS CSV FILE...")
    csv_filepath = filepath
else:
    print("USING DEFAULT PRODUCTS CSV FILE...")
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "default_products.csv")



from pandas import read_csv

#reads the csv file into products variable
products = read_csv(csv_filepath)
#pandas transforms the data into a list of dictionaries
products = products.to_dict('records')



# PRINTED INVENTORY REPORT

print("---------")
print("THERE ARE", len(products), "PRODUCTS:")
print("---------")

all_prices = []
for p in products:
    all_prices.append(float(p["price"]))
    print("..." + p["name"] + "   " + to_usd(p["price"]))

import statistics
avg_price = statistics.mean(all_prices)

print("---------")
print("AVERAGE PRICE:", to_usd(avg_price))





# EMAIL INVENTORY REPORT
