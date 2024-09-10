from collections import defaultdict
from maxheap import *
from collections import deque
from BST import *
import os


history_frequency = defaultdict(int)
with open('search-history.txt', 'r') as f:
    for line in f:
        each = line.split('\n')[0]
        history_frequency[each] += 1


urls = dict()
with open('search-results.txt') as f:
    for line in f:
        line = line.rsplit('\n')[0]
        his, res = line.split(':')
        urls[his] = res



heap = Maxheap()
for each, freq in history_frequency.items():
    heap.insert(History(each, freq))

lst = []
f = open('50MostFrequent.txt', 'w')
for i in range(10000):
    popped = heap.delete()
    f.writelines(popped.history + ':' + ' ' + str(popped.freq) + '\n')
    lst.append(popped.history)
f.close()
lst.sort()


# l1 = lst[:2500]; l2 = lst[2500:5000]; l3 = lst[5000:7500]; l4 = lst[7500:]
# lst = l4 + l1 + l2 + l3
# lst = deque(lst)
# with open('MostFrequent.txt', 'w') as f:
#     while lst:
#         f.writelines(lst.popleft() + '\n')
#         f.writelines(lst.pop() + '\n')

# tree = BinarySearchTree()
# with open('MostFrequent.txt') as f:
#     line = f.readline().rsplit('\n')[0]
#     while line:
#         url = urls.get(line)
#         tree.insert(line, url)
#         line = f.readline().rsplit('\n')[0]


def arranging(lst: list, result=[]) -> list:
    '''It assists arrange to do the job.'''
    if lst:
        mid = len(lst) // 2
        result.append(lst[mid])
        left = lst[:mid]
        right = lst[mid+1:]
        arranging(left, result)
        arranging(right, result)
    return result


def arrange(lst: list) -> list:
    '''This function helps to make sure that the list is arranged in a way that the tree is balanced.'''
    result = []
    return arranging(lst, result)


lst = deque(arrange(lst))
tree = BinarySearchTree()
while lst:
    query = lst.popleft()
    tree.insert(query, urls.get(query))

k = 0
not_frequent = []
f = open('50LessFrequent.txt', 'w')
while heap.get_size() > 0:
    p = heap.delete()
    if k > 100000 and k <100051:  # UNCOMMENT FOR FIRST RUN
        f.writelines(p.history + ':' + ' ' + str(p.freq) + '\n')
    not_frequent.append(p.history)
    k += 1
f.close()


# for i in range(26):
#     os.makedirs('Less frequent', exist_ok=True)
#     filename = f'{chr(i + 97)}.txt'
#     file_path = os.path.join(os.path.join(os.path.dirname(__file__), 'Less frequent'), filename)
#     with open(file_path, 'w') as f:
#         for query in not_frequent:
#             if query[0] == chr(i + 97):
#                 f.writelines(query + '\n')



# ------- METHOD-1 : Making files and not using tree for less frequent queries -------
not_frequent.sort()
names =[]
while not_frequent:
    lst2 = not_frequent[:1000]
    not_frequent = not_frequent[1000:]
    first_query = lst2[0]
    names.append(first_query)
    file = f'{first_query}.txt'
    os.makedirs('Less frequent', exist_ok=True)
    path = os.path.join(os.path.join(os.path.dirname(__file__), 'Less frequent'), file)
    with open(path, 'w') as f:
        for query in lst2:
            url = urls.get(query)
            f.writelines(query + ':' + ' ' + url + '\n')



def finding_from_disk(query: str) -> str:
    for i in range(len(names)-1):
        if names[i] <= query < names[i+1]:
            file_path = os.path.join(os.path.join(os.path.dirname(__file__), 'Less frequent'), f'{names[i]}.txt')
            with open(file_path, 'r') as f:
                for line in f:
                    if line.split(':')[0] == query:
                        return line.split(':')[1].rsplit('\n')[0]
    else:
        file_path = os.path.join(os.path.join(os.path.dirname(__file__), 'Less frequent'), f'{names[-1]}.txt')
        with open(file_path, 'r') as f:
            for line in f:
                if line.split(':')[0] == query:
                    return line.split(':')[1].rsplit('\n')[0]
    return


# ------- METHOD-2: MAKING TREE FOR LESS FREQUENT QUERIES-------

# lst2 = [i for i in not_frequent]
# lst2 = arrange(lst2)
# tree2 = BinarySearchTree()
# for query in lst2:
#     file = f'{query}.txt'
#     os.makedirs('Less frequent2', exist_ok=True)
#     path = os.path.join(os.path.dirname(__file__), 'Less frequent2', file)
#     with open(path, 'w') as f:
#         url = urls.get(query)
#         f.writelines(url)
#     tree2.insert(query, file)
# def finding_from_disk(query: str) -> str:
#     file = tree2.search(query)
#     if not file: return
#     file_path = os.path.join(os.path.join(os.path.dirname(__file__), 'Less frequent2'), file)
#     with open(file_path, 'r') as f:
#         return f.read()

