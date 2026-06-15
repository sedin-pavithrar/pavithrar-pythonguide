from collections import deque

class Browser:
    def __init__(self):
        self.back_stack = []
        self.frwd_stack = []
        self.history = deque()

        self.current = None
    
    def visit(self,url):
        if self.current is not None:
            self.back_stack.append(self.current)

        self.current = url
        self.history.append(self.current)
        self.frwd_stack.clear()
        print(f" \n Visited url: {url}")

    def back(self):
        if not self.back_stack:
            print("\n Nothing to go back!")
            return
        
        self.frwd_stack.append(self.current)
        self.current = self.back_stack.pop()
        self.display()

    def forward(self):
        if not self.frwd_stack:
            print("\n Nothing to go forward")
            return 
        self.back_stack.append(self.current)
        self.current = self.frwd_stack.pop()
        self.display()

    def show_history(self):
        print("\n History logs:")

        if not self.history:
            print("\n No History Found")
            return 
        for url in self.history:
            print(url)

    def search_history(self,keyword):
        matches = []
        for url in self.history:
            if keyword.lower() in url.lower():
                matches.append(url)
        return matches
    
    def display(self):
        print(f" \n Current Page : {self.current}")

    
def main():

    browser = Browser()

    browser.visit(" google.com")
    browser.visit(" youtube.com")
    browser.visit(" github.com")

    browser.back()
    browser.back()

    browser.forward()

    browser.visit(" linkedin.com")

    browser.forward()

    browser.show_history()

    print("\n Search Results:")
    print(browser.search_history("git"))


if __name__ == "__main__":
    main()
        










    
    
        

        



    


