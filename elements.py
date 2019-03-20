import json


class Answer(object):
    def __init__(self, desc):
        self.text = desc['text']
        self.next_page_name = desc['next_page_name']

    def equals(self, answer):
        return self.text == answer

class Page(object):
    def __init__(self, path_to_file):
        with open(path_to_file) as f:
            data = json.load(f)
            self.name = data['name']
            self.text = data['text']
            self.question = data['question']
            self.answers = []
            for answer in data['answers']:
                self.answers.append(Answer(answer))


    def get_name(self):
        return self.name

    def next_page(self, usr_ans):
        for a in self.answers:
            if a.equals(usr_ans):
                return a.next_page_name
        return None

    def print_page(self):
        print(self.text)
        print("\n")
        print(self.question)
        for answer in self.answers:
            print("\t> " + answer.text)


