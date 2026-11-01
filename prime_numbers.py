#Python Program to Find Prime Numbers in a Given Range

def find_prime(n):
    
    prime_list=list()
    
    for num in range(2,n+1):
        if not is_nonprime(num):
            prime_list.append(num)
            
    return f'There are {len(prime_list)} prime numbers present and are {prime_list} '
    
    
def is_nonprime(num):
    
    n_factors=0
    
    if num==0 or num==1:
        print('0 and 1 are special numbers ')
    else:
        for i in range(2,num):
            if num%i==0:
                n_factors+=1 
    return n_factors

def main():
    num_range=int(input('enter a number range'))
    print(find_prime(num_range))

main()
