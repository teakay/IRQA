**A simple Information Retrieval Based Question Answering System**

The system contain four modules : 
1. Question Analysis Module
* Built upon LSTM model to identified question type and used keyword extraction to generate query

2. Information Retrieval Module
* Implement ElasticSearch and plugged XGBoost model as learning to rank algorithm using Letor dataset

3. Passage Retrieval Module
* Using BM25 scoring to get most relevant paragraph based on query

4. Answer Extraction Module.
* Fine-tune BERT model to do answer span extraction

![IR-QA-system](https://github.com/user-attachments/assets/42073d2a-6e9f-48fb-95fd-5dd8d953b6b7)
