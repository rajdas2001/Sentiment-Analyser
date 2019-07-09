from aylienapiclient import textapi

#application_id = "a0fbf0c1"
#application_key = "0485c1dbab34d2cafd2dafdafab2875f"
x = input("Enter a sentence")
c = textapi.Client("a0fbf0c1", "0485c1dbab34d2cafd2dafdafab2875f")
s = c.Sentiment({'text': x})
print(s)
print("Polarity:", s['polarity'])
print("Polarity Confidence:",s['polarity_confidence']*100,"%")