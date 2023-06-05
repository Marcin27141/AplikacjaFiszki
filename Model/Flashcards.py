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
    def __init__(self, original, translation) -> None:
        super().__init__(original, translation)
        self.times_right = 0
        self.times_wrong = 0
        self.last_time_tested = None

    def __getstate__(self):
        state = super().__getstate__()
        state.update({
            'stats_flashcard': (self.times_right, self.times_wrong, self.last_time_tested)
        })
        return state

    def __setstate__(self, state):
        super().__setstate__(state)
        self.time_right, self.times_wrong, self.last_time_tested = state['stats_flashcard']
        
    def test_answer(self, answer):
        is_correct = super().test_answer(answer)
        self.last_time_tested = datetime.now()
        if is_correct:
            self.times_right += 1
        else:
            self.times_wrong += 1
        return is_correct        