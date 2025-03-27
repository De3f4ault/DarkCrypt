from textual import on
from textual.keys import Keys

class NormalMode:
    BINDINGS = [
        ("e", "encrypt", "Encrypt file"),
        ("d", "decrypt", "Decrypt file"),
        (Keys.Escape, "normal_mode", "Normal mode"),
    ]
