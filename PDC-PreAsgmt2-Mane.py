# Import MPI library
from mpi4py import MPI

# Initialize communication world
comm = MPI.COMM_WORLD

# Get process rank (process ID)
rank = comm.Get_rank()

# Get total number of processes
size = comm.Get_size()

# Master process (Rank 0)
if rank == 0:
    print("Master process started.\n")

    # Receive messages from worker processes
    for i in range(1, size):
        message = comm.recv(source=i)

        print(f"Received from Worker {message['rank']}:")
        print(f"Assigned Task: {message['task']}")
        print(f"Computed Sum: {message['result']}")
        print("-" * 40)

    print("\nAll worker results successfully received.")
    print("Program completed.")

# Worker processes
else:
    # Assign data chunk based on process rank
    start = rank * 10
    end = start + 9

    # Compute sum of numbers in assigned range
    result = sum(range(start, end + 1))

    # Create message to send to master
    message = {
        "rank": rank,
        "task": f"Sum of numbers from {start} to {end}",
        "result": result
    }

    # Send computed result to master process
    comm.send(message, dest=0)