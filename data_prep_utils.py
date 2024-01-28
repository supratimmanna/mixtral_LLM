# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 15:42:14 2024

@author: User
"""
import os

def find_topic_words(sent, label):
    
    topic_str = ''
    m=0
    topics=[]
    
    while m<len(label):
        
        topic = label[m]
        if topic=='B':
            topic_str+=sent[m]
            
            for n in range(1,9):
                topic = label[m+n]
                if topic=='I':
                    topic_str = topic_str + ' ' + sent[m+n]
                if topic=='B' or topic=='O':
                    m=m+n
                    topics.append(topic_str)
                    topic_str = ''
                    break
        else:
            m+=1
    topics = (', '.join(topics))
    return topics