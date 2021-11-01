class Page:
    def __init__(self, page: str, prev):
        self.page = page
        self.prev = prev
        self.next = None


class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Page(page=homepage, prev=None)

    def visit(self, url: str) -> None:
        self.curr.next = Page(page=url, prev=self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.page

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.page

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
