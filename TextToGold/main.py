from text_chunk import TextChunk
from taxonomy_builder import TaxonomyBuilder
from user_interface import UserInterface

# Four test text chunks from randomly-selected Google Maps reviews
# of Vancouver General Hospital:
text_data = [
    "Great service and care from both nurses and doctors.",
    ("Visited VGH Emergency January 24, 2024.  The wait is not important. "
     "It is important to realize when you get in "
     "to see a doctor you're seeing the best  doctors ever! "
     "I was, happy and  pleased there wasn't  a shift change "
     "the doctor I saw stayed to give me my results, late night, "
     "that meant a lot to me. He is a very kind doctor. "
     "I know from experience ER and specialist, doctors sacrifice "
     " a lot of their time to take care of my medical "
     "challenges, unconditional  love, care and kindness without complaining,"
     "it is important to acknowledge all Doctors."),
    ("My sister was at the emergency yesterday she is pregnant the RN "
     "that helping us in the intake is really rude. She keeps questioning "
     "my sister why she is at the emergency and her case is not for emergency. "
     "She should not question patient or decide for the patient if it's "
     "emergency or not especially that she is not the one who experiencing pain. "
     " After we left the intake and go in the waiting area we heard her talking "
     "to her co-worker regarding to my sister case.It’s really unprofessional. "
     " She should not treat patients that way!"),
    ("I experienced a medical emergency today that resulted in a visit to "
     "the emergency department at VGH. I was attended to promptly and treated "
     "with respect and compassion by the entire staff - from registration, "
     "to the triage nurse, to the doctor who treated me, and the woman who "
     "did my bloodwork who was incredibly kind. It's clear this team is "
     "incredibly busy and under high demand, and they operated with seamless "
     "efficiency.")
]

# Create a list of TextChunk objects for each text chunk in text_data:
text_chunks = [TextChunk(text) for text in text_data]

# Initialize TaxonomyBuilder with text chunks
taxonomy_builder = TaxonomyBuilder(text_chunks)

# Initialize UserInterface with text chunks
ui = UserInterface(text_chunks)

# Display sample text chunks to the user
ui.display_chunks()

# Build the taxonomy with user input
noun_to_adjectives, adjective_to_nouns = taxonomy_builder.build_taxonomy(ui)

# Print the generated taxonomies
print("Noun to Adjectives:", noun_to_adjectives)
print("Adjective to Nouns:", adjective_to_nouns)
