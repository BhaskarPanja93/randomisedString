__version__ = "1.4.0"
__packagename__ = "randomisedstring"


def updatePackage():
    from time import sleep
    from json import loads
    import http.client
    print(f"Checking updates for Package {__packagename__}")
    try:
        host = "pypi.org"
        conn = http.client.HTTPSConnection(host, 443)
        conn.request("GET", f"/pypi/{__packagename__}/json")
        data = loads(conn.getresponse().read())
        latest = data['info']['version']
        if latest != __version__:
            try:
                import subprocess
                from pip._internal.utils.entrypoints import (
                    get_best_invocation_for_this_pip,
                    get_best_invocation_for_this_python,
                )
                from pip._internal.utils.compat import WINDOWS
                if WINDOWS:
                    pip_cmd = f"{get_best_invocation_for_this_python()} -m pip"
                else:
                    pip_cmd = get_best_invocation_for_this_pip()
                subprocess.run(f"{pip_cmd} install {__packagename__} --upgrade")
                print(f"\nUpdated package {__packagename__} v{__version__} to v{latest}\nPlease restart the program for changes to take effect")
                sleep(3)
            except:
                print(f"\nFailed to update package {__packagename__} v{__version__} (Latest: v{latest})\nPlease consider using pip install {__packagename__} --upgrade")
                sleep(3)
        else:
            print(f"Package {__packagename__} already the latest version")
    except:
        print(f"Ignoring version check for {__packagename__} (Failed)")


class Imports:
    from secrets import choice, randbelow


class RandomisedString:
    def __init__(self):
        """
        Initialise the Generator and use the public functions to generate a randomised string.
        """
        self.LOWER_CASE_ASCIIS = list(range(97, 122 + 1))
        self.UPPER_CASE_ASCIIS = list(range(65, 90 + 1))
        self.NUMBER_ASCIIS = list(range(48, 57 + 1))
        self.ALPHANUMERIC_ASCIIS = self.LOWER_CASE_ASCIIS + self.UPPER_CASE_ASCIIS + self.NUMBER_ASCIIS

    def AlphaNumeric(self, _min=10, _max=20) -> str:
        """
        Generates a string with numbers and alphabets(a-z, A-Z, 0-9)
        :param _min: Minimum possible length of generated string
        :param _max: Maximum possible length of generated string
        :return: A random string of the specified size
        """
        _minLength = min(_min, _max)
        _maxLength = max(_min, _max)
        if _maxLength == _minLength:
            _maxLength += 1
        length = Imports.randbelow(_maxLength - _minLength) + _minLength
        string = ''.join(chr(Imports.choice(self.ALPHANUMERIC_ASCIIS)) for _ in range(length))
        return string

    def OnlyNumeric(self, _min=10, _max=20) -> str:
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
        length = Imports.randbelow(_maxLength - _minLength) + _minLength
        string = ''.join(chr(Imports.choice(self.NUMBER_ASCIIS)) for _ in range(length))
        return string

    def OnlyAlpha(self, _min=10, _max=20) -> str:
        """
        Generates a string with only Alphabets(a-z, A-Z)
        :param _min: Minimum possible length of generated string
        :param _max: Maximum possible length of generated string
        :return: A random string of the specified size
        """
        _minLength = min(_min, _max)
        _maxLength = max(_min, _max)
        if _maxLength == _minLength: _maxLength += 1
        length = Imports.randbelow(_maxLength - _minLength) + _minLength
        string = ''.join(chr(Imports.choice(self.LOWER_CASE_ASCIIS + self.UPPER_CASE_ASCIIS)) for _ in range(length))
        return string
