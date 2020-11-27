class Solution:
    def decodeString(self, s: str) -> str:
        counts = []
        str_to_build = []

        decoded = ""
        temp_num = ""

        for char in s:
            if char.isdigit():
                temp_num += char
            elif char == "[":

                counts.append(temp_num)
                str_to_build.append(decoded)
                decoded = ""
                temp_num = ""
            elif char == "]":
                count = int(counts.pop())
                build = str_to_build.pop()
                decoded = build + count * decoded

            else:
                decoded += char

        return decoded
