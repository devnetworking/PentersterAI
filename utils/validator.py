import re

class Validator:
    @staticmethod
    def is_valid_ip(ip: str) -> bool:
        pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        return bool(pattern.match(ip))

    @staticmethod
    def is_valid_url(url: str) -> bool:
        pattern = re.compile(
            r"^(http://|https://)"
            r"(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(/|/\S+)?$"
        )
        return bool(pattern.match(url))
