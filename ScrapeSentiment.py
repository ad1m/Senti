from twython import Twython
from textblob import TextBlob

consumerKey = "ENTER HERE "
consumerSecret = "ENTER HERE"
accessToken = "ENTER HERE"
accessTokenSecret = "ENTER HERE"
#tweet['id_str']
ticker = 'Rockets'   #Search keyword here 
c = 100
t = Twython(app_key=consumerKey, app_secret=consumerSecret, oauth_token=accessToken, oauth_token_secret=accessTokenSecret)
search = t.search(q=ticker, count = c)
tweets = search['statuses']
score = 0
bullish = 0
bearish = 0
average  = 0
positiveWords = ['buy', 'bought', 'long', 'good', 'great', 'best', 'bull', 'bullish', 'up', 'buy now', 'add', 'gain', 'high', 'win', 'won', 'winner', 'awesome', 'growth']
negativeWords = ['sell', 'sold', 'short', 'bad', 'terrible', 'worst', 'bear', 'bearish', 'down', 'avoid', 'reduce', 'loss', 'trash', 'warn', 'scam', 'shit', 'crap', 'lose', 'loser']
i = 0
for tweet in tweets:
    blob = TextBlob(tweet['text'])
    for sentence in blob.sentences:
        if sentence in positiveWords:
            sentence.sentiment.polarity = .7
        if sentence in negativeWords:
            sentence.sentiment.polarity = -.7
        score = score + sentence.sentiment.polarity
        #print(sentence.sentiment.polarity)
    #print tweet['text'].lower(), '\n\n\n'

average = score/10           
print '----------------------------------------------------'
print 'score: ' , score
print 'average is: ', average
print '----------------------------------------------------'
if score > 0 and score <= .25: 
    print 'slighly positive sentiment'

if score > .25 and score <= .5:
    print 'moderatly positive sentiment'

if score > .5 and score <= 1:
    print 'very positive sentiment' 

if score >= 1:
    print 'highly positive sentiment' 

if score >= - .25 and score < 0: 
    print 'slightly negative sentiment'

if score >= - .5 and score < -.25: 
    print 'moderately negative sentiment'

if score >= -1 and score < -.5:
    print 'very negative sentiment'

if score < -1:
    print 'highly negative sentiment'
if score == 0:
    print 'average sentiment: neither positive or negative' 
print '----------------------------------------------------'

#score = 0
#twitter = Twython(app_key=consumerKey, app_secret=consumerSecret, oauth_token=accessToken, oauth_token_secret=accessTokenSecret)
#search = t.get_user_timeline(screen_name="Bloomberg")
#print search
#print '----------------------------------------------------'
