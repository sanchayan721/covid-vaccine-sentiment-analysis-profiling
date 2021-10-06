import csv, re
from os import name
import json
import subprocess
import sys




try:
    from geotext import GeoText

except ModuleNotFoundError:
    print("Warning: geotext module not found!")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'geotext'])
    from geotext import GeoText


country_dict = dict()
with open('data/countries.json', 'r', encoding='utf-8') as json_file:
        country_dict = json.load(json_file)
        country_list = list(country_dict.values())



def write_to_csv(new_data, filename='data/clean_tweets.csv'):
    with open(filename, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(new_data)



def fixCountry(mispell):

    misspell_cap = " ".join([x[0].upper() + x[1:] for x in mispell.split()])

    places = GeoText(misspell_cap)
    abbvs = list()
    if not places.cities and not places.countries:
        return ''
    
    else:
        for abbv in places.country_mentions.keys():
            abbvs.append(abbv)

        return country_dict[abbvs[0]]




def clean_with_regex(sentence):
    
    def deEmojify(text):

        text = str(text).replace(','," ")
        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                    "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'',text)

    def remove_url(txt):
        return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

    def remove_number(txt):
        return re.sub(r'[0-9]+', '', txt)
    
    def remove_email(text):
        return re.sub('\S*@\S*\s?','',text)
        
    def remove_username(text):
        return re.sub('@[^\s]+','',text)    

    clean_sentence = deEmojify(sentence)
    clean_sentence = remove_url(clean_sentence)
    clean_sentence = remove_email(clean_sentence)
    clean_sentence = remove_username(clean_sentence)
    clean_sentence = remove_number(clean_sentence)

    return clean_sentence



def merge_vaccine_names(vaccine_name):
    
    if vaccine_name in ['Pfizer Vaccine', 'BioNTech', 'Comirnaty Vaccine']:
        return 'Pfizer BioNTech'
        
    elif vaccine_name in ['AstraZeneca','Covishield']:
        return 'AstraZeneca'
        
    elif vaccine_name in ['Johnson & Johnson vaccine', 'Vaccine Janssen']:
        return 'Johnson & Johnson'
        
    elif vaccine_name in ['Sinovac vaccine', 'CoronaVac']:
        return 'CoronaVac'
        
    elif vaccine_name in ['BBIBP-CorV', 'Sinopharm vaccine']:
        return 'BBIBP-CorV'

    elif vaccine_name in ['PakVac', 'Ad5-nCoV', 'Convidicea']:
        return 'Convidicea'
        
    elif vaccine_name in ['Covaxin Vaccine', 'Bharat Biotech Vaccine']:
        return 'Covaxin'

    else:
        return vaccine_name


def cleanAndSort(filtr):

    with open('data/raw_tweets.csv', 'r', encoding='utf-8') as file_object:
        tweet_file = csv.reader(file_object)

        for row in tweet_file:
            if len(row[1]) > filtr:
                new_row = row[:]
                new_row[0] = merge_vaccine_names(row[0])
                new_row[1] = clean_with_regex(row[1])
                new_row[2] = fixCountry(row[2])
                write_to_csv(new_row)



if __name__ == '__main__':
    filtr = int(input("Input minimum length filter: \t"))
    
    try:
        val = int(filtr)
    
    except:
        filtr = 25
        print('using default minimum length: {}'.format(filtr))
    
    cleanAndSort(filtr)