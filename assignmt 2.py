

import fuzzywuzzy
from fuzzywuzzy import process

keywords = ['Good/like the show/everything','thought provoking',
            'Complex storyline',
            'Original',
            'Suspense/Mystery/thrillers',
            'Attention grabbing/holds interest/keeps you wanting to watch more'
           ]
responses = 'I really like the show because it is thought provoking and i like shows that make me think'

print(process.extractBests(responses,keywords,limit=2))
