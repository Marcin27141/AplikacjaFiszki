from Flashcards import Flashcard
from View.BasicView import StartView

flashcards = [
    Flashcard("kot", "cat"),
    Flashcard("pies", "dog"),
    Flashcard("krowa", "cow"),
    Flashcard("koń", "horse"),
    Flashcard("osioł", "donkey"),
    Flashcard("kura", "hen"),
]

start_view = StartView(flashcards)
start_view.show()
