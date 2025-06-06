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

def test_return_estimate_time_for_reading():
    # need length of the content and divide that with wpm
    diary_entry = DiaryEntry("My Title", "who are you i dont know?")
    result = diary_entry.reading_time(2)
    assert result == 3