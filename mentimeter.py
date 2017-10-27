import requests
import re
import threading
import sys

quest_arg = sys.argv[1]
numb_arg = sys.argv[2]
choi_arg = sys.argv[3]

# Takes a question number, a choice number and a times value
# and votes 'times' times for this choice.
# Blocking. Takes about 113s for 100 Votes
def mentimeter_vote_n_times(question_dec, choice_dec, times):
    question_id, choice_id = mentimeter_get_ids(question_dec, choice_dec)
    for i in range(times):
        mentimeter_vote(question_id, choice_id)

# Sames as above just with threading
# Takes about 1s for 100 Votes.
def mentimeter_vote_n_times_async(question_dec, choice_dec, times):
    question_id, choice_id = mentimeter_get_ids(question_dec, choice_dec)
    for i in range(times):
        t = threading.Thread(target = mentimeter_vote, args = (question_id, choice_id))
        t.start()

# Takes the question and choice id and votes for it
def mentimeter_vote(question_id, choice_id):
    url = 'https://govote.at/questions'
    payload = {'code': question_id, 'vote': choice_id}
    headers = {'Host': 'www.govote.at'}
    cookies = dict(ct='0')

    requests.post(url, data=payload, headers=headers, cookies=cookies)

# Takes the decimal question number and the number of the choice to vote for
# and returns the question id, and choice id
def mentimeter_get_ids(question_dec, choice_dec):
    url = 'https://govote.at'
    payload = {'id': question_dec}
    headers = {'Host': 'www.govote.at'}
    r = requests.get(url, data=payload, headers=headers)
    choice_id = re.findall('id=\'choice_([0-9]+)', r.text)[choice_dec-1]
    question_id = re.search('code\' type=\'hidden\' value=\'([a-z0-9]+)\'', r.text).group(1)

    return question_id, choice_id

# Example usage: Vote for question number '726305', choice number '2' a hundred times
#mentimeter_vote_n_times_async(726305, 2, 100)

def take_params(question=quest_arg, number=numb_arg, choice=choi_arg):
    print("{} {} {}".format(question, number, choice))
    question = int(question)
    number = int(number)
    choice = int(choice)
    mentimeter_vote_n_times_async(question, choice, number)

#call
take_params()
