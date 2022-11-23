#use the nltk library to process headlines and articles grabbed from the nasdaq site and the sites it links to

# https://python.gotrained.com/nltk-corupus/

verbose = True

if(verbose): print("importing modules")
from nltk.corpus import PlaintextCorpusReader
import ndaqfxns as n
import os

if(verbose): print("initializing corpus")
corpus_root = "./"
file_ids = ".*.json"
corpus = PlaintextCorpusReader(corpus_root,file_ids)

#verify corpus was created correctly
print(corpus.fileids())
print(corpus.words(corpus.fileids()[0]))


