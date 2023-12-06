
import day_05 as day

import time



if __name__ == '__main__':
    start_time = time.time()

    file_name = "data/day_05_test.txt"

    task_number = day.do_task_2(file_name)

    print(time.time()-start_time)

    print(task_number)
