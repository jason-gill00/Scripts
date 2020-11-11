import requests
import bs4
#WEBSITE: http://books.toscrape.com/catalogue/page-1.html


def second_star():

    for n in range(1,51):
        link = " http://books.toscrape.com/catalogue/page-{}.html"
        page_link = link.format(n)
        res = requests.get(page_link)
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        products = soup.findAll("article", {"class": "product_pod"})

        for product in products:
            if product.p['class'][1] == 'Two':
                availability = product.findAll("p", {"class": "instock availability"})
                title = product.h3.a['title']
                if availability[0].text.strip() == 'In stock':
                    price_tag = product.findAll("p", {"class":"price_color"})
                    price = float(price_tag[0].text.strip()[2:])
                    if price < 30.00:
                        print(title + " PRICE: " + str(price))
                        note = open("BooksUnder30.txt", 'a')
                        note.write(title + " PRICE: " + str(price) + "\n")
                        note.close()




if __name__ == "__main__":
    second_star()
