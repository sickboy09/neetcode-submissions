class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        all_strings = ""
        for s in strs:
            all_strings += s + "/0"
        for c in all_strings:
            encoded_str += chr(ord(c)+5)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_str = ""
        for c in s:
            decoded_str += chr(ord(c)-5)
        decoded_strs = decoded_str.split("/0")
        return decoded_strs[:len(decoded_strs)-1]
        