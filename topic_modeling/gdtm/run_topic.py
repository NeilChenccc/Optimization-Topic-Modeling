from settings.common import get_pp_pipeline, load_flat_dataset, save_flat_dataset
from settings.ngrams import insert_ngrams_flat_from_lists
from preprocessing_pipeline.NextGen import NextGen
import csv
from settings.common import load_flat_dataset
from settings.ngrams import insert_ngrams_flat_from_lists
import pandas as pd 


dataset_name = 'sample_tweets'

data_path = 'data/{}.csv'

pp = get_pp_pipeline(remove_stopwords=True, stem=False, clean_twitter=False)

ds_path = data_path.format(dataset_name + '_raw')

dataset = load_flat_dataset(ds_path, delimiter=' ')
ng = NextGen()
clean_ds = ng._preprocess_dataset(dataset=dataset, pp=pp)
save_flat_dataset(data_path.format(dataset_name), clean_ds, delimiter=' ')



dataset = []
from src.gdtm.helpers.common import load_flat_dataset
from src.gdtm.models import GTM, NLDA

tnd_path = '../topic-noise-models-source/mallet-tnd/bin/mallet'
lda_path = '../topic-noise-models-source/mallet-lda/bin/mallet'
gtm_path = '../topic-noise-models-source/mallet-gtm/bin/mallet'
dataset = load_flat_dataset("data/{}.csv".format(dataset_name))


all_bigram = []
for i in dataset:
    tmp = []
    for index in range(0,len(i)-1):
        tmp.append('$'.join(i[index:index+2]))
    all_bigram.append(tmp)
dataset.extend(all_bigram)

model = NLDA(dataset=dataset, mallet_tnd_path=tnd_path, mallet_lda_path=lda_path, 
             tnd_k=30, lda_k=30,tnd_beta1 = 25, phi=10, top_words=20)

topics = model.get_topics()
noise = model.get_noise_distribution()

print(noise)
with open('data/'+dataset_name+"_topics.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(topics)