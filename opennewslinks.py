import webbrowser

#input sites that you want opened
sites = ['https://en.wikipedia.org/wiki/Portal:Current_events','https://apnews.com','https://www.reuters.com','https://www.nytimes.com',
         'https://www.politico.com','https://www.fivethirtyeight.com',
         'https://news.ycombinator.com']

for site in sites:
    webbrowser.open(site,new=0)

