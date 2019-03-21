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
            try:
                data = json.load(f)
            except:
                print(path_to_file)
                exit(1)
            try:
                self.name = data['name']
                self.text = data['text']
                self.question = data['question']
                if 'next_page_name' in data.keys():
                    self.next_page_name = data['next_page_name']
                    self.answers = None
                else:
                    self.next_page_name = None
                    self.answers = []
                    for answer in data['answers']:
                        self.answers.append(Answer(answer))

            except:
                print(path_to_file)
                exit(1)



    def get_name(self):
        return self.name

    def next_page(self, usr_ans):
        if self.next_page_name is not None:
            return self.next_page_name

        for a in self.answers:
            if a.equals(usr_ans):
                return a.next_page_name
        return None

    def print_page(self):
        print(self.text)
        print("\n")
        print(self.question)
        if self.answers is None:
            print("\t> Нажмите  на любую клавишу")
        else:
            for answer in self.answers:
                print("\t> " + answer.text)


