#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Provides deletion-resilient hypermedia pagination details.

        Args:
            index (int): The current start index. Must be within a valid range.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing the following keys:
            - "index": The current start index of the return page.
            - "next_index": The next index to query with.
            - "page_size": The current page size.
            - "data": The actual page of the dataset.

        Raises:
            AssertionError: If `index` is not within a valid range.
        """
        assert type(index) is int and 0 <= index < len(self.indexed_dataset())
        assert type(page_size) is int and page_size > 0

        indexed_data = self.indexed_dataset()
        data = []
        current = index
        count = 0

        while count < page_size and current < len(indexed_data):
            if current in indexed_data:
                data.append(indexed_data[current])
                count += 1
            current += 1

        next_index = current if current < len(indexed_data) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
