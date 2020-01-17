import numpy as np
import pandas as pd
import urllib.request as request
import time

from pandas import DataFrame


class SimpleWordCountExample:
    """
    source file: https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt
    save output file into output folder
    """

    def __init__(self):
        self.source_url = 'https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt'
        self.get_current_time_func = lambda: int(round(time.time() * 1000))

    def load_source_file(self) -> DataFrame:
        pass

    def do_word_count(self, df: DataFrame) -> DataFrame:
        pass

    def persist_result(self, df: DataFrame):
        pass

    def run(self):
        raw_df = self.load_source_file()
        wordcount_result_df = self.do_word_count(raw_df)
        self.persist_result(wordcount_result_df)


if __name__ == "__main__":
    runner = SimpleWordCountExample()
    runner.run()
