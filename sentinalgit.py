from aylienapiclient import textapi

#application_id = ""
#application_key = ""
x = input("Enter a sentence")
c = textapi.Client("Enter application id", "Enter application key")
s = c.Sentiment({'text': x})
print(s)
print(s['polarity'])