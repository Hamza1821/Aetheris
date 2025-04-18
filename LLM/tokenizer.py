import re
# import nltk
# from nltk.tokenize import word_tokenize

# nltk.download('punkt_tab')
tokens=[]
with open("dataset/the-verdict.txt","r",encoding="utf-8") as f:
    raw_text=f.read()
    tokens=re.split(r'([,.:;?_!"()\']|--|\s)',raw_text)
    # tokens = word_tokenize(raw_text)
# print("total number of characters = ", len(raw_text))
preprocessed=[token for token in tokens if token and token.strip()]

all_words=sorted(set(preprocessed))

vocab={token:integer for integer,token in enumerate(all_words)}

# print("vocab : " ,vocab)

# print(raw_text)


class SimpleTokenizerV1 :
    def __init__(self,vocab):
        self.str_to_int=vocab
        self.int_to_str={s:i for i,s in vocab.items()}
    
    def encode(self,text):
        preprocessed=re.split(r'([,.:;?_!"()\']|--|\s)',text)
        preprocessed=[token.strip() for token in preprocessed if token and token.strip()]
        ids=[self.str_to_int[s] for s in preprocessed]
        return ids
    
    def decode(self,ids):
        text=" ".join(self.int_to_str[i] for i in ids)
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        text = re.sub(r'\s*\'\s*', '\'', text)
        return text



tokenizer=SimpleTokenizerV1(vocab)
my_text="It's the last he painted, said Mrs Gisburn."
ids=tokenizer.encode(my_text)
print("ids are = ",ids)

decoded_text=tokenizer.decode(ids)
print("decoded text is = ", decoded_text)