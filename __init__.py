from mycroft import MycroftSkill, intent_file_handler


class Aimsir(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('aimsir.intent')
    def handle_aimsir(self, message):
        self.speak_dialog('aimsir')


def create_skill():
    return Aimsir()

