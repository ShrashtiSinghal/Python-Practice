class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people= len(groupSizes)
        set_list=set(groupSizes)
        set_list=list(set_list)
        idlist=[]
        newList=[]
        idList1=[]
        lettercount=0

        for x in set_list:
            y= groupSizes.count(x)
            cal=y//x
            
            if (x in idlist):
                break
            
            else:
                for y in range (0,people):

                    if lettercount!=cal:

                        if groupSizes[y]==x:
                            newList.append(y)
                        else:
                            continue


                        if len(newList)==int(x):
                            lettercount=lettercount+1
                            idList1=newList.copy()
                            idlist.append(idList1)
                            newList.clear()
                
                    lettercount=0
                        

        return idlist
        