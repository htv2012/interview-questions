#!/usr/bin/env python3
import pytest

from solution import RLEIterator


@pytest.mark.parametrize(
    "actions, args_list, expected_list",
    [
        pytest.param(
            ["RLEIterator", "next", "next", "next", "next"],
            [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]],
            [None, 8, 8, 5, -1],
            id="example 1",
        ),
        pytest.param(
            [
                "RLEIterator",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
                "next",
            ],
            [
                [
                    [
                        923381016,
                        843,
                        898173122,
                        924,
                        540599925,
                        391,
                        705283400,
                        275,
                        811628709,
                        850,
                        895038968,
                        590,
                        949764874,
                        580,
                        450563107,
                        660,
                        996257840,
                        917,
                        793325084,
                        82,
                    ]
                ],
                [612783106],
                [486444202],
                [630147341],
                [845077576],
                [243035623],
                [731489221],
                [117134294],
                [220460537],
                [794582972],
                [332536150],
                [815913097],
                [100607521],
                [146358489],
                [697670641],
                [45234068],
                [573866037],
                [519323635],
                [27431940],
                [16279485],
                [203970],
            ],
        ),
    ],
)
def test_solution(actions, args_list, expected_list):
    obj = None
    for action, args, expected in zip(actions, args_list, expected_list):
        if action == "RLEIterator":
            obj = RLEIterator(*args)
            assert expected is None
            continue

        method = getattr(obj, action)
        actual = method(*args)
        assert actual == expected, f"{action=}"
