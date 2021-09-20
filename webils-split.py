import json
import os
import random
from os import path

from tqdm import tqdm

all_posts = []
with open('/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/corpus-webis-tldr-17.json') as fR:
    for l in tqdm(fR, total=3848330):
        ent = json.loads(l.strip())
        all_posts.append(
            {
                'document': ent['body'].replace('\n', '').lower(),
                'summary': ent['summary'].replace('\n', '').lower()
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
if not path.exists('/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/splits/'):
    os.makedirs('/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/splits/')

print('-----------')
print('Wrting to /trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/splits/')
for set, instances in splits.items():
    with open(f'/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/splits/{set}.json', mode='w') as fW:
        for inst in tqdm(instances, total=len(instances)):
            json.dump(inst, fW)
            fW.write('\n')
