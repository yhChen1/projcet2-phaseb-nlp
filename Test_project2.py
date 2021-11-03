
import project2
import pytest
import tweepy


consumer_key = "llEDRrYlF3aOb9V9jMR1lWzZf"
consumer_secret = "8XUbnox3Cox5lEAXOcAnAmlxP43ZUa2juZeRh46Jz8OLrdS4pi"
access_key = "1442202224973676548-d3Kq7BSdveVcRTx37jmI6Xtszm2iQn"
access_secret = "nxLjK9C86kqUgE2Tsx2ytSkW5AKWMOKksmCFlwmO9Pwgn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def test_get_keyword_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"Genshin,Boston University")
    keywords_input = input('give me keywords (use comma to split):')
    get_keywords = project2.get_keywords_from_input(keywords_input)
    assert get_keywords == ['Genshin','Boston University']

def test_get_keyword_param():
    get_keywords = project2.get_keywords_from_param()
    assert get_keywords == ['Test_project2.py']


