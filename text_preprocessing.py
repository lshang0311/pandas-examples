import pandas as pd
import nltk
import string

"""
    https://stackoverflow.com/questions/33098040/how-to-use-word-tokenize-in-data-frame
    https://stackoverflow.com/questions/33245567/stopword-removal-with-nltk-and-pandas/33246035
    
    https://medium.com/@chaimgluck1/have-messy-text-data-clean-it-with-simple-lambda-functions-645918fcc2fc

"""

nltk.download('punkt')
nltk.download('stopwords')

# input
df = pd.DataFrame({
    'sentences':
        [
            'This is a very good site. I will recommend it to others.',
            'Can you please give me a call at 9983938428. have issues with the listings.',
            'good work! keep it up'
        ]
})

# lower case
df['lower_case'] = df['sentences'].apply(lambda x: x.lower())
table = str.maketrans({}.fromkeys(string.punctuation))
df['punctuation_removed'] = df['sentences'].apply(lambda x: x.translate(table))

# tokenize
df['tokenized_1'] = df.apply(lambda row: nltk.word_tokenize(row['sentences']), axis=1)

# tokenize
df['tokenized_2'] = df['sentences'].apply(nltk.word_tokenize)

# stopword removal
stop = nltk.corpus.stopwords.words('english')
df['stopwords_removed'] = df['tokenized_1'].apply(lambda x: [item for item in x if item not in stop])

print(df)
