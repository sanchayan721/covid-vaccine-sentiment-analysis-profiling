import subprocess
import sys
try:
    import nltk
    
except ModuleNotFoundError:
    print("Warning: nltk module not found!")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nltk'])
    import nltk

if not 'averaged_perceptron_tagger':
    nltk.download('averaged_perceptron_tagger')

sentense = "i told Sanchayan what is my name"


class Subject:

    def __init__(self):
        pass
    
    sentiment = 0

    def changeSentiment(self, new_sentiment):
        self.sentiment = new_sentiment


def classifier(sentense, point_of_view):

    tokenized_sentense = nltk.word_tokenize(sentense)
    pos_tags = nltk.pos_tag(tokenized_sentense)
    dict_of_subjects = dict()

    for word_tags in pos_tags:
        if word_tags[1] in ("NN","NNS", "NNP", "NNPS"):
            dict_of_subjects[word_tags[0]] = Subject()    


    return(dict_of_subjects[point_of_view].sentiment)

print(classifier(sentense,'Sanchayan'))