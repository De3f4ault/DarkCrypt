from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import DirectoryTree, Static, Input
from textual.reactive import reactive
from textual.keys import Keys

# Local imports
from .widgets.status_bar import StatusBar
from .commands import encrypt_file, decrypt_file

class NeovimTUI(App):
    """
    Neovim-inspired terminal UI with modal interactions.
    Modes: normal (default), command, insert
    """

    CSS = """
    #workspace {
        layout: horizontal;
    }
    #file-tree {
        width: 30%;
        border-right: solid $accent;
        scrollbar-size: 0 0;
    }
    #main-panel {
        width: 70%;
    }
    #command-line {
        dock: bottom;
        display: none;
    }
    """

    mode = reactive("normal")
    current_file = reactive("")

    def compose(self) -> ComposeResult:
        """Create main UI components"""
        with Horizontal(id="workspace"):
            yield DirectoryTree(".", id="file-tree")
            with Vertical(id="main-panel"):
                yield Static(id="content", classes="panel")
        yield Input(placeholder=":", id="command-line", disabled=True)
        yield StatusBar()

    def on_mount(self) -> None:
        """Initialize the interface"""
        self.switch_mode("normal")

    def switch_mode(self, mode: str) -> None:
        """Handle mode transitions"""
        self.mode = mode
        self.query_one(StatusBar).update_mode(mode)

        if mode == "command":
            command_line = self.query_one("#command-line")
            command_line.display = True
            command_line.disabled = False
            self.set_focus(command_line)
        else:
            command_line = self.query_one("#command-line")
            command_line.display = False
            command_line.disabled = True
            self.set_focus(self.query_one("#file-tree"))

    # Keybindings
    def key_colon(self) -> None:
        """':' enters command mode"""
        if self.mode == "normal":
            self.switch_mode("command")

    def key_escape(self) -> None:
        """ESC returns to normal mode"""
        self.switch_mode("normal")

    def key_e(self) -> None:
        """Encrypt file in normal mode"""
        if self.mode == "normal":
            selected = self.query_one(DirectoryTree).cursor_node
            if selected and selected.is_file:
                self.current_file = str(selected.path)
                self.run_encrypt(self.current_file)

    def key_d(self) -> None:
        """Decrypt file in normal mode"""
        if self.mode == "normal":
            selected = self.query_one(DirectoryTree).cursor_node
            if selected and selected.is_file:
                self.current_file = str(selected.path)
                self.run_decrypt(self.current_file)

    @work
    async def run_encrypt(self, path: str) -> None:
        """Handle file encryption"""
        password = await self.get_password("Encryption password:")
        if password:
            result = encrypt_file(path, password)
            self.query_one(StatusBar).notify(result)

    @work
    async def run_decrypt(self, path: str) -> None:
        """Handle file decryption"""
        password = await self.get_password("Decryption password:")
        if password:
            result = decrypt_file(path, password)
            self.query_one(StatusBar).notify(result)

    async def get_password(self, prompt: str) -> str:
        """Password input dialog"""
        self.switch_mode("insert")
        password = await self.get_input(prompt, password=True)
        self.switch_mode("normal")
        return password

    @on(Input.Submitted, "#command-line")
    def handle_command(self, event: Input.Submitted) -> None:
        """Execute command-line commands"""
        cmd = event.value.strip()
        if cmd == "q":
            self.exit()
        elif cmd.startswith("e "):
            self.run_encrypt(cmd[2:])
        elif cmd.startswith("d "):
            self.run_decrypt(cmd[2:])
        self.switch_mode("normal")

if __name__ == "__main__":
    NeovimTUI().run()
