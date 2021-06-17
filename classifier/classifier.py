sentense = "I am a man who not is good in coding"

class Subject:
    def __init__(self):
        pass
    
    sentiment = 0

    def changeSentiment(self, new_sentiment):
        self.sentiment = new_sentiment

def classifier(sentense, point_of_view):
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

    tokenized_sentense = nltk.word_tokenize(sentense)
    pos_tags = nltk.pos_tag(tokenized_sentense)

    return pos_tags

print(classifier(sentense,0))