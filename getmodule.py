import requests
import json

# I only get 440 because after investigating the matter, it seems there are only this many (at the time of writing)


def getfacts():
    facts = []
    r = requests.get(
        url='https://cat-fact.herokuapp.com/facts/random?animal=cat&amount=440')
    q = r.json()
    for element in q:
        if not any(fact['_id'] == element['_id'] for fact in facts):
            facts.append({"_id": element['_id'], "text": element['text'], })

    return facts
