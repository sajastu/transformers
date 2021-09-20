import json
import os
import random
from multiprocessing import Pool
from os import path

import re
from tqdm import tqdm


def tl_dr(ent_m):
    set, ent = ent_m
    input = ent['document']

    r1 = re.findall(r'tl.{0,3}dr', input)
    try:
        tldr_kw = r1[0]
    except:
        return None

    return set, {
        'id': ent['id'],
        'document' : input.split(tldr_kw)[0].strip(),
        'summary': ent['summary']
    }

all_posts = []
with open('/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/corpus-webis-tldr-17.json') as fR:
    for l in tqdm(fR, total=3848330):
        ent = json.loads(l.strip())
        all_posts.append(
            {
                'id': ent['id'],
                'document': ent['body'].replace('\n', '').lower(),
                'summary': ent['summary'].replace('\n', '').lower()
            }
        )
        if len(all_posts) == 10000:
            break

# set split: 98-1-1

random.seed(8080)
random.shuffle(all_posts)

splits = {
    'train': [],
    'val': [],
    'test': []
}
splits['train'] = all_posts[:int(.98 * len(all_posts))-1]
splits['val'] = all_posts[int(.98 * len(all_posts))-1: int(.99 * len(all_posts))]
splits['test'] = all_posts[int(.99 * len(all_posts)):]

# now wrting splits for BART and CurrSumm
if not path.exists('/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/splits/'):
    os.makedirs('/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/splits/')


all_ents = []
for set, instances in splits.items():
    for inst in tqdm(instances, total=len(instances)):
        all_ents.append((set,inst))

pool = Pool(40)
splits = {
    'train': [],
    'val': [],
    'test': []
}
print('Tokenizing...')
for ent_out in tqdm(pool.imap_unordered(tl_dr, all_ents), total=len(all_ents)):
    if ent_out[0] is not None:
        splits[ent_out[0]].append(ent_out[1])

print('-----------')
print('Wrting to /trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/splits/')
for set, instances in splits.items():
    with open(f'/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/splits/{set}.json', mode='w') as fW:
        for inst in tqdm(instances, total=len(instances)):
            json.dump(inst, fW)
            fW.write('\n')

