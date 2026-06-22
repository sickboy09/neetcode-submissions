class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        passengers = {x: int(x[11:13]) for x in details}
        for key, value in passengers.items():
            if value > 60:
                count += 1
        return count

