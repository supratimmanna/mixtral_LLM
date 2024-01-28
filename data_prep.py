# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 13:04:42 2024

@author: User
"""

import os
import pandas as pd
import json
import random
from data_prep_utils import find_topic_words


curr_path = os.getcwd()
data_save_path = 'data\\ae\\laptop\\'
json_path = 'data\\ae\\laptop\\train.json'
print(json_path)

f = open(json_path)
data = json.load(f)

all_feedbacks = []
topic_for_each_feedback = []
for j in range(len(data)):
    if j%100==0:
        print(j)
        
    idx = str(j)
    
    try:
        fdbck = (' ').join(data[idx]['sentence'])
        
        
        sent = data[idx]['sentence']
        label = data[idx]['label']
        
        topics = find_topic_words(sent, label)
        all_feedbacks.append(fdbck)
        topic_for_each_feedback.append(topics)
    except:
        pass
    
    print(j, topics)
    
df = pd.DataFrame({'feedbacks':all_feedbacks, 'topics':topic_for_each_feedback})

test_samples = random.sample(range(1, len(df)), int(len(df)*0.15))

train_df = df[~(df.index.isin(test_samples))].copy().reset_index(drop=True)
test_df = df[df.index.isin(test_samples)].copy().reset_index(drop=True)

train_df.to_csv(data_save_path+'laptope_mistral_train.csv', index=False)
test_df.to_csv(data_save_path+'laptope_mistral_test.csv', index=False)
# df.to_csv('laptop.csv', index=False)
