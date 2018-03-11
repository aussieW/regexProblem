from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

LOGGER = getLogger(__name__)

class regexProblem(MycroftSkill):

    def __init__(self):
        super(regexProblem, self).__init__(name="regexProblem")

    def initialize(self):
        pass
		
    @intent_handler(IntentBuilder('handle_show_world_time').require("ShowWorldTime").require("WorldTime").optionally("city_name").optionally("LocationKeyword"))
    def handle_show_world_time(self, message):
	    # examples: "show the world time for shanghi on the kitchen display"
	    #           "display the world time for shanghi"
		
        LOGGER.info('Intent: handle show world time')
        LOGGER.info('Remainder: ' + str(message.utterance_remainder()))
		
        city = message.data.get("city_name")
        loc_name = message.data.get("LocationKeyword")

        LOGGER.info('City = ' + str(city))        

def create_skill():
    return regexProblem()
