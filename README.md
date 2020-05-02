# computersystem
# computersystem

Question 1: What is the default block size on HDFS? What is the default replication factor of HDFS on Dataproc?
Answer 1: 128MB, 2

Question 2: What is the completion time of the task?
Answer 2: 3 min 28 sec

Question 3: Is the performance getting better or worse in terms of completion time? Briefly explain.
Answer 3: 2 min 28 sec. Better. Because we have two work nodes to execute the task. 

Question 4: Is the performance getting better or worse in terms of completion time? Briefly explain.
Answer 4: 2 min 17 sec. A bit better. As block size increases, it takes longer latency to read a single block, and thus the # of IOPS decreases. Inversely, smaller block sizes yield higher IOPS.

Question 5: Does the job still finish? Do you observe any difference in the completion time? Briefly explain your observations.
Answer 5: The job can still finish. From 29 min 18 sec to 1 hr 4 min. Because we shut down one node, only one left running this task. So the running time doubled.

Question 6: Do you observe any difference in the completion time? Briefly explain.
Answer 6: 29 min 54 sec. No obvious difference.

Question 7: is the performance getting better or worse in terms of completion time? Briefly explain.
Answer 7: 28 min 44 sec. Better. As block size increases, it takes longer latency to read a single block, and thus the # of IOPS decreases. Inversely, smaller block sizes yield higher IOPS.

Question 8: What is the completion time of the task?
Answer 8: 1 hr 53 min
