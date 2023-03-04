import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")