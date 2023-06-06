from datetime import datetime

class Flashcard:
    def __init__(self, original, translation) -> None:
        self.original = original
        self.translation = translation

    def __getstate__(self):
        return self.original, self.translation

    def __setstate__(self, state):
        self.original, self.translation = state

    def test_answer(self, answer):
        return answer == self.translation
    
    def edit_original(self, new_original):
        self.original = new_original

    def edit_translation(self, new_translation):
        self.translation = new_translation

    def edit(self, new_original, new_translation):
        self.edit_original(new_original)
        self.edit_translation(new_translation)

class StatsFlashcard(Flashcard):
    def __init__(self, original, translation, times_correct=0, times_incorrect=0, last_tested=None) -> None:
        super().__init__(original, translation)
        self.times_correct = times_correct
        self.times_incorrect = times_incorrect
        self.last_tested = last_tested

    def __getstate__(self):
        state = super().__getstate__()
        state_dict = {
            'flashcard': state,
            'stats_flashcard': (self.times_correct, self.times_incorrect, self.last_tested)
        }
        return state_dict

    def __setstate__(self, state):
        super().__setstate__(state['flashcard'])
        self.times_correct, self.times_incorrect, self.last_tested = state['stats_flashcard']

    def test_answer(self, answer):
        is_correct = super().test_answer(answer)
        self.last_tested = datetime.now()
        if is_correct:
            self.times_correct += 1
        else:
            self.times_incorrect += 1
        return is_correct        
    
    def tested_correct(self):
        self.last_tested = datetime.now()
        self.times_correct += 1

    def tested_incorrect(self):
        self.last_tested = datetime.now()
        self.times_incorrect += 1