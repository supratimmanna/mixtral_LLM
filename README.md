# mixtral_LLM
This repo contains finetuning code for mistral 7B model

> **Data**

There are different types of data available for fine tuning and the data location is: **_'data/ae/'_**.

For this fine tuning part we use the **_dataset/ae/laptop/_** data. It contains several feedbacks for purchased laptops.

Initally the data are in .json format are not suitable to feed into the model. So, we create the data according to the model and tha has been done in the **_data_prep.py_**
file
> **The model**

We use a pre-trained Mistral-7B model. One can look into the **_finetuning.ipynb_** file to get a detailed understanding of the fine-tuning process. 
