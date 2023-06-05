from Flashcards import Flashcard, StatsFlashcard
from FlashcardsSet import FlashcardsSet
import pytest

(TEST_ORIGINAL, TEST_TRANSLATION) = ("test1", "test2")
cat_flashcard = Flashcard("kot", "cat")
dog_flashcard = Flashcard("pies", "dog")
cow_flashcard = Flashcard("krowa", "cow")

@pytest.mark.parametrize("name, flashcards", [
    ("some_set", [cat_flashcard, dog_flashcard, cow_flashcard]),
    ("", []),
    ("other_set", None),
])
def test_valid_answers(name, flashcards):
    _set = FlashcardsSet(name, flashcards)
    assert _set.name == name and _set.flashcards == flashcards