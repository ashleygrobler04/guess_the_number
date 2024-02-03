import pygame
import state
import globals
import speech
import random

main_state_machine = state.state_machine()


class intro_state(state.state):
    def enter(self):
        speech.speak(globals.t.translate(
            "welcome to guess the number", globals.selected_language))

    def update(self):
        res = globals.main_menu.show("Main menu")
        if res == "exit":
            quit()
        else:
            main_state_machine.to("input")

    def exit(self):
        globals.tries = 0
        globals.guess = random.randint(1, 50)


class game_over_state(state.state):
    def enter(self):
        pass

    def update(self):
        speech.speak(
            f"{globals.t.translate('game over',globals.selected_language,guess=globals.guess)}")
        main_state_machine.to("main menu")

    def exit(self):
        pass


class input_state(state.state):
    def enter(self):
        self.text = ""
        self.index = 0
        speech.speak(globals.t.translate(
            "input numbers", globals.selected_language))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_state_machine.to("main menu")
                elif event.key == pygame.K_UP:
                    speech.speak(self.text)
                elif event.key == pygame.K_DOWN:
                    speech.speak(self.text)
                elif event.key == pygame.K_LEFT and self.index > 0:
                    if self.text[self.index - 1] != "":
                        speech.speak(self.text[self.index - 1])
                    else:
                        speech.speak("blank")
                    self.index -= 1
                elif event.key == pygame.K_RIGHT and self.index < len(self.text) - 1:
                    if self.text[self.index + 1] != "":
                        speech.speak(self.text[self.index + 1])
                    else:
                        speech.speak("blank")
                    self.index += 1
                elif event.key == pygame.K_RETURN:
                    try:
                        self.player_guess = int(self.text)
                        main_state_machine.to("game")
                    except Exception as e:
                        speech.speak(f"{e}")
                        self.text = ""
                elif event.key == pygame.K_BACKSPACE and len(self.text) > 0:
                    self.text = self.text[:-1]
                    speech.speak(self.text)
                elif event.key == pygame.K_HOME:
                    if self.text != "":
                        self.index = 0
                        speech.speak(self.text[self.index])
                elif event.key == pygame.K_END:
                    if self.text != "":
                        self.index = len(self.text)-1
                        speech.speak(self.text[self.index])
                elif event.unicode:
                    self.text += event.unicode

    def exit(self):
        pass


class game_state(state.state):
    def enter(self):
        speech.speak(globals.t.translate(
            "tries", globals.selected_language, tries=5-globals.tries))

    def update(self):
        if globals.tries < 5 and main_state_machine.states['input'].player_guess != globals.guess:
            globals.tries += 1
            if main_state_machine.states['input'].player_guess < globals.guess:
                speech.speak(globals.t.translate(
                    "too low", globals.selected_language))
            elif main_state_machine.states['input'].player_guess > globals.guess:
                speech.speak(globals.t.translate(
                    "too high", globals.selected_language))
            main_state_machine.to("input")
            globals.try_subject.notify(globals.tries)
        else:
            # We have to use int and the number generation is from 1 to 50
            globals.try_subject.notify(-1)

    def exit(self):
        pass


class congratulations_state(state.state):
    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        speech.speak(globals.t.translate("congrats", globals.selected_language, computerGuess=globals.guess,
                     yourGuess=main_state_machine.states['input'].player_guess))
        main_state_machine.to("main menu")


intro = intro_state("main menu")
go = game_over_state("game over")
text_input = input_state("input")
gs = game_state("game")  # The state of the game where computation takes place
congrats_state = congratulations_state("congratulations")
main_state_machine.add_state(intro)
main_state_machine.add_state(go)
main_state_machine.add_state(text_input)
main_state_machine.add_state(gs)
main_state_machine.add_state(congrats_state)
