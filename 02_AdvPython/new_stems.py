#!/usr/local/bin/python3
# Python 3 version

import multiprocessing
from multiprocessing import Process
from mmytimer import MyTimer

def find_current_best_stem(stems: dict, offset: int, length: int) -> None:

    for stem_size in range(offset, length):
        best_stem = ""
        best_count = 0
        
        for stem, count in stems.items():            
            if stem_size == len(stem) and count > best_count:
                best_stem  = stem
                best_count = count

        if best_stem:
            print ("Most popular stem of size", stem_size, "is:",
                    best_stem, "(occurs", best_count, "times)")

if __name__ == '__main__':   
    multiprocessing.freeze_support()
    
    stems = {}
    processes = []

    n: int = 30
    max_concurrent_processes: int = multiprocessing.cpu_count()
    n_per_cpu: int = 1 + int(n / max_concurrent_processes)

    with MyTimer('Loaded file successfully'):
        for row in open("02_AdvPython/words"):
            for count in range(1, len(row)):
                stem = row[0:count]
                if stem in stems:
                    stems[stem] += 1
                else:
                    stems[stem] = 1
            
    with MyTimer('Processes joined'):                
        for i in range(0, max_concurrent_processes):
            start_pos = 1 + (i * n_per_cpu)
            end_pos = min(n, start_pos + n_per_cpu)
            
            process = Process(target = find_current_best_stem, args = (stems, start_pos, end_pos))
            processes.append(process)
            process.start()
                    
        for process in processes:
            process.join()
