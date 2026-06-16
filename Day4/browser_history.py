# Two stacks simulate browser back/forward navigation. 
# visit(url) pushes to back_stack and clears 
# fwd_stack. back() pops from back to forward. 
# forward() pops from forward to back. A deque 
# maintains a permanent chronological log. This is the exact data structure Chrome uses for browser history.
# Problem
# Two stacks + deque history log. visit() pushes to back. back() pops to forward. forward() reverses.
# Constraints
# • visit() clears forward stack
# • back() -> "Nothing to go back to" if empty
# • history_log is append-only, never cleared
# Bonus: Add search_history(keyword) returning all matching URLs.from collections import deque

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
        self.display("Backward")

    def forward(self):
        if not self.frwd_stack:
            print("\n Nothing to go forward")
            return 
        self.back_stack.append(self.current)
        self.current = self.frwd_stack.pop()
        self.display("Forward")

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
    
    def display(self,action = "Current Page"):
        print(f" \n {action} -> {self.current}")

    
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
        










    
    
        

        



    


