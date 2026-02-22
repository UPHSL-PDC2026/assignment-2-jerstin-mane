# Distributed Message Passing using MPI

## 📌 Objective
Implement a simple distributed program where multiple processes communicate using message passing.

## 💻 Program Features
- Uses MPI communication
- Master-worker process model
- Message passing using send and receive
- Simple computation (sum of numbers)

## ⚙️ How the Program Works
- Process 0 is the master process.
- Other processes are worker processes.
- Each worker is assigned a range of numbers.
- Workers compute the sum of their assigned numbers.
- Workers send the results to the master process.
- The master process receives and displays the results.

## 💻 Program Code

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print("Master process started.\n")

    for i in range(1, size):
        message = comm.recv(source=i)

        print(f"Received from Worker {message['rank']}:")
        print(f"Assigned Task: {message['task']}")
        print(f"Computed Sum: {message['result']}")
        print("-" * 40)

    print("\nAll worker results successfully received.")
    print("Program completed.")

else:
    start = rank * 10
    end = start + 9

    result = sum(range(start, end + 1))

    message = {
        "rank": rank,
        "task": f"Sum of numbers from {start} to {end}",
        "result": result
    }

    comm.send(message, dest=0)
