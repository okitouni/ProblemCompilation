# # 1472. Design Browser History

# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
import unittest

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.future = []
        self.homepage= homepage
        self.size = 0
        

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        while self.history and steps:
            self.future.append(self.history.pop())
            steps -= 1
        if not self.history: 
            self.history = [self.homepage]
            self.future.pop()
        return self.history[-1]

        
    def forward(self, steps: int) -> str:
        while self.future and steps:
            self.history.append(self.future.pop())
            steps -= 1
        return self.history[-1]
    
class Test(unittest.TestCase):
    def test_browserHistory(self):
        browserHistory = BrowserHistory("leetcode.com")
        browserHistory.visit("google.com")       # You are in "leetcode.com". Visit "google.com"
        browserHistory.visit("facebook.com")     # You are in "google.com". Visit "facebook.com"
        browserHistory.visit("youtube.com")      # You are in "facebook.com". Visit "youtube.com"
        self.assertEqual(browserHistory.back(1), "facebook.com")                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
        self.assertEqual(browserHistory.back(1), "google.com")                     # You are in "facebook.com", move back to "google.com" return "google.com"
        self.assertEqual(browserHistory.forward(1), "facebook.com")                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
        browserHistory.visit("linkedin.com")     # You are in "facebook.com". Visit "linkedin.com"
        self.assertEqual(browserHistory.forward(2), "linkedin.com")                # You are in "facebook.com", you cannot move forward any steps.
        self.assertEqual(browserHistory.back(2), "google.com")                     # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
        self.assertEqual(browserHistory.back(7), "leetcode.com")                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

if __name__ == "__main__":
    unittest.main()