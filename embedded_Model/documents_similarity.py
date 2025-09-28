
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')


documents = [
    "Sachin Tendulkar is one of the greatest batsmen in cricket history. He played for India and is known as the 'Master Blaster'.",
    "Virat Kohli is an Indian cricketer famous for his aggressive batting style and consistency across all formats.",
    "MS Dhoni is a legendary Indian wicketkeeper and captain who led India to World Cup victories in 2007 and 2011.",
    "AB de Villiers from South Africa is known for his innovative shots and explosive batting, often called Mr. 360.",
    "Ben Stokes is an English all-rounder known for his match-winning performances and fighting spirit, especially in Test matches."
]

query='tell me about virat kohli'

# doc mebedding
doc_embedding=embedding.embed_documents(documents)
# query embedding 
query_embedding = embedding.embed_query(query)


# find similarity 
# print(cosine_similarity([query_embedding],doc_embedding))

score=cosine_similarity([query_embedding],doc_embedding)[0]
# print(list(enumerate(score)))

#
#  
index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is :",score)
