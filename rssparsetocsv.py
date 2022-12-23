import feedparser
import pandas as pd
from tqdm import tqdm
import warnings #get rid of annoying pandas depreciating function warnings (ik its bad)
warnings.simplefilter(action='ignore',category=FutureWarning)
from datetime import datetime
import os

#put desired RSS links into list of strings
sites = ['https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml','http://www.axios.com/feeds/feed.rss',
         'https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best']

#RSS parsing function
def parse(data, limit):
    #lists for titles & links -> DataFrame -> .csv
    titleout = []
    linkout = []
    
    feed = feedparser.parse(data)

    #parsing article titles & links
    for entry in feed["entries"]:
            title = entry.get("title")
            link = entry.get("link")
            if title:
                if link:
                    titleout.append(title)
                    linkout.append(link)
                else:
                    titleout.append(title)
            if limit and len(titleout) == limit:
                break
    news = {'Title':titleout,'Link':linkout}
    df = pd.DataFrame.from_dict(news, orient='index')
    df = df.transpose()
    return df

#enter the number of articles you want
nArticles = int(input('Enter number of articles per site: '))
#making DataFrame
totalnews = pd.DataFrame(columns=['Title','Link'])

#parsing through each site and adding to DataFrame
for site in tqdm(sites):
    newsdf = parse(site,nArticles)
    totalnews = totalnews.append(newsdf)

#exporting to .csv
os.chdir('') #put ur directory in the quotes
filename = datetime.now().strftime('news_%H%M_%m%d%Y.csv')
totalnews.to_csv(filename)
