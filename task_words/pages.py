from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time

class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['expiry_timestamp'] = time.time() + 5*60


class Task(Page):
    form_model = 'player'
    form_fields = ['submitted_answer', 'word_increment']


    def vars_for_template(self):
        return {
            'word': self.player.current_question()['question'],
            'word_id' : self.player.word_show + 1, ## Seems easier to just use the word_show variable (and not have a word_id variable)
            'player_in_previous_rounds': reversed(self.player.in_previous_rounds()), # show the last period first
            'total_payoff': sum([p.payoff for p in self.player.in_all_rounds()]),
        }

    # Validate all form fields at once
    def error_message(self, values):
        if values['word_increment']==0:
            if self.player.validate_answer(str(values['submitted_answer'])) == False:
                return 'The word you introduced is too short, use at least 5 characters'

    def before_next_page(self):
        self.player.set_payoffs()

        if self.player.word_increment==1:
            self.player.word_show += 1
        else:
            if self.player.validate_answer(self.player.submitted_answer):
                self.player.word_check()

        timer_text = 'Time left to complete this task:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


page_sequence = [
    Start,
    Task,
]

