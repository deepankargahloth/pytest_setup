"""
add_new method add a new_item to the starting_list

get_most_often method create a list of most unique items and then iterate through the items 
in the list and return the highest item whcih is in highest number

functionality: 1. Find the unique

also, return the highest item if there is only one, otherwise return no clear winner

"""

from lib.most_often import MostOften

def test_find_the_most__number_item():
    new_list = MostOften(["1", "2", "3", "4", "1"])
    assert new_list.get_most_often() == "1"


def test_if_all_items_equal_in_number():
    new_list = MostOften(["1", "2", "3", "4"])
    assert new_list.get_most_often() == "no clear winner"

def test_add_new_item():
    new_list = MostOften(["1", "2", "3", "4", "1"])
    new_list.add_new("1")
    assert new_list.get_most_often() == "1"

def test_add_new_item_twice():
    new_list = MostOften(["1", "2", "3", "4", "1"])
    new_list.add_new("2")
    new_list.add_new("2")
    assert new_list.get_most_often() == "2"

def test_add_new_item_twice_extension():
    new_list = MostOften(["1", "2", "3", "4", "1"])
    new_list.add_new("2")
    new_list.add_new("2")
    new_list.add_new("1")
    assert new_list.get_most_often() == "no clear winner"