

# Check for presence of a tldr pattern
import json
import re
from multiprocessing import Pool

from tqdm import tqdm


def tl_dr(ent):

    input = ent['document']

    r1 = re.findall(r'tl.{0,3}dr', input)
    tldr_kw = r1[0]

    return {
        'id': ent['id'],
        'document' : input.split(tldr_kw)[0].strip(),
        'summary': ent['summary']
    }

all_ents = []
for set in ['train', 'val', 'test']:
    with open(f'/trainman-mount/trainman-k8s-storage-349d2c46-5192-4e7b-8567-ada9d1d9b2de/webis-tldr/splits/{set}.json') as fR:
        for l in tqdm(fR):
            ent = json.loads(l.strip())
            all_ents.append((set, ent))



