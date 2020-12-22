
# taking examples from assignment file
responses='''I really like the show because it is thought provoking and i like shows that make me think
             The cast.
             Nothing
             It is the most complex and original idea I have ever seen or heard of. Also, because it delves into the topic of human emotions, but in an artificial way, if I were to be punny and serious all at once. From what I have seen of the show, I believe that we, as human beings, can compare ourselves to the androids, because we can definitely relate to them.
             it has many twists and I like that
             It's unpredictable so you are left wanting more'''

import nltk
import re
from nltk.stem import WordNetLemmatizer
let=WordNetLemmatizer()
from nltk.corpus import stopwords

#converting to sentences
sent=nltk.sent_tokenize(responses)

#data cleaning and keyword generation
keywords=[]
for i in range(len(sent)):
    words= re.sub('[^a-zA-Z]', ' ', sent[i])
    words = words.lower()
    words=words.split()
    words=[let.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    words= ' '.join(words)
    keywords.append(words)


