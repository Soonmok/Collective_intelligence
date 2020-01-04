from sklearn.datasets import load_iris

from modules.cluster import hcluster, drawdendrogram

if __name__=="__main__":
    data = load_iris()
    data_vecs = data.data
    labels = data.target_names
    clust = hcluster(data_vecs)
    drawdendrogram(clust)