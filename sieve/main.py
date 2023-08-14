import math

# try:
#     end_num = int(input("Set the end number: "))
# except TypeError:
#     print('Error: Please input an integer')
# else:
#     if end_num <= 1:
#         print('Please pick a positive number greater than 1')
#     else:
#         pass


def check_square_root (num):
    '''
    Check if end num is a perfect square by deducting the square root to the rounded floor of the square root
    '''
    square_root = math.sqrt(num)
   
    if square_root - math.floor(square_root) != 0:
        return num
    else:
        return square_root

def sieve(end_num):
    '''
    Run a sieve
    '''
    prime_list = []
    num_list=[]
    
