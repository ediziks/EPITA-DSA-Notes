import sys
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')


def transform(file_name):
    """
    transform the words from file into bitext representation, and save into a file
    :param file_name:
    :return:
    """
    # read the file
    with open(file_name, 'r') as f:
        lines = f.readlines()
    # remove the \n
    lines = [line.strip() for line in lines]
    # remove the empty lines
    lines = [line for line in lines if line]
    # remove the punctuations
    lines = [re.sub(r'[^\w\s]', '', line) for line in lines]
    # remove the stop words
    stop_words = set(stopwords.words('english'))
    lines = [line for line in lines if line not in stop_words]
    # lemmatize the words
    lemmatizer = WordNetLemmatizer()
    lines = [lemmatizer.lemmatize(line) for line in lines]
    # stem the words
    stemmer = PorterStemmer()
    lines = [stemmer.stem(line) for line in lines]
    fname = file_name.split('.')[0]
    # write the words into a file
    with open(f'./{fname}.bitext.txt', 'w') as f:
        for line in lines:
            f.write(line + '\n')
    

if __name__ == '__main__':
    transform(sys.argv[1])
    print('Done!')