# Precog Assignment 
### By Anmol Kumar (2018382)

## Task 1 - Report of Paper

I have selected [Signals Matter: Understanding Popularity and Impact of Users
on Stack Overflow](http://precog.iiitd.edu.in/pubs/SignalsMatter-TheWebConf19.pdf) as the paper to summarise. The file name is  Task 1-Report.pdf

## Task 2 - Twitter Scrapping

The implementation is  based on Twitter API v2.0 which extracts recent trending tweets in the city of Delhi and Hyderabad, India. For this purpose, python module tweepy as been used. This task is implemented in two ways:

- twitter-scrapper.ipynb : Jupyter Notebook
- [https://usetwitterscrapper.herokuapp.com](https://usetwitterscrapper.herokuapp.com/) : A flask web app with extracted data and plots. The app can be run locally as well. Just clone the reposity, browse to **Twitter-Scrapper-Flask** directory and run the following command:

    ```python
    python3 app.py
    ```

    The Flask app will then run locally on local server [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

To start with using this application, you need to follow these 3 steps: 

1. You must have a Twitter ID. Login to [https://developer.twitter.com](https://developer.twitter.com/) and create API Project to generate the API key and Secret.
2. Enter the API key and Secret in the two fields given below
3. Authorize the key and then enter the number of tweets to be extracted. Entering a large number might result in delays due to API restrictions on rate limit.

### Analysis about the users

- Number of verified profiles
- Linguistic Analysis through graphs.
- *Relation with other hashtags (not explored because of time limitations)*
- A Custom **Reach Score** has been defined for each user based on the following formula:

```python
Reach Score = ln(followers * friends)
```

### Limitations of the script

1. An API key must be generated for the program to run which is to be entered in the scripy before running it.
2. The user must be logged into the twitter account before hand because the Tweepy API needs to authenticate using a link from which a PIN is extracted. The PIN is also entered as an input in the script. 
3. The API has rate limits so that the twitter servers are not overburdened, hence data can take some time update.
4. We are only able to extract twitter data of the last 7 days

### Why not Selenium/Scrapy/BeautifulSoup ?

It is very easy to implement a web crawler with these python framworks, but the main challenge is that twitter is able to detect these crawlers. The following ways were tried with Selenium twitter couldn't detect them: 

1. Scraping using such automation for such a large amount of data could generate a lot of traffic which could overburden the Twitter server. The website has put various measures to avoid that. 
2. Since I was at the risk of getting my IP blocked for scraping large amounts of data, I needed a way to avoid this. One way of doing this was by using multiple proxies and run the bot parallelly using tools like [proxyscrape.com](http://proxyscrape.com) and [scraperapi.com](http://scraperapi.com). But these tools are mostly paid so I didn't try them any further.
