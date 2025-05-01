#!/usr/bin/env python3
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """
        Retrieves a page of the dataset based on page number and page size.

        Args:
            page (int): The current page number. Must be a positive integer.
            page_size (int): The num of items per page. Must be positive.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
                        Returns an empty list if out of range.

        Raises:
            AssertionError: If `page` or `page_size` are not positive integers.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Provides hypermedia pagination details for the requested page.

        Args:
            page (int): The current page number. Must be a positive integer.
            page_size (int): The number of items. Must be positive.

        Returns:
            dict: A dictionary containing the following key-value pairs:
                - "page_size": The length of the returned dataset page.
                - "page": The current page number.
                - "data": The dataset page (return from `get_page`).
                - "next_page": The number of the next page, or None.
                - "prev_page": The number of the previous page, or None.
                - "total_pages": The total number of pages in the dataset.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
