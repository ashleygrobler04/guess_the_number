import translate
import menu
import observers
import observer
import random
import jconfig

tries = 0
try_observable = observers.try_observer()
congrats_observable = observers.win_observer()
try_subject = observer.Subject()
try_subject.addObserver(try_observable)
try_subject.addObserver(congrats_observable)
guess = random.randint(1, 50)
t = translate.Translator()
config = jconfig.JConfig("conf.json")
selected_language = config.get("lang").value
t.load(selected_language)

main_menu = menu.Menu(
    [menu.menu_item(t.translate("Start", selected_language), True, "start", ), menu.menu_item(t.translate("Exit", selected_language), True, "exit"), ])
