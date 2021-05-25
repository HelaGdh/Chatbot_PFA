# This files contains your custom actions which can be used to run
# custom Python code.

from typing import Any, Text, Dict, List
from .database_connectivity import DataUpdate
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from .IMC import BMI_Calculate
import webbrowser


class ValidateHealthForm(Action):
    def name(self) -> Text:
        return "validate_health_form"

    async def validate_confirm_exercise(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value:
            return {"confirm_exercise": True}
        else:
            return {"exercise": "None", "confirm_exercise": False }

class ActionSubmitResults(Action):
    def name(self) -> Text:
        return "action_submit"
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        confirm_exercise = tracker.get_slot("confirm_exercise")
        DataUpdate(tracker.get_slot("exercise"), tracker.get_slot("stress"), tracker.get_slot("sleep"))
        dispatcher.utter_message("Thanks, your answers have been recorded!")
        return []

"""
class ValidateHealthForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["exercise", "stress", "sleep"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        DataUpdate(tracker.get_slot("exercise"),tracker.get_slot("stress"),tracker.get_slot("sleep"))
        dispatcher.utter_message("Thanks for providing these informations.")
"""

class ValidateIMCForm(Action):
    def name(self) -> Text:
        return "user_imc_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["height", "weight"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]


class ActionIMC(Action):
    def name(self) -> Text:
        return "action_IMC"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        BMI_Calculate(tracker.get_slot("height"),tracker.get_slot("weight"))
        dispatcher.utter_message("Did this help?")
