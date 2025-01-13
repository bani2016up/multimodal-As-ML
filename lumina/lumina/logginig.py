

class Logger:

    def __init__(self, log_file: str) -> None:
        self.log_file = log_file

    def log(self, message: str) -> None:
        with open(self.log_file, "a") as f:
            f.write(f"{message}\n")
