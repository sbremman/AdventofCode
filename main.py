
import day_04 as day

import time



if __name__ == '__main__':
    start_time = time.time()

    file_name = "data/day_04_input_test"

    task_1_output = day.do_task_1(file_name)

    task_2_output = day.do_task_2(file_name)

    print(f"Time taken: {time.time()-start_time:.4f} seconds")

    print(f"Task 1 output: {task_1_output}")
    print(f"Task 2 output: {task_2_output}")



