try:
    with open('numbers.txt','r') as f1:
        nums=f1.readlines()
    
except FileNotFoundError:
    print('File does not exist')
    
else:
    with open('even.txt','w') as evenf , open('odd.txt','w') as oddf:
        for num in nums:
            num=int(num.strip())
        
            if num%2==0:
                evenf.write(str(num)+'\n')
            else:
                oddf.write(str(num)+'\n')

finally:
    print('Numbers are written in respective files')
