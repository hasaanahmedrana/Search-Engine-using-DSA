with open('50MostFrequent.txt') as f, open('Report.txt', 'w') as report:
    report.write('-------------------- TOP 50 MOST SEARCHES.-----------------------\n')
    report.write('\n')
    report.write('Query'.ljust(30) + 'Frequency'.ljust(10) + 'Probability'.center(30) + '\n')
    for i in range(50):
        line = f.readline().rsplit('\n')[0]
        q, fr = line.split(':')
        report.write(q.ljust(30) + fr + str(int(fr) / 9930936).center(50) + '\n')