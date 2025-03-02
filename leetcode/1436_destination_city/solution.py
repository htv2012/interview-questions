#!/usr/bin/env python3
# https://leetcode.com/problems/destination-city/?envType=daily-question&envId=2024-03-13
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src, dest = map(set, zip(*paths))
        dest -= src
        dest_city = dest.pop()
        return dest_city
