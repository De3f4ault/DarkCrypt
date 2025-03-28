import os
import logging

def secure_delete(file_path: str, passes: int = 3) -> None:
    try:
        with open(file_path, "ba+") as f:
            length = f.tell()
            for _ in range(passes):
                f.seek(0)
                f.write(os.urandom(length))
        os.remove(file_path)
    except Exception as e:
        logging.error(f"Secure deletion failed: {e}")
        raise
