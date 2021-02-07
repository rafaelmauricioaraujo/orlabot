# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient


class getProjects(Action):

    def name(self) -> Text:
        return "action_get_projects"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        client = MongoClient("mongodb+srv://rasa:Y3XMzsBIO5i1N9Re@cluster0.tpni9.mongodb.net/orla?retryWrites=true&w=majority")
        db = client.orla
        cursor = db.project.find({})
        results = [doc for doc in cursor]
        message = ''
        for result in results:
            print('result.name: ', result['name'])
            message += result['name'] + ', '

        dispatcher.utter_message(text=message)
        client.close
        return []
