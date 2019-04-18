# import libraries
import urllib.request as urllib2
import re
from bs4 import BeautifulSoup
import os


class Search:

    def __init__(self, search_terms, url_lang, location):
        # inintialize variables here
        self.search_terms = search_terms
        self.url_lang = url_lang
        self.location = location

    # set up search loop iterating +30 every time to match syntax in url. Starting at 1470, no reason to start before
    def searchloop(self):
        i = 30
        # open file
        review_file = open("review_file.txt", "w")
        while i < 1600:
            print("loop" + str(i))
            quote_page = "https://www.tripadvisor." + self.url_lang + "/Hotels-" + self.location + "-oa" + str(i) + ".html"
            # increment search url
            i += 30
            # query the website and return the html to the variable ‘page’
            page = urllib2.urlopen(quote_page)
            # parse the html using beautiful soup and store in variable `soup`
            soup = BeautifulSoup(page, 'html.parser')

            # find ratings on search page under 2.5 stars
            rating_table = ['30', '25', '20', '15', '10']
            x = 0
            while x < 5:

                list1 = soup.find_all("a", class_="ui_bubble_rating bubble_" + rating_table[x])
                x += 1
                # print(list1)

                # save links to reviews of matching hotels on page
                listLink = []
                for a in list1:
                        listLink.append(a['href'])

                # iterate thru list of links, getting reviews
                for String in listLink:
                        rev_link = "https://www.tripadvisor." + self.url_lang + String
                        # print(rev_link)
                        # parse page
                        rev_page = urllib2.urlopen(rev_link)
                        rev_soup = BeautifulSoup(rev_page, 'html.parser')
                        reviews = rev_soup.find_all('div', {'class': 'entry'})
                        print(reviews)
                        if reviews:
                                parsed_review = reviews[0].get_text()
                                print(parsed_review)
                                for search in self.search_terms:
                                    if search in parsed_review:
                                        review_file.write(rev_link + "s\n")
                                        review_file.write(parsed_review+"\n")

            # review_file.close()
            # lines = []
            # with open("review_file.txt", "rt") as in_file:
            #         for line in in_file:
            #                 lines.append(line)
            #                 for String in lines:
            #                         if String.find(search_terms[0]):
            #                                 print(String)
