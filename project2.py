# from logging import logMultiprocessing
# from pkg_resources import LegacyVersion
import tweepy
from google.cloud import language_v1
import sys
import string
import re
import time

def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        if (sentence.text.content[0:5] == 'https'):
            print("it is a picture")
        else:
            print(u"Sentence text: {}".format(sentence.text.content))
            print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
            print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))
    print("\n")
    return sentence.sentiment.score

def sample_analyze_sentiment_zh(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "zh"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))
    print("\n")




consumer_key = "llEDRrYlF3aOb9V9jMR1lWzZf"
consumer_secret = "8XUbnox3Cox5lEAXOcAnAmlxP43ZUa2juZeRh46Jz8OLrdS4pi"
access_key = "1442202224973676548-d3Kq7BSdveVcRTx37jmI6Xtszm2iQn"
access_secret = "nxLjK9C86kqUgE2Tsx2ytSkW5AKWMOKksmCFlwmO9Pwgn"



# Create an Api instance.
#submit key and secret.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


# for tweet in tweepy.Cursor(api.search_users, q='League of Legends').items(8):
#     print(tweet.screen_name)


# recent_tweet = api.user_timeline('YuhanCh71346999')
# for twee in recent_tweet:
#     sample_analyze_sentiment(tweet.text)
def get_keywords_from_input(keywords):
    keywords_list=keywords.split(',')
    for index in range(len(keywords_list)):
        keywords_list[index] = keywords_list[index].strip()
    return keywords_list

def get_keywords_from_param():
    args = sys.argv
    return args[1:]
def main():
    start = time.time()
    keywords = get_keywords_from_param()
    keywords = get_keywords_from_param()
    if keywords != []:
        flag = input('You want to search {}. y/n: '.format(''.join(keywords)))
        while (flag != 'y' and flag != 'n'):
            flag = input('Please choose exactly y/n: ')
        while (flag == 'n'):
            keywords = input('You need to provide at least one keyword.\nYou can use comma to split.\nEmpty input will be seen as stop program.\nNow please give me keywords:\n')
            if keywords == '':
                print('Program stop')
                return 0
            else:
                keywords = get_keywords_from_input(keywords)
                flag = input('You want to search {}. y/n: '.format(' and '.join(keywords)))
                while (flag != 'y' and flag != 'n'):
                    flag = input('Please choose exactly y/n: ')
            
    else:
        flag = 'n'
        while (flag == 'n'):
            keywords=input('You need to provide at least one keyword.\nYou can use comma to split.\nEmpty input will be seen as stop program.\nNow please give me keywords:\n')
            if keywords == '':
                print('Program stop')
                return 0
            else:
                keywords = get_keywords_from_input(keywords)
                flag = input('You want to search {}. y/n: '.format(' and '.join(keywords)))
                while (flag != 'y' and flag != 'n'):
                    flag = input('Please choose exactly y/n: ')
    end = time.time()
    for keyword in keywords:
        searchr = api.search_tweets(q = keywords, lang='en',count = 5)
        pt = api.home_timeline()
        score = []
        for tweet in searchr:
            score.append(sample_analyze_sentiment(tweet.text))

        le = len(score)

        t = 0

        for i in range(0,le):
            t = t +score[i]

        ave = t / le

    print("the avergae of score is", ave)
    
    return end-start

if __name__=='__main__':
    main()

