class CounterManager:
    insCount = 0
    def __init__(self) :
        CounterManager.insCount += 1
    def staticPrintCount() :
        print("Instance Count:me", CounterManager.insCount)
    SPrintCount = staticmethod(staticPrintCount)
    def classPrintCount(cls) :
        print("Instance Count: cl",CounterManager.insCount)
    CPrintCount = classmethod(classPrintCount)
A,b,c= CounterManager(), CounterManager(), CounterManager()
CounterManager.SPrintCount()
b.SPrintCount()
CounterManager.CPrintCount()
c.SPrintCount()
