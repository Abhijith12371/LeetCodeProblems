class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        l=[]
        out=[]
        valid_chars="abcdefghijklmnopqrstuvwxyz0123456789_"
        items=list(zip(code,businessLine,isActive))
        for ch,b,active in items:
            if not ch:
                continue
            isvalied=all(letter.lower() in valid_chars for letter in ch)
            if (isvalied and b!="invalid") and active:
                l.append((ch,b))
        finalItems=sorted(l,key=lambda x:(x[1],x[0]))
        for i in finalItems:
            out.append(i[0])
        return out
            