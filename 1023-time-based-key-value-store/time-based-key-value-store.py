class TimeMap:

    def __init__(self):
        self.hashmap={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key]=[]
        self.hashmap[key].append([value,timestamp]) 

    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.hashmap.get(key,[])
        l,r=0,len(values)-1
        while l<=r:
            mid=(l+r)//2
            ts,val=values[mid][1],values[mid][0]
            if ts==timestamp: return val
            elif ts<timestamp:
                res=val
                l=mid+1
            else: r=mid-1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)