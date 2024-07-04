import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Ensure you have the necessary NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


class TextChunk:
    def __init__(self, text):
        self.__text = text
        self.__tokens = word_tokenize(text)
        self.__pos_tags = pos_tag(self.__tokens)

    @property
    def text(self):
        return self.__text

    # Method to extract nouns and adjectives as sets
    # (we care about unique, unordered elements, but recast them to lists for convenience
    def extract_nouns_and_qualifiers(self):
        nouns = list(set([word for word, pos in self.__pos_tags if pos.startswith('NN')]))
        qualifiers = (self.extract_adjectives() + self.extract_adverbs() +
                      self.extract_determiners() + self.extract_possessives())
        # return nouns and a unique list o qualifiers
        return nouns, list(set(qualifiers))

    def extract_nouns(self):
        nouns = list(set([word for word, pos in self.__pos_tags if pos.startswith('NN')]))
        return nouns

    def extract_adjectives(self):
        adjectives = list(set([word for word, pos in self.__pos_tags if pos.startswith('JJ')]))
        return adjectives

    def extract_adverbs(self):
        adverbs = list(set([word for word, pos in self.__pos_tags if pos.startswith('RB')]))
        return adverbs

    def extract_determiners(self):
        determiners = list(set([word for word, pos in self.__pos_tags if pos.startswith('DT')]))
        return determiners

    def extract_possessives(self):
        possessives = list(set([word for word, pos in self.__pos_tags if pos in ['PRP$', 'PRP']]))
        return possessives
