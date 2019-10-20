## SentencePiece
SentencePiece was released from google to do text tokenization. It's an unsupervised text tokenizer for Neural Network-based text generation. I tried to make it easy to use for the Bengali language. 

##Usages
In Bengali language we generally do tokenization based on whitespace and punctuations (e.g , . ; |). But by using this unsupervised tokenization model we can generate tokens list that can be easily used in many language models like word2vec, XLM, BERT or LASER to get context from Bengali language story. One of my major concerns to use this model for my other NLP/NLU task. 

## How
    1. Collect your Bengali raw data corpus & store it in a dir as pickle format.
    2. code base use **data/** as a corpus dir
    3. Use main.py to train SentencePiece model
    4. Change params from main.py file.
    5. Trained model will save on "mode/" dir
    
## Acknowledgement
Don't forget to say thanks to [goru001](https://github.com/goru001) for his awesome collections of bengali [WikiData](https://drive.google.com/drive/folders/1GC76qIGbly4sKX9XsUP_OtsI80nJ6lQ4). He also mantain a great Bengali-NLP task repo [nlp-for-bengali](https://github.com/goru001/nlp-for-bengali)

## Then
To know, is to know that you know nothing.
That is the meaning of true knowledge.
**Socrates**