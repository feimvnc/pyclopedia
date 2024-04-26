from sentence_transformers import SentenceTransformer, util
# Model for computing sentence embeddings. 
model = SentenceTransformer('all-MiniLM-L6-v2')
sentences = [
    'i want the red color',
    'these are some interesting articles',
    'want to buy this',
    'very insightful article',
    'wanna buy this product',
    'buy this',
    'this article is really good',
    'i want the blue color',
    'i would like to buy this',
    'do you have another color'
]
embeddings = model.encode(sentences)
clusters = util.community_detection(embeddings, min_community_size=2, threshold=0.5, batch_size=len(embeddings))
#Print all clusters with the members
for i, cluster in enumerate(clusters):
    print("\nCluster {}, #{} Elements ".format(i+1, len(cluster)))
    for sentence_id in cluster:
        print("\t", sentences[sentence_id])