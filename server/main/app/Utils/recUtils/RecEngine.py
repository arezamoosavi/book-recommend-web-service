from app.Utils.recUtils.builder import *

def recBooks(book, k):
    idx = getBookId(book=book)
    if idx:
        
        bookIndx = getSimilarIndx(idx, k)
        rec_books = getListResult(bookIndx)

        return rec_books, getBookWithid(idx)
        
    else:
        return None, [book, None]
