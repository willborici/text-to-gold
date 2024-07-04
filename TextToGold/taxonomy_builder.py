class TaxonomyBuilder:
    def __init__(self, text_chunks):
        self.__text_chunks = text_chunks
        self.__noun_to_adjectives = {}
        self.__adjective_to_nouns = {}
        # hold pairs the user confirms so if a similar pair is encountered,
        # the user doesn't have to reconfirm - @TODO - Probably redundant once program evolves
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
            nouns = chunk.extract_nouns()
            adjectives = chunk.extract_adjectives()
            for noun in nouns:
                if noun not in self.__noun_to_adjectives:
                    self.__noun_to_adjectives[noun] = set()  # new noun entry, ready for adj.
                for adjective in adjectives:
                    if (noun, adjective) not in self.__user_confirmed_relations:
                        if user_interface.ask_user_confirmation(noun, adjective):
                            # user confirms this (noun, adj) pair is business-relevant
                            self.__user_confirmed_relations[(noun, adjective)] = True
                            # associate this adjective to the noun:
                            self.__noun_to_adjectives[noun].add(adjective)
                            # because noun-adjective is a many-to-many relationship and
                            # above we covered one-noun-to-many-adjectives, now do the
                            # reverse: one-adjective-to-many-nouns check:
                            if adjective not in self.__adjective_to_nouns:
                                self.__adjective_to_nouns[adjective] = set()
                            self.__adjective_to_nouns[adjective].add(noun)
        return self.__noun_to_adjectives, self.__adjective_to_nouns
