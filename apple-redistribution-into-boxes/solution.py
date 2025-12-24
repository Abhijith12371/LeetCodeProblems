class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples=sum(apple)
        box_cap=[]
        count_box=[]
        capacity=sorted(capacity,reverse=True)
        for i in capacity:
            box_cap.append(i)
            if sum(box_cap)>=total_apples:
                count_box.append(len(box_cap))
                box_cap=[]     
        return min(count_box)