import glob
import elements


class Story(object):
    def __init__(self, path_to_dir):
        self.pages = dict()

        files = glob.glob(path_to_dir + "**.json")
        for file in files:
            page = elements.Page(file)
            self.pages[page.get_name()] = page

        self.curr_page = self.pages["start"]

    def start(self):
        while True:
            self.curr_page.print_page()
            answer = self.get_answer()
            next_page_name = self.curr_page.next_page(answer)

            while next_page_name is None:
                answer = self.get_answer()
                next_page_name = self.curr_page.next_page(answer)

            self.curr_page = self.pages[next_page_name]

    def get_answer(self, ):
        print("----")
        return input()