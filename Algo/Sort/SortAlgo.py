import  operator
class Sort:
    def bubbleSort(self,iter_ob,compare=operator.gt):
        """
        working good in int,char,string,float
        :param iter_ob: any iter object
        :return: list of object
        """
        lenth=len(iter_ob)
        for out_index in range(lenth):
            for inner_index in range(lenth-out_index-1):
                if compare(iter_ob[inner_index],iter_ob[inner_index+1]):
                #if iter_ob[inner_index]>iter_ob[inner_index+1]:
                    iter_ob[inner_index],iter_ob[inner_index+1]=iter_ob[inner_index+1],iter_ob[inner_index]
        #print("Bublle:-"iter_ob)
        return iter_ob

    def selctionSort(self,iter_ob,compare=operator.gt):
        """
        selection sort with genric implematin
        :param iter_ob: iter obj
        :return: iter obj
        """
        lenth=len(iter_ob)
        for i in range(lenth-1):
            swap_index=i
            for j in range(i,lenth):
                if compare(iter_ob[swap_index],iter_ob[j]):
                #if iter_ob[swap_index]>iter_ob[j]:
                    swap_index=j
            iter_ob[i],iter_ob[swap_index]=iter_ob[swap_index],iter_ob[i]
        #print("selelction:-",iter_ob)
        return iter_ob

    def insertionSort(self,iter_obj):
        lenth=len(iter_obj)
        for elemnt_index in range(1,lenth):
            key_elmement=iter_obj[elemnt_index]
            swap_index=elemnt_index-1
            while swap_index>=0 and key_elmement<iter_obj[swap_index]:
                iter_obj[swap_index+1]=iter_obj[swap_index]
                swap_index-=1
            iter_obj[swap_index+1]=key_elmement
        #print(iter_obj)
        return iter_obj

    def mergeSort(self,iter_ob,compare=operator.lt):
        def merge(left, right, compare):
            result = []
            left_index, right_index = 0, 0
            while left_index < len(left) and right_index < len(right):
                if compare(left[left_index], right[right_index]):
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1
            result += left[left_index:]
            result += right[right_index:]
            return result
        if len(iter_ob)<2:
            return iter_ob
        else:
            middle=len(iter_ob)//2
            left_arr=iter_ob[:middle]
            right_arr=iter_ob[middle:]
            self.mergeSort(left_arr,compare)
            self.mergeSort(right_arr,compare)
            return merge(left_arr,right_arr,compare)

    def partition(self,iter_obj, strat, end):
        pivot = iter_obj[strat]
        low = strat + 1
        high = end
        while True:
            while low <= high and iter_obj[high] >= pivot:
                high = high - 1
            while low <= high and iter_obj[low] <= pivot:
                low = low + 1
            if low <= high:
                iter_obj[low], iter_obj[high] = iter_obj[high], iter_obj[low]
            else:
                break
        iter_obj[strat], iter_obj[end] = iter_obj[end], iter_obj[strat]
        return high

    def quicksort(self,iter_obj, strat, end):
        if strat >= end:
            return
        p = self.partition(iter_obj, strat, end)
        self.quicksort(iter_obj, strat, p - 1)
        self.quicksort(iter_obj, p + 1, end)

    def quickSort(self,iter_obj):
        self.quicksort(iter_obj,0,len(iter_obj)-1)
        return iter_obj
















s=Sort()
interger_arr=[6,5,4,3,2,1]
dupplicat__int_arr=[5,5,4,3,2,1,0]
float_ar=[2.1,0.0,0.3,4.6,7.8]
string_arr=["soehsh","jinal","naman","arpit","rahul"]
char_arr=["a","a","z","t","w","q"]
# print(s.bubbleSort(interger_arr))
# print(s.bubbleSort(dupplicat__int_arr))
# print(s.bubbleSort(float_ar))
# print(s.bubbleSort(string_arr))
# print(s.bubbleSort(char_arr))
# print(s.selctionSort(interger_arr))
# print(s.selctionSort(dupplicat__int_arr))
# print(s.selctionSort(float_ar))
# print(s.selctionSort(string_arr))
# print(s.selctionSort(char_arr))
#print(s.quickSort(interger_arr))