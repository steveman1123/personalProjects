# https://python.gotrained.com/nltk-corupus/

from nltk.corpus import PlaintextCorpusReader
import os

corpus_root = "./"
file_ids = ".*.json"
corpus = PlaintextCorpusReader(corpus_root,file_ids)

#verify corpus was created correctly
print(corpus.fileids())
print(corpus.words(corpus.fileids()[0]))


