import requests
import bs4
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine


# mydb = mysql.connector.connect(host='localhost',user='root',passwd='sherrygill123',database='books')
# my_cursor = mydb.cursor()
# my_cursor.execute("")

df = pd.DataFrame(columns=['Name', 'UPC', 'Product Type', 'Price(exc.tax)', 'Price(incl.tax)', 'Tax', 'Availability', 'Number of Reviews' ])


df_count = 0

for x in range(1,51):
    link = "http://books.toscrape.com/catalogue/page-{}.html"
    l = link.format(x)
    res = requests.get(l)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    products = soup.findAll('article', {"class":'product_pod'})


    for product in products:
        df.loc[df_count] = 'x','x','x','x','x','x','x','x'
        product_link = product.h3.a['href']
        book_link = "http://books.toscrape.com/catalogue/" + product_link
        res = requests.get(book_link)
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        title_tag = soup.findAll('div', {'class':'col-sm-6 product_main'})
        title = title_tag[0].h1.text
        df.iloc[df_count, 0] = title

        table = soup.findAll('table', {'class':'table table-striped'})
        rows = table[0].findAll('tr')


        count = 0
        for row in rows:
            df.iloc[df_count, count+1] = row.td.text
            count += 1

        df_count += 1

        #print(df)

        print(f"You are on page {x}")


mydb = create_engine('mysql+mysqlconnector://root:sherrygill123@localhost:3306/books', echo=False)

df.to_sql(name='books_record', con=mydb, index=False, if_exists='replace')
