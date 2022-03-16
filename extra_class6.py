#2
def sum_of_digit(n):
    if n==0:
        return 0
    return (n%10+sum_of_digit(int(n/10)))
given_numbers= 123456
results= sum_of_digit(given_numbers)
print(results)

#3
def reverse(s):
    if s=="":
        return s
    else:
        return reverse(s[1:])+s[0]
s="nish"
print (reverse(s))

#4

def merge_sort(arr):
    if len(arr) >1:
        m= lrn(arr)//2
        div=arr[:m]
        half=arr[m:]
        merge_sort(div)
        merge_sort(half)
        k=j=i=0
        while i<len(div) and j<len(half):
            if div[i]<half[j]:
                arre[k]=div[i]
                i+=1
            else:
                arr[k]= half[j]
                j+=1
            k+=1
        while i< len(div):
            arr[k]=div[i]
            i+=1
            k+=1

        while j<len(half):
            arr[k]=half[j]
            j+=1
            k+=1

def print_l(arr):
    for i in range (len(arr)):
        print(arr[i], end="  ")
    print ()

if __name__ =='__main__':
    arr=[11,8,4,1,2,8,7,9,5,4]
    print_l(arr)
    merge_sort(arr)

#5

def insertion_sort(arr):
    for level in range(1, len(arr)):
        start= arr[level]
        j= level-1

        while j>=0 and start < arr[j]:
            arr[j+1]= arr[j]
            j -=1
        arr[j+1]=start
data=  [11,8,4,1,2,8,7,9,5,4]
print(insertion_sort(data))



