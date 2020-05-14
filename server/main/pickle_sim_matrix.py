
def load_data():
    from pandas import read_csv
    return read_csv('app/Utils/recUtils/goodreads_data.csv',index_col=0)
books_df = load_data()

def get_cosine_sim():
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import linear_kernel

    tf_corpus = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix_corpus = tf_corpus.fit_transform(books_df['corpus'])
    cosine_sim_corpus = linear_kernel(tfidf_matrix_corpus, tfidf_matrix_corpus)
    return cosine_sim_corpus

def main():
    import pickle

    data = get_cosine_sim()

    # Store data (serialize)
    with open('app/Utils/recUtils/sim_matrix.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    # books_df.to_pickle("app/Utils/recUtils/goodreads_data.pkl")

if __name__ == "__main__":
    main()