## Goal
The goal of this project is to collect tweets written in English, German
and French from Twitter and applying some of the ETL techniques to clean the text and analyse the sentiment of those tweets,
then by using some of the other techniques learnt from previous courses
in my master's curriculum to find out the distributions of sentiments
for different vaccines and also to find out any co-relation between
different types of twitter users namely "verified" ones who are usually
celebrates and well known people in their respective communities and
non-verified ones, the general public. Other important goals of this
project includes to find out heat-maps of vaccine hesitancy and vaccine
decisiveness around the globe and if possible to find out which are the
most popular vaccines in the different parts of the world.

## Entry point
Please start from "Vaccine_Sentiment_Analysis_Report.pdf" file.

### Important Notes

Collecting the tweets using takes about 5-6 hours as twitter has an hourly limit. The cleaning part takes about 1 minute but the sentiment assignment part will take about 25-30 minutes.

I am sharing the links of all those data files uploaded in my One Drive folder from where it can be downloaded in order for you to save a lot of time. After downloading place the missing files in the "submission/data" folder. The total size of all of the data files is about 80 MB.

OneDrive Link:
<https://1drv.ms/u/s!ApUwC0uDWXPNg55uPMnMaBUEnQ46Ew?e=5jzHOL>

When the getTweets.py module is executed, it will ask for an encryption key, which will allow you to use my Tweeter API access keys to collect tweets. If you are authorized, you can use my tweeter tokens using the key. Otherwise, please collect a Tweeter developer account and use your own keys.
Else, one is welcomed to download the data from my OneDrive and use it. 
