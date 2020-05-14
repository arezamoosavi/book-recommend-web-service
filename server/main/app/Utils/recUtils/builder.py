
def load_data():
    import pandas as pd
    return pd.read_csv('goodreads_data.csv',index_col=0)
books_df = load_data()


def look_for_book(df, name):
    return df[df.title.str.contains(name.lower(), na=False)]

def getBookId(book):
    book_df = look_for_book(books_low, name=book)
    
    if book_df.empty:
        return None
    else:
        return book_df.index.values[0]

def getBookWithid(x):
    d= [books_df.title.iloc[x], books_df.authors.iloc[x]]
    return d

def getDictResult(bookInx):
    res = []
    for i in range(len(bookInx)):
        x = bookInx[i]
        d = {i+1: {'book' : books_df.title.iloc[x], 'authors' : books_df.authors.iloc[x]}} 
        res.append(d)
    return res
