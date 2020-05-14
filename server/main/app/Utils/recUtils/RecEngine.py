from app.Utils.recUtils.builder import *

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
