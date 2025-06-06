class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary enteries must have Title and content")
        self._title = title
        self._content = contents
        self.diary_entry = []
        # Parameters:
        #   title: string
        #   contents: string
        

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        diary_entry = f"{self._title}: {self._content}" 
        return diary_entry

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        words = self.format().split()
        return len(words)
            

    def reading_time(self, wpm):
        time = len(self._content) / wpm
        print(time)
        return time
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass
