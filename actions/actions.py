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
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from typing import Any, Text, Dict, List
import torch
from rasa_sdk.events import UserUtteranceReverted


class Action_greet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print('action name is ',self.name)
        message = "Hi, Thanks for trying our website. How can i help you"
        dispatcher.utter_message(text=message)
        return []
   

class ActionAskSubjects(Action):
    def name(self) -> Text:
        return "action_ask_subjects"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "We offer study materials for various subjects including Math, Science, Social Studies, English, Kannada, and Sanskrit. You can find resources for these subjects on our website."
        dispatcher.utter_message(text=message)

        return []


class ActionAccessStudyMaterials(Action):
    def name(self) -> Text:
        return "action_access_study_materials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        message = "Yes, all the study materials on our website are available for free. Simply browse the subject of your choice and access the resources instantly."
        dispatcher.utter_message(text=message)

        return []

class ActionAccessVideoLectures(Action):
    def name(self) -> Text:
        return "action_access_video_lectures"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        message = "To access video lectures, navigate to the respective subject's page, and you'll find a section with links to video lectures relevant to that subject."
        dispatcher.utter_message(text=message)

        return []

class ActionDownloadMaterials(Action):
    def name(self) -> Text:
        return "action_download_materials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        message = "currently we don't have download option.we will work on it shortly"
        dispatcher.utter_message(text=message)

        return []

class ActionOfferSamplePapers(Action):
    def name(self) -> Text:
        return "action_offer_sample_papers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        message = "Absolutely! We provide a collection of sample papers for your exams. You can find them in the 'Sample Papers' section under each subject."
        dispatcher.utter_message(text=message)

        return []

class ActionSuitableForGradeLevels(Action):
    def name(self) -> Text:
        return "action_suitable_for_grade_levels"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        message = "You have materials for 10th std. You can filter the content based on subjects to find relevant resources."
        dispatcher.utter_message(text=message)

        return []

class ActionUpdateFrequency(Action):
    def name(self) -> Text:
        return "action_update_frequency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        message = "We regularly update our study materials to ensure they align with the latest curriculum and educational standards."
        dispatcher.utter_message(text=message)

        return []

class ActionOfferQuizzesTests(Action):
    def name(self) -> Text:
        return "action_offer_quizzes_tests"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        message = "Yes, we have quizzes and practice tests available for each subject to help you assess your knowledge and improve your understanding."
        dispatcher.utter_message(text=message)

        return []

class ActionRegistrationRequirement(Action):
    def name(self) -> Text:
        return "action_registration_requirement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        message = "No, registration is not mandatory to access the study materials. However, creating an account allows you to track your progress and bookmark your favorite resources."
        dispatcher.utter_message(text=message)

        return []

class ActionContactCustomerSupport(Action):
    def name(self) -> Text:
        return "action_contact_customer_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        message = "You can reach out to our customer support team through ' acadevo123@gmail.com '. We are here to assist you with any queries or concerns you may have."
        dispatcher.utter_message(text=message)

        return []

class ActionProvideTips(Action):
    def name(self) -> Text:
        return "action_provide_tips"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        message = "Sure, here are some tips to handle exam pressure:\n1. Create a study schedule.\n2. Take short breaks to avoid burnout.\n3. Practice relaxation techniques like deep breathing.\n4. Stay physically active.\n5. Seek help when needed.\nRemember, you've got this and you are the best!"
        dispatcher.utter_message(text=message)
        return []

class ActionManageTime(Action):
    def name(self) -> Text:
        return "action_manage_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        message = "Effective time management is key. Try setting study goals, prioritizing tasks, and using techniques like the Pomodoro Technique.\n1.Get a to-do list and a timer\n2.Set your timer for 25 minutes and focus on your task.\n3.When your session ends, mark off one pomodoro and record what you completed.\n4.Then enjoy a five-minute break.\n5.After four pomodoros, take a longer, more restorative 15-30 minute break."
        dispatcher.utter_message(text=message)
        return []
    
class ActionDealWithStress(Action):
    def name(self) -> Text:
        return "action_deal_with_stress"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        message = "Coping with stress involves self-care. Ensure you get enough sleep, eat well, and practice mindfulness."
        dispatcher.utter_message(text=message)
        return []

class ActionDefinePeerPressure(Action):
    def name(self) -> Text:
        return "action_define_peer_pressure"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        message = "Peer pressure refers to the influence exerted by peers or friends to conform to their behaviors, attitudes, or decisions. It can lead individuals to do things they might not want to do. It's important to know how to handle peer pressure positively."
        dispatcher.utter_message(text=message)
        return []

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def generate_gpt2_response(self, input_text, conversation_history):
        model_name = "gpt2"
        model = GPT2LMHeadModel.from_pretrained(model_name)
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)

        # Combine conversation history and input text
        full_input_text = ' '.join(conversation_history) + " " + input_text

        input_ids = tokenizer.encode(full_input_text, add_special_tokens=True, return_tensors="pt")
        attention_mask = torch.ones_like(input_ids)

        # Generate text using max_length to control response length
        output = model.generate(input_ids, attention_mask=attention_mask, max_length=100, no_repeat_ngram_size=2)

        # Decode the generated output
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        # Extract the first sentence
        first_sentence = generated_text.split('.')[0].strip()

        return first_sentence
        

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get('text')
        conversation_history = [event['text'] for event in tracker.events if event['event'] == 'user']

        print("User:", user_message)
        generated_text = self.generate_gpt2_response(user_message, conversation_history)
        print("Bot (Generated):", generated_text)
        dispatcher.utter_message(text=generated_text)

        return [UserUtteranceReverted()]
