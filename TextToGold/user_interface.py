import random


class UserInterface:
    __LEARNED_ASSOCIATIONS = 0.8  # the rate at which the program has learned to associate pairs

    def __init__(self, text_chunks):
        self.__text_chunks = text_chunks
        self.__user_input_count = 0
        self.__total_relations = 0

    @property
    def user_input_count(self):
        return self.__user_input_count

    @property
    def total_relations(self):
        return self.__total_relations

    # Method to display a sample of text chunks (min. 4 for testing purposes)
    def display_chunks(self):
        sample_chunks = random.sample(self.__text_chunks, min(4, len(self.__text_chunks)))
        for i, chunk in enumerate(sample_chunks):
            print(f"Chunk {i + 1}: {chunk.text}")

    # Method to ask user for confirmation until such time as the program
    # has learned to associate adjectives and nouns at least
    # (1.0 - self.__LEARNED_ASSOCIATIONS)% of the time
    # TODO: Work on this logic as it tends to terminate too early -- uncomment the if below to begin
    def ask_user_confirmation(self, noun, adjective):
#        if (float(self.__user_input_count / max(1, self.__total_relations))
#                < (1.0 - self.__LEARNED_ASSOCIATIONS)):
            user_input = input(f"Does the adjective '{adjective}' describe the noun '{noun}'? (y/n): ")
            self.__total_relations += 1
            if user_input.lower() == 'y':
                self.__user_input_count += 1
                return True
            elif user_input.lower() == 'n':
                return False
            else:
                user_input = input("Enter y for yes, n for no. Press x to terminate: ")
                if user_input.lower() == 'x':
                    exit()  # TODO: Replace this conditional later once program is interactive
