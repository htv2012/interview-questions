NEITHER = "Neither"
IPV4 = "IPv4"
IPV6 = "IPv6"


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if ":" in queryIP:
            return self.validIPv6(queryIP)
        elif "." in queryIP:
            return self.validIPv4(queryIP)
        return NEITHER

    def validIPv4(self, queryIP: str) -> str:
        def valid(num: str):
            try:
                if (len(num) > 1 and num[0] == "0") or (int(num) > 255):
                    return False
            except ValueError:
                return False
            return True

        nums = queryIP.split(".")
        if len(nums) == 4 and all(valid(num) for num in nums):
            return IPV4
        return NEITHER

    def validIPv6(self, queryIP: str) -> str:
        def valid(num: str):
            return 0 < len(num) <= 4 and set(num).issubset(
                set("0123456789abcdefABCDEF")
            )

        nums = queryIP.split(":")
        if len(nums) == 8 and all(valid(num) for num in nums):
            return IPV6
        return NEITHER
