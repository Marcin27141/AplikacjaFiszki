from Flashcards import Flashcard, StatsFlashcard
import time
import pytest

(TEST_ORIGINAL, TEST_TRANSLATION) = ("test1", "test2")
cat_flashcard = Flashcard("kot", "cat")
dog_flashcard = Flashcard("pies", "dog")
cow_flashcard = Flashcard("krowa", "cow")

@pytest.mark.parametrize("flashcard, answer", [
    (cat_flashcard, "cat"),
    (dog_flashcard, "dog"),
    (cow_flashcard, "cow"),
])
def test_valid_answers(flashcard, answer):
    assert flashcard.test_answer(answer) == True

@pytest.mark.parametrize("flashcard, answer", [
    (cat_flashcard, "Cat"),
    (cat_flashcard, "c at"),
    (cat_flashcard, " cat"),
    (cat_flashcard, "cat "),
    (cat_flashcard, ""),
    (cat_flashcard, " "),
])
def test_invalid_answers(flashcard, answer):
    assert flashcard.test_answer(answer) == False

def test_original_edit():
    EDIT_APPEND = "_edited"
    test_stat_flashcard = StatsFlashcard(TEST_ORIGINAL, TEST_TRANSLATION)
    test_stat_flashcard.edit_original(TEST_ORIGINAL + EDIT_APPEND)
    assert test_stat_flashcard.original == TEST_ORIGINAL + EDIT_APPEND

def test_translation_edit():
    EDIT_APPEND = "_edited"
    test_stat_flashcard = StatsFlashcard(TEST_ORIGINAL, TEST_TRANSLATION)
    test_stat_flashcard.edit_translation(TEST_TRANSLATION + EDIT_APPEND)
    assert test_stat_flashcard.translation == TEST_TRANSLATION + EDIT_APPEND

def test_flashcard_edit():
    EDIT_APPEND = "_edited"
    test_stat_flashcard = StatsFlashcard(TEST_ORIGINAL, TEST_TRANSLATION)
    test_stat_flashcard.edit(TEST_ORIGINAL + EDIT_APPEND, TEST_TRANSLATION + EDIT_APPEND)
    assert test_stat_flashcard.original == TEST_ORIGINAL + EDIT_APPEND
    assert test_stat_flashcard.translation == TEST_TRANSLATION + EDIT_APPEND

def test_initial_stats():
    test_stat_flashcard = StatsFlashcard(TEST_ORIGINAL, TEST_TRANSLATION)
    assert test_stat_flashcard.last_time_tested == None
    assert test_stat_flashcard.times_right == 0
    assert test_stat_flashcard.times_wrong == 0

def test_stats_wrong_increment():
    test_stat_flashcard = StatsFlashcard(TEST_ORIGINAL, TEST_TRANSLATION)
    test_stat_flashcard.test_answer(TEST_TRANSLATION + "wrong answer")
    assert test_stat_flashcard.times_wrong == 1
    assert test_stat_flashcard.times_right == 0

def test_stats_right_increment():
    test_stat_flashcard = StatsFlashcard(TEST_ORIGINAL, TEST_TRANSLATION)
    test_stat_flashcard.test_answer(TEST_TRANSLATION)
    assert test_stat_flashcard.times_wrong == 0
    assert test_stat_flashcard.times_right == 1

def test_stats_date_update():
    TIME_SLEEP = 1
    test_stat_flashcard = StatsFlashcard(TEST_ORIGINAL, TEST_TRANSLATION)
    test_stat_flashcard.test_answer(TEST_TRANSLATION)
    first_check = test_stat_flashcard.last_time_tested
    assert first_check != None
    time.sleep(TIME_SLEEP)
    test_stat_flashcard.test_answer(TEST_TRANSLATION + "wrong answer")
    second_check = test_stat_flashcard.last_time_tested
    assert second_check != None and second_check != first_check
