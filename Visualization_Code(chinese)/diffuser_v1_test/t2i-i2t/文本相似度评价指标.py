from transformers import BertTokenizer, BertModel
import torch
from scipy.spatial.distance import cosine

'''
BERT（来自转换器的双向编码器表示）:
BERT 是一个强大的预训练模型，用于自然语言理解。
使用“transformers”库来加载预先训练的 BERT 模型并计算句子嵌入或相似性。

'''
# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Example sentences
sentence1 = "Hello, how are you?"
sentence2 = "Hi, how are you doing?"

# Tokenize and obtain embeddings
inputs1 = tokenizer(sentence1, return_tensors="pt")
inputs2 = tokenizer(sentence2, return_tensors="pt")

with torch.no_grad():
    embeddings1 = model(**inputs1).last_hidden_state.mean(dim=1).squeeze().numpy()
    embeddings2 = model(**inputs2).last_hidden_state.mean(dim=1).squeeze().numpy()

# Calculate cosine similarity
similarity_score = 1 - cosine(embeddings1, embeddings2)
print(f"Cosine Similarity: {similarity_score}")