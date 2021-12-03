import logging


class Logger:
    def __init__(self):
        logging.basicConfig(
            filename="app.log",
            filemode="w",
            format="%(name)s - %(levelname)s - %(message)s",
            level=30,
        )

    def warning(self, message: str):
        logging.warning(message)

    def info(self, message: str):
        logging.info(message)


log = Logger()
