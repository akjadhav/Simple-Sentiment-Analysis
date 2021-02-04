from nltk.sentiment import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

title = input('Enter a sentence for Sentiment Analyzation: ')
print('\n')

global positivecounter
global negativecounter
global neutralcounter

neg = 0.000
pos = 0.000
neu = 0.000
negposneu = []

ss = sid.polarity_scores(title)
values = ss

neg = float(values['neg'])
neu = float(values['neu'])
pos = float(values['pos'])

negposneu.append(neg)
negposneu.append(neu)
negposneu.append(pos)

neg = neg * 100.0
neu = neu * 100.0
pos = pos * 100.0

print(title)
print('Positive: ', pos, '%')
print('Neutral: ', neu, '%')
print('Negative: ', neg, '%')
print(' ')


test
test 2
