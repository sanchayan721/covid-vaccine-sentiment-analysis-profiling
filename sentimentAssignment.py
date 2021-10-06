import csv
import nltk
from nltk import sentiment
from nltk.sentiment import SentimentIntensityAnalyzer
if not 'vader_lexicon':
    nltk.download('vader_lexicon')
from textblob_de import TextBlobDE
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from langdetect import detect


def write_to_csv(new_data, filename='data/tweet_sentiment.csv'):
    with open(filename, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(new_data)

def confirmLanguage(sentense, language):
    try:
        lang = detect(sentense)
        if language == lang:
            return True
        else:
            return False

    except:
        lang = "error"
        print("This sentence throws and error:", sentense)

def addSentiment(row):

    # Sentiment Analysis English Tweets
    if row[4] == 'en':
        analyser = SentimentIntensityAnalyzer()
        polarity = analyser.polarity_scores(row[1])

        if polarity['compound'] > 0:
            row.append(1)

        elif polarity['compound'] == 0:
            row.append(0)
        
        else:
            row.append(-1)

    # Sentiment Analysis German Tweets
    elif row[4] == 'de':
        blob = TextBlobDE(row[1])

        if blob.polarity > 0:
            row.append(1)

        elif blob.polarity == 0:
            row.append(0)
        
        else:
            row.append(-1)
    
    # Sentiment Analysis French Tweets
    elif row[4] == 'fr':
        tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        blob = tb(row[1])

        if blob.sentiment[0] > 0:
            row.append(1)

        elif blob.sentiment[0] == 0:
            row.append(0)
        
        else:
            row.append(-1)
    
    return row

def sentimentAssignment():

    language_list = ['en', 'de', 'fr']  

    with open('data/clean_tweets.csv', 'r') as file_object:
        tweet_file = csv.reader(file_object)

        for row in tweet_file:
            if row[4] in language_list and confirmLanguage(row[1], row[4]):
                new_row = addSentiment(row)
                write_to_csv(new_row)

            else:
                pass

if __name__ == '__main__':

    print("Sentimens are being assigned ...")
    sentimentAssignment()