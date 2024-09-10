from code import *
import time
with open('TimeReport.txt' , 'w') as report:

    with open('50LessFrequent.txt') as f:
        report.write('-----------LESS FREQUENT QUERIES----------\n')
        for i in range(10):
            line = f.readline().rsplit('\n')[0]
            q, fr = line.split(':')
            start = time.time()
            url = finding_from_disk(q)
            end = time.time()
            report.write(q.ljust(30) + str(end-start).center(40) + '\n')

        report.write('------------------------------------------\n')
        report.write('\n')
        report.write('-----------MOST FREQUENT QUERIES----------\n')

    with open('50MostFrequent.txt') as f:
        for i in range(10):
            line = f.readline().rsplit('\n')[0]
            q, fr = line.split(':')
            start = time.time()
            url = tree.search(q)
            end = time.time()
            report.write(q.ljust(30) + str(end-start).center(40) + '\n')
        report.write('------------------------------------------\n')