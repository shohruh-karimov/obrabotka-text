from pymystem3 import Mystem
from tqdm import tqdm
from joblib import Parallel, delayed
batch_size = 1000

myText = ['МАМА мыла раму {}'.format(i) for i in range(100000)]

text_batch = [myText[i: i + batch_size] for i in range(
    0, len(myText), batch_size
)]

def lemmatize(text):
    m = Mystem()
    merget_text = "|".join(text)

    doc = []
    res = []

    for t in m.lemmatize(merget_text):
        if t != "|":
            doc.append(t)
        else:
            res.append(doc)
        doc = []
    return res
processing_text = Parallel\
    (n_jobs= -1)\
    (delayed(lemmatize)(t) for t in tqdm(text_batch))