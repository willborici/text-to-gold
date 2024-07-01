class TaxonomyBuilder:
    def __init__(self, text_chunks):
        self.__text_chunks = text_chunks
        self.__noun_to_adjectives = {}
        self.__adjective_to_nouns = {}
        self.__user_confirmed_relations = {}

    @property
    def noun_to_adjectives(self):
        return self.__noun_to_adjectives

    @property
    def adjective_to_nouns(self):
        return self.__adjective_to_nouns

    # Method to build the taxonomy
    def build_taxonomy(self, user_interface):
        for chunk in self.__text_chunks:
            nouns, adjectives = chunk.extract_nouns_and_adjectives()
            for noun in nouns:
                if noun not in self.__noun_to_adjectives:
                    self.__noun_to_adjectives[noun] = set()
                for adjective in adjectives:
                    if (noun, adjective) not in self.__user_confirmed_relations:
                        if user_interface.ask_user_confirmation(noun, adjective):
                            self.__user_confirmed_relations[(noun, adjective)] = True
                            self.__noun_to_adjectives[noun].add(adjective)
                            if adjective not in self.__adjective_to_nouns:
                                self.__adjective_to_nouns[adjective] = set()
                            self.__adjective_to_nouns[adjective].add(noun)
        return self.__noun_to_adjectives, self.__adjective_to_nouns
