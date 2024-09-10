from code import *
import time
if __name__ == '__main__':
    while True:
        q = input('Please Enter the Search Query:')
        start = time.time()
        url = tree.search(q)
        if url:
            print('Output: ', url)
            print('URLs Located in Memory.')
        else:
            url = finding_from_disk(q)
            if url:
                print('Output: ', url)
                print('URLs Located in Disk.')
            else:
                print('No such query found.')
        end = time.time()
        print('Time taken to execute this query :', end-start)
        if input('If you want to search again type 1 else 0: ') != '1':
            break

