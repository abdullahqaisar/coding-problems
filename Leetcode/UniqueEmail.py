class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for e in emails:
            i, email = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    email += e[i]
                i += 1
            while e[i] not in "@":
                i += 1
            email += e[i: -1]
            res.add(email)

        return len(res)
