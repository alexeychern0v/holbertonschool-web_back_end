#!/usr/bin/env python3
"""pagination"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """ returns a tuple of size two containing a
    start index and an end index """
    start_index = ((page - 1) * page_size)
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ find the correct indexes to paginate the dataset
        and return the appropriate page of the dataset
        If the input arguments are out of range for the dataset
        an empty list should be returned """
        assert isinstance(page, int) and page > 0, (
            "page should be an int greater than 0")
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size should be an int greater than 0")
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index < len(dataset):
            return dataset[start_index:end_index]
        else:
            return []
