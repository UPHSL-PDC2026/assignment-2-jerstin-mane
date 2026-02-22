# Distributed Message Passing using MPI

## 📌 Project Description
This project demonstrates a simple distributed program using message passing. One process acts as the master process while other processes act as worker processes. Workers compute the sum of assigned number ranges and send the results to the master process.

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

## 🧠 Reflection

### Why is message passing required in distributed systems?
Message passing is important in distributed systems because processes may run on different computers and do not share memory. Sending and receiving messages helps processes communicate and share data.

### What happens if one process fails?
If one process fails, communication may be interrupted. The master process may wait for a message that will not arrive. The program may stop or hang. Distributed systems need ways to handle process failures.

### How does this model differ from shared-memory programming?
Message passing uses explicit communication where processes send and receive data. Each process has its own memory. In shared-memory programming, processes share the same memory space and can communicate using shared variables.

---

## 📸 Output Screenshots

### Code Output Screenshot

<img width="534" height="893" alt="image" src="https://github.com/user-attachments/assets/4cc50d10-3f63-4bb2-8300-5b50fdc28b01" />


---


### Program Result Screenshot

<img width="657" height="338" alt="image" src="https://github.com/user-attachments/assets/c6292063-ca59-4fd9-8175-d449a4d6a071" />
