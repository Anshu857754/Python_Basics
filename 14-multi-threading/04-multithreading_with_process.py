### Multiprocessing with ProcessPoolExecutor
# Calculate karna ho → Process Pool

from concurrent.futures import ProcessPoolExecutor

import time

def cube_number(number):
    time.sleep(3)
    return f"Cube: {number*number*number}"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]



if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=7) as executor:
        results = executor.map(cube_number,numbers)

    for result in results:
        print(result)