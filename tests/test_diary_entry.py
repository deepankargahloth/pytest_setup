import pytest
from lib.diary_entry import DiaryEntry

"""
return the formatted string
"""
def test_return_the_formatted_string():
    diary_entry = DiaryEntry("My Title", "who are you?")
    result = diary_entry.format() 
    assert result == "My Title: who are you?"

"""
return the number of words in the diary entry
"""

def test_return_the_number_words_in_the_content():
    diary_entry = DiaryEntry("My Title", "who are you i dont know you?")
    result = diary_entry.count_words()
    assert result == 9

"""
Given an emptry title and content, this should raise error
"""
def test_empty_title_and_content_return_error():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "")
    assert str(err.value) == "Diary enteries must have Title and content"


"""
WPM: User can read words per  minutes e.g, 1 means, user can read one word per minute
return an estimate of the time by user to take in reading the content, 
e.g if the content is "one two three, four, five, six" and WPM : 2, this should return 3 
"""

def test_return_estimated_time_for_reading():
    # need length of the content and divide that with wpm
    diary_entry = DiaryEntry("My Title", "who are you i dont know?")
    result = diary_entry.reading_time(5)
    assert result == 2

"""
Parameters WPM, reading minutes, return chunck of content user can read in the given time and speed

for e.g WPM = 2, reading_time = 2, content = "One two three four five six seven eight", function should return
"One two three four"-----First time
if call again should return: "five six seven eight"
if call again should return "One two three four" means start from the beginining.
"""

def test_return_content_part_based_on_WPM_and_minutes():
        diary_entry = DiaryEntry("My Title", "One two three four five six seven eight?")
        result = diary_entry.reading_chunk(2, 2)
        assert result == "One two three four"


def test_return_content_part_based_on_WPM_and_minutes_2_3():
        diary_entry = DiaryEntry("My Title", "One two three four five six seven eight?")
        result = diary_entry.reading_chunk(2, 3)
        assert result == "One two three four five six"


def test_return_content_part_based_on_WPM_and_minutes_called_multiple_times():
        diary_entry = DiaryEntry("My Title", "One two three four five six seven")
        assert diary_entry.reading_chunk(2, 1) == "One two"
        assert diary_entry.reading_chunk(2, 1) == "three four"
        assert diary_entry.reading_chunk(2, 1) == "five six"
        assert diary_entry.reading_chunk(1, 1) == "seven"
        assert diary_entry.reading_chunk(2, 1) == "One two"
"""
If called more then two time, 
"""