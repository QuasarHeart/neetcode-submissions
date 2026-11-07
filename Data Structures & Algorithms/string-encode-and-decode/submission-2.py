class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output = output+string+"。"
        return output


    def decode(self, s: str) -> List[str]:
        output = s.split("。")
        return output[:-1]
