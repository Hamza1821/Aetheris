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
tokens=[token for token in tokens if token and token.strip()]

print("tokens : " ,tokens)

# print(raw_text)