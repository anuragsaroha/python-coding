class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i == '+':
                record.append(record[-1] + record[-2])
            elif i == "D":
                record.append(record[-1] * 2)
            elif i == "C":
                record.pop()
            else:
                record.append(int(i))
        if record:
            result = sum(record)
        else:
            result = 0
        return result
