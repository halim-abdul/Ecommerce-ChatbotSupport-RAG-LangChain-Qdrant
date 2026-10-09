class Counters:
    def __init__(self): self.values={}
    def inc(self,key:str,n:int=1): self.values[key]=self.values.get(key,0)+n
