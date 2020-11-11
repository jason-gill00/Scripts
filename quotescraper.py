import requests
import bs4
#SCRAPE: http://quotes.toscrape.com/page/1/


def quotescrape():

    page = True
    counter = 8
    while(page == True):
        link = "http://quotes.toscrape.com/page/{}/"
        link_page = link.format(counter)
        counter = counter + 1
        res = requests.get(link_page)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        page_check = soup.findAll("div", {"class": "col-md-8"})
        page_valid = page_check[1].text.strip()[0:15]
        if page_valid == 'No quotes found':
            print("NO MORE QUOTES")
            print("___________________________________________________")
            page = False
            break
        # if len(page_check) != 0:
        #     print("YOU HAVE REACHED END OF WEBPAGE")
        #     print("____________________________________________")
        #     page = False
        #     break

        quotes = soup.findAll("div", {"class":"quote"})
        authors = set()
        author_quotes = []

        for quote in quotes:
            author_tag = quote.findAll("small", {"class":"author"})
            author = author_tag[0].text
            authors.add(author)
            text_quote_tag = quote.findAll("span", {"class": "text"})
            print(len(text_quote_tag))
            quote_text = text_quote_tag[0].text
            author_quotes.append(quote_text)
            # if counter == 9:
            #     print(quote_text)


        for author in authors:
            print(author)
        # for author_quote in author_quotes:
        #     text_file = open("quotes.txt", "a")
        #     text_file.write(author_quote + "\n")
        #     print(author_quote)
        # text_file.close()









if __name__ == '__main__':
    quotescrape()
