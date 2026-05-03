
# 🎲 Roll the Dice: A Speed Battle Between Sequential, Threading, and Multiprocessing
**NAME:** INTAN NURUL FASIHAH BINTI MOHD LAZIM

**STUDENT ID:** 2024442972

**CLASS:** M3CS2554A

**VIDEO DEMONSTRATION LINK:** https://youtu.be/sFz0jU-fFgI

--------------------------------------------------------------------------------------------------------------------------------
## 📝 INTRODUCTION
The Parallel Dice Combination Simulator is a Python-based application that simulates rolling dice a large number of times 

This project demonstrates three execution approaches:

- Sequential execution (single process)
- Concurrent execution using threading
- Parallel execution using multiprocessing

The goal is to compare performance and efficiency when processing large-scale data.
  
  ------------
 ## 🎯 OBJECTIVE
 
- Simulate large numbers of dice rolls
- Implement sequential processing as baseline
- Apply threading for concurrent execution
- Apply multiprocessing for parallel execution
- Compare execution time between methods
-----------

## 💻 SYSTEM REQUIREMENT
Hardware Requirements:
- Minumum 4GB RAM
- Multi-core CPU (recommended for multiprocessing)

Software Requirement
- Operating System: Windows
- Python version : 3.8 and above

Python Libraries (Built-in)
- ```random```
- ```time```
- ```threading```
- ```multiprocessing ```
  
  --------------
  ## ⚙️ INSTALLATION GUIDE
Step 1: Start Virtual Machine
1. Open VMware Workstation
2. Start your Kali Linux virtual machine
3. Log in to Kali Linux
 
 Step 2: Open Terminal
- Click Terminal or press:
```bash  
Ctrl + Alt + T
```
Step 3: Check Python Installation

Kali usually has Python pre-installed.

Run:

```bash  
python3 --version
```
If not installed:
```bash  
sudo apt update
sudo apt install python3 -y
```

Step 4: Create Project Folder
```bash  
mkdir parallel-dice-simulator-
cd parallel-dice-simulator-
```
Step 5: Create Python File
```bash  
nano main-dice.py
```
Step 6: Paste Your Code
Copy your Python code
Paste into main-dice.py
Save:

In nano:
- Press ```bash CTRL + X```
- Press ```bashY```
- Press ```bashEnter```

 ## ▶️ How It Runs in Kali Linux

Run the program using:
```bash  
python3 main.py
```
What Happens When You Run

Program simulates dice rolls
Executes:
- Sequential method
- Threading (concurrent)
- Multiprocessing (parallel)
- Measures execution time

2. Performance in VM

Running in VMware may be:
- Slower than real machine
- Limited by allocated CPU/RAM
👉 Recommended:
- Allocate at least 2–4 CPU cores
- Allocate 4GB RAM or more
  

💻 Source Code

```bash
import random
import time
from threading import Thread, Lock
from multiprocessing import Process, Manager, cpu_count
import matplotlib.pyplot as plt

# ---------------------------------------------------
# Roll N dice
# ---------------------------------------------------
def roll_dice(num_dice):
    return sum(random.randint(1, 6) for _ in range(num_dice))


# ---------------------------------------------------
# SEQUENTIAL
# ---------------------------------------------------
def run_sequential(total_rolls, num_dice):
    print("\n--- Sequential ---")

    start = time.time()

    for _ in range(total_rolls):
        roll_dice(num_dice)

    elapsed = time.time() - start
    print(f"Time: {elapsed:.2f} seconds")

    return elapsed


# ---------------------------------------------------
# THREADING WORKER
# ---------------------------------------------------
def threading_worker(num_rolls, num_dice):
    for _ in range(num_rolls):
        roll_dice(num_dice)


# ---------------------------------------------------
# THREADING
# ---------------------------------------------------
def run_threading(total_rolls, num_dice, num_threads=4):
    print("\n--- Threading (Concurrent) ---")

    threads = []

    chunk = total_rolls // num_threads
    remainder = total_rolls % num_threads

    start = time.time()

    for i in range(num_threads):
        rolls = chunk + (1 if i < remainder else 0)
        t = Thread(target=threading_worker, args=(rolls, num_dice))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start
    print(f"Time: {elapsed:.2f} seconds")

    return elapsed


# ---------------------------------------------------
# MULTIPROCESSING WORKER
# ---------------------------------------------------
def process_worker(num_rolls, num_dice):
    for _ in range(num_rolls):
        roll_dice(num_dice)


# ---------------------------------------------------
# MULTIPROCESSING
# ---------------------------------------------------
def run_multiprocessing(total_rolls, num_dice):
    print("\n--- Multiprocessing (Parallel) ---")

    processes = []
    num_processes = cpu_count()

    chunk = total_rolls // num_processes
    remainder = total_rolls % num_processes

    start = time.time()

    for i in range(num_processes):
        rolls = chunk + (1 if i < remainder else 0)
        p = Process(target=process_worker, args=(rolls, num_dice))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    elapsed = time.time() - start
    print(f"Time: {elapsed:.2f} seconds")

    return elapsed


# ---------------------------------------------------
# GRAPH
# ---------------------------------------------------
def plot_graph(seq, thr, proc):
    methods = ["Sequential", "Threading", "Multiprocessing"]
    times = [seq, thr, proc]
    colors = ["blue", "orange", "green"]

    plt.figure()
    plt.bar(methods, times, color=colors)

    plt.xlabel("Execution Method")
    plt.ylabel("Time (seconds)")
    plt.title("Performance Comparison")

    for i, v in enumerate(times):
        plt.text(i, v, f"{v:.2f}", ha='center', va='bottom')

    plt.savefig("performance.png")
    print("\nGraph saved as performance.png")


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------
def main():
    try:
        num_dice = int(input("Enter number of dice: "))
        total_rolls = int(input("Enter number of rolls: "))

        if num_dice < 1 or total_rolls < 1:
            raise ValueError

    except ValueError:
        print("Invalid input. Using default values (2 dice, 1,000,000 rolls).")
        num_dice = 2
        total_rolls = 1_000_000

    print(f"\nSimulating {total_rolls:,} rolls with {num_dice} dice...")
    print(f"CPU cores available: {cpu_count()}")

    seq_time = run_sequential(total_rolls, num_dice)
    thr_time = run_threading(total_rolls, num_dice)
    proc_time = run_multiprocessing(total_rolls, num_dice)

    plot_graph(seq_time, thr_time, proc_time)


# ---------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------
if __name__ == "__main__":
    main()


```
--------------------------------

# Sample Input / Output


Sample Input
```bash  
Enter number of dice: 2
Enter number of rolls: 1000000
```

Sample Output
```bash  
Simulating 1,000,000 rolls with 2 dice...
CPU cores available: 4

--- Sequential ---
Time: 0.85 seconds

--- Threading (Concurrent) ---
Time: 1.10 seconds

--- Multiprocessing (Parallel) ---
Time: 0.60 seconds

```
Graph saved as performance.png

<img width="637" height="482" alt="Screenshot 2026-04-28 111412" src="https://github.com/user-attachments/assets/6ef9e291-b014-420f-9a62-6419763859ee" />

-----------------------
# 📌 Conclusion

This program demonstrates how:

- Sequential processing works step-by-step
- Threading improves performance using concurrency
- Multiprocessing achieves the best performance using parallel execution

The results also confirm the probability distribution of dice combinations, where 7 is the most frequent outcome.
  

  
 

  




