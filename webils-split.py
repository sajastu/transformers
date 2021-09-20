import json
import random

from tqdm import tqdm

3,848,330

all_posts = []
with open('') as fR:
    for l in tqdm(fR, total=3848330):
        ent = json.loads(l.strip())
        all_posts.append(
            {
                'src': ent['body'],
                'summary': ent['summary']
            }
        )

# set split: 98-1-1

random.seed(8080)
random.shuffle(all_posts)

splits = {
    'train': [],
    'val': [],
    'test': []
}
splits['train'] = all_posts[:int(.98 * len(all_posts))]
splits['val'] = all_posts[int(.98 * len(all_posts)): int(.99 * len(all_posts))]
splits['test'] = all_posts[int(.99 * len(all_posts)):]

# now wrting splits for BART and CurrSumm
