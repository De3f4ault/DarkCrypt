import os

def secure_delete(file_path: str, passes: int = 3) -> None:
    """Overwrite file with random data before deletion."""
    try:
        file_size = os.path.getsize(file_path)
        with open(file_path, "ba+") as f:
            for _ in range(passes):
                f.seek(0)
                f.write(os.urandom(file_size))
            f.flush()
            os.fsync(f.fileno())
        os.remove(file_path)
    except Exception as e:
        raise RuntimeError(f"Secure deletion failed: {e}") from e
