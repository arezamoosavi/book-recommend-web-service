
def load_data():
    from pandas import read_csv
    return read_csv('app/Utils/recUtils/goodreads_data.csv',index_col=0)
books_df = load_data()

# from pandas import read_pickle
# books_df = read_pickle("app/Utils/recUtils/goodreads_data.pkl")

# Load data (deserialize)
with open('app/Utils/recUtils/sim_matrix.pickle', 'rb') as handle:
    from pickle import load
    cosine_sim_corpus = load(handle)

def look_for_book(df, name):
    return df[df.title.str.contains(name.lower(), na=False)]

def getBookId(book):
    book_df = look_for_book(books_df, name=book)
    
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

