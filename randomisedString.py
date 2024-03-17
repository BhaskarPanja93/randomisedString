__version__ = "1.2.0"


class Generator:
    def __init__(self):
        """
        Initialise the Generator and use the public functions to generate a randomised string.
        """
        from random import choice as __choice, randrange as __randrange
        self.__choice = __choice
        self.__randrange = __randrange
        self.LOWER_CASE_ASCIIS = list(range(97, 122 + 1))
        self.UPPER_CASE_ASCIIS = list(range(65, 90 + 1))
        self.NUMBER_ASCIIS = list(range(48, 57 + 1))
        self.ALPHANUMERIC_ASCIIS = self.LOWER_CASE_ASCIIS + self.UPPER_CASE_ASCIIS + self.NUMBER_ASCIIS


    def AlphaNumeric(self, _min=10, _max=20)->str:
        """
        Generates a string with numbers and alphabets(a-z, A-Z, 0-9)
        :param _min: Minimum possible length of generated string
        :param _max: Maximum possible length of generated string
        :return: A random string of the specified size
        """
        _minLength = min(_min, _max)
        _maxLength = max(_min, _max)
        if _maxLength == _minLength:
            _maxLength+=1
        string = ''
        for _ in range(self.__randrange(_minLength, _maxLength)):
            string += chr(self.__choice(self.ALPHANUMERIC_ASCIIS))
        return string


    def OnlyNumeric(self, _min=10, _max=20)->str:
        """
        Generates a string with only numbers(0-9). Convert the string to int if needed
        :param _min: Minimum possible length of generated string
        :param _max: Maximum possible length of generated string
        :return: A random string of the specified size
        """
        _minLength = min(_min, _max)
        _maxLength = max(_min, _max)
        if _maxLength == _minLength:
            _maxLength += 1
        string = ''
        for _ in range(self.__randrange(_minLength, _maxLength)):
            string += chr(self.__choice(self.LOWER_CASE_ASCIIS+self.UPPER_CASE_ASCIIS))
        return string


    def OnlyAlpha(self, _min=10, _max=20)->str:
        """
        Generates a string with only Alphabets(a-z, A-Z)
        :param _min: Minimum possible length of generated string
        :param _max: Maximum possible length of generated string
        :return: A random string of the specified size
        """
        _minLength = min(_min, _max)
        _maxLength = max(_min, _max)
        if _maxLength == _minLength:
            _maxLength += 1
        string = ''
        for _ in range(self.__randrange(_minLength, _maxLength)):
            string += chr(self.__choice(self.LOWER_CASE_ASCIIS+self.UPPER_CASE_ASCIIS))
        return string

