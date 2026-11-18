import argparse
import data
import math
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.txt import CountVectorizer

# Ignore 'future warnings' from the toolkit.
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

# Regression object
clf = LogisticRegression()

# Create a "vectorizer" object.	
vectorizer = CountVectorizer(analyzer='word', min_df=16, ngram_range=(1, 2))   # 1 and 2-grams, min 5 count

''' Using libraries

# load data into a row and targets
# pick features (author classification???)
# pair features to compare target and sources (cosine similarity)

'''

def train(articles):
    '''
        Given a list of passages and their novelty, we train our classifier.
        articles: list of tuples ((source1, source2, source3, target), novelty)
    '''

    # BUILDING INPUTS
    # Y_train represents labels (novelty), X_train represents article sets (we van vary this)
    
    article_sets = list()
    novelties = list()
    for article_set, novelty in articles:
        article_sets.append(article_set)
        novelties.append(novelty)

    # todo: parse out articles, build out article inpuits/embeddings
    Y_train = novelties
    #X_train = article_sets ###edit this here!!ß
    #X_train_counts = 
    
    # train classifier(s)
    clf.fit(X_train_counts, Y_train)

def test(passages):
    return 

if __name__ == '__main__':

    # Command-line argument parser
    parser = argparse.ArgumentParser(description="embedall.py")
    parser.add_argument('-data', action="store", dest="data", type=str, default='data', help='Directory containing the books')
    parser.add_argument('-test', action="store", type=bool, default=False, help='Use the test set not dev')
    args = parser.parse_args()
        
    passages = data.Passages(args.data)
    trainset = passages.get_training()
    if args.test:  testset = passages.get_test()
    else:          testset = passages.get_development()

    # TRAIN
    train(trainset)

    # TEST
    predicted_labels = test(testset)
        
    # EVALUATE
    accuracy = data.evaluate(predicted_labels, testset)
    print('Accuracy: %.2f%%\n' % (accuracy))
