from textual.widget import Widget
from textual.reactive import reactive

class StatusBar(Widget):
    mode = reactive("normal")
    message = reactive("")

    def render(self) -> str:
        return f"[bold]{self.mode.upper()}[/] | {self.message}"

    def update_mode(self, mode: str) -> None:
        self.mode = mode
        self.refresh()

    def notify(self, message: str) -> None:
        self.message = message
        self.refresh()
