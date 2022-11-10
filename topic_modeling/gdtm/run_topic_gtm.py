from settings.common import get_pp_pipeline, load_flat_dataset, save_flat_dataset
from settings.ngrams import insert_ngrams_flat_from_lists
from preprocessing_pipeline.NextGen import NextGen
import csv
from settings.common import load_flat_dataset
from settings.ngrams import insert_ngrams_flat_from_lists
import pandas as pd 
import os 


dataset_name = 'sample_tweets'
seed_topics_file = "data_gtm/{}_seed_topics.csv".format(dataset_name)
data_path = 'data_gtm/{}.csv'

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
dataset = load_flat_dataset("data_gtm/{}.csv".format(dataset_name))

# remove all mentions in the data
dataset1 = []
for d in dataset:
    tmp = []
    for i in d:
        if '@' not in i:
            tmp.append(i)
    dataset1.append(tmp)
dataset = dataset1

# add bigrams to the dataset
ngrams = []
with open("data_gtm/{}_seed_topics.csv".format(dataset_name), 'r') as f:
    for line in f:
        topic = line.strip().split(',')
        for w in topic:
            if '$' in w:
                ngrams.append(w)
dataset = insert_ngrams_flat_from_lists(dataset, ngrams, [])
all_bigram = []
for i in dataset:
    tmp = []
    for index in range(0,len(i)-1):
        tmp.append('$'.join(i[index:index+2]))
    all_bigram.append(tmp)
dataset.extend(all_bigram)


model = GTM(dataset=dataset, mallet_tnd_path=tnd_path, mallet_gtm_path=gtm_path, 
              tnd_k=30, gtm_k=30, tnd_beta1 = 25, over_sampling_factor=100, phi=10,
              top_words=35,tnd_iterations=1000, gtm_iterations=1000, seed_topics_file=seed_topics_file)

topics = model.get_topics()
noise = model.get_noise_distribution()

print(noise)
with open('data_gtm/'+dataset_name+"_gtm_topics.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(topics)


cmd = 'rm /tmp/750b80*'
os.system(cmd)
cmd = 'rm /tmp/f86f5*'
os.system(cmd)
