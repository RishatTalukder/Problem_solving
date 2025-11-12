class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        import re
        n = len(code)
        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        line_order = {name: idx for idx, name in enumerate(valid_lines)}
        valid_coupons = []

        for i in range(n):
            if (isActive[i] and
                businessLine[i] in line_order and
                code[i] and
                re.match(r'^[a-zA-Z0-9_]+$', code[i])):
                valid_coupons.append((line_order[businessLine[i]], code[i]))

        valid_coupons.sort()
        return [c[1] for c in valid_coupons]
