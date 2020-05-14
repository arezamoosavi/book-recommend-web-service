from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from app.Utils.recUtils.builder import *

tf_corpus = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix_corpus = tf_corpus.fit_transform(books['corpus'])
cosine_sim_corpus = linear_kernel(tfidf_matrix_corpus, tfidf_matrix_corpus)


def recBooks(book, k):
    idx = getBookId(book=book)
    if idx:
        
        listScores = list(enumerate(cosine_sim_corpus[idx]))
        sim_scores = sorted(listScores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:k+1]
        
        book_indices = [i[0] for i in sim_scores]
        rec_books = getDictResult(book_indices)

        return rec_books, getBookWithid(idx)
        
    else:
        return None, [book, None]
