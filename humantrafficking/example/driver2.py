from search import Search

search_terms = []
lang = 'en'


def getsearchterms():
     while True:
        entry = input('Enter a search term (q to quit): ')
        if entry.lower() == 'q':
            break
        search_terms.append(entry)


def getlang(lang):
    global url_lang
    if lang == 'en':
        url_lang = "com"
        return url_lang
    elif lang == 'es':
        url_lang = "es"
        return url_lang


def getlocation(location):
    countryCode = ['Dominican Republic', 'g147288', 'Puerto Rico', 'g147319']
    i = 0
    for country in countryCode:
            if location == country:
                return countryCode[i+1]
                break
            else:
                i = i+1


getsearchterms()

newSearch = Search(search_terms, getlang('en'), getlocation('Puerto Rico'))
newSearch.searchloop()
