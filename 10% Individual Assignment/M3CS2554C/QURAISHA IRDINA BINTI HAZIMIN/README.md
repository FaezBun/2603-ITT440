
# 🚀 High-Volume Cashback Calculator

<p align="center">
  <img src="logo (2).png" width="600">
</p>

> **Audit Professional:** Quraisha Irdina Binti Hazimin    
> **Course:** ITT440-Individual Assignment  
> **Student ID:** 2025479998  
> **Github Link:** **https://github.com/irdinaquraisha/CASHBACK_CALCULATOR**  
> **Youtube Link:** **https://youtu.be/vEkoO0Yroes?si=BtiLAKTicksvfYYe**

---
### *Performance Analysis: Sequential vs. Concurrent vs. Parallel*


## 📌 1. Project Overview

This application is a **High-Volume E-Wallet Auditor** designed to simulate real-world financial data processing at scale. The system performs complex cashback calculations for **millions of transactions**, utilizing an optimized mathematical algorithm to determine rewards. 

The project benchmarks three major computing architectures:
* **Sequential:** Traditional serial processing (Baseline: **20.71s**).
* **Concurrent (Threading):** Task overlapping via the `threading` module (**17.53s**).
* **Parallel (Multiprocessing):** True simultaneous execution using multiple CPU cores to bypass the GIL (**9.97s**).

This tool demonstrates a **2.08x performance increase** through parallelism and generates automated audit reports and visual data breakdowns.

---

## 💻 2. System Requirements
| Requirement | Minimum Specification |
| :--- | :--- |
| **OS** | Windows 10+, macOS, or Linux |
| **Language** | Python 3.7+ |
| **Libraries** | `matplotlib`, `pandas`, `numpy` |
| **Hardware** | Multi-core CPU (recommended for Parallel testing) |

---

## 🛠️ 3. Installation Steps
1. **Install Python:** Ensure Python is installed on your system via [python.org](https://www.python.org/).
2. **Install dependencies:** 
   ```bash
   pip install matplotlib pandas numpy
3. **Setup Workspace:** Create a main folder: CASHBACK_PROJECT
4. **Create a sub-folder:** CASHBACK_PROJECT/receipt
5. **Save Script:** Save the project code as importmultiprocessing.py inside the main folder.

## 🏃 4. How to Run the Program
1. Open your terminal or IDE and navigate to the CASHBACK_PROJECT directory.
2. Launch the application:
```Bash
python importmultiprocessing.py
```
3. **Follow the Prompts:**
   Enter Merchant, Username and amount.
5. **View Results:** The system will display two graphs. Close the graph window to see the option to run another audit or exit.

## 📊 5. Performance Logic Explained
| Architecture | Implementation | Best For... | Behavior |
| :--- | :--- | :--- | :--- |
| **Sequential** | Standard Loop | Small tasks | Processes one item at a time; moves to the next only when the current one finishes. |
| **Concurrent** | `threading` | IO-Bound tasks | Tasks "overlap." While one task waits for a simulated server response, another begins. |
| **Parallel** | `multiprocessing` | CPU-Bound tasks | Tasks run at the exact same physical moment by utilizing multiple CPU cores simultaneously. |

## 📝 6. Sample Input/Output
### User Input Example:
* **Merchant:** Shein  
* **Username:** Irdina
* **Amount:** 7500.00
* **Count:** 8000000
 
**Generated Audit Receipt**
```text
=============================================
           OFFICIAL CASHBACK RECEIPT
=============================================
Merchant:           SHEIN
Customer Name:      irdina
Single Amount:      $7,500.00
Transaction Count:  8,000,000
---------------------------------------------
TOTAL CASHBACK:     $3,000,000,000.00
---------------------------------------------
PERFORMANCE METRICS:
Sequential Time:    20.7122s
Threading Time:     17.5272s
Parallel Time:      9.9721s
=============================================
```
# 🖼️ 7. Screenshots & Visuals
**Staircase Performance Benchmark**
<img src="final_result.png" width="600">
### Results & Performance Analysis

| Metric | Sequential (Baseline) | Concurrent (Threading) | Parallel (Multiprocessing) |
| :--- | :--- | :--- | :--- |
| **Execution Time** | **20.712s** | **17.527s** | **9.972s** |
| **Speedup Factor** | 1.0x (Reference) | ~1.18x Faster | **~2.08x Faster** |
| **CPU Utilization** | Single Core (100%) | Single Core (GIL Limited) | **Multiple Cores (4x 100%)** |
| **Efficiency** | Lowest | Moderate | **Highest** |

> **Note:** The Parallel method achieved the best results because the task is CPU-bound (heavy mathematical calculations), which benefits directly from additional physical

---

### 🔍 Key Findings

#### **1. Architecture Performance**
The performance metrics demonstrate a significant leap in efficiency when leveraging true parallelism:

* **The Bottleneck (Sequential):** Processing transactions one by one takes **20.712 seconds**. This method is limited to a single CPU core, creating a massive queue for high-volume data.
* **The Mid-Ground (Threading):** Threading offers a slight improvement at **17.527 seconds**. However, because this is a CPU-bound task (heavy math), it remains largely restricted by Python’s Global Interpreter Lock (GIL).
* **The Solution (Parallel):** By bypassing the GIL and distributing the workload across multiple physical CPU cores, the **Parallel** mode completes the task in just **9.972 seconds**.
* **Observation:** This implementation achieves a **2.08x speedup**. While system overhead prevents a perfect 1:1 linear speedup, the Parallel mode is **over twice as efficient** as standard execution.

### 2. Financial Distribution Insights
Analysis of the transaction breakdown (at a rate of 5% cashback):

* **85.0% Product Value:** The core value of the goods processed.
* **10.0% Tax:** Estimated tax overhead per transaction.
* **5.0% User Cashback:** For a $7,500.00 transaction, the reward is **$375.00**.
* **Scale Observation:** At a volume of 8M transactions, the system audited a total reward pool of **$3,000,000,000.00**.

---

# 📂 8. Source Code Technical Breakdown
The core of this project lies in how the script handles the ```complex_cashback_logic```—a CPU-intensive task involving 40 iterations of mathematical growth per transaction—across three distinct execution patterns:

**A. Sequential Logic**
This method uses a list comprehension to process transactions one by one in a single serial stream. It is the baseline for performance comparison, showing the raw time required without any optimization.
```
# Processes 8,000,000 transactions in a single loop
[complex_cashback_logic(amount) for _ in range(iterations)]
```
**B. Concurrent (Threading) Logic**
Uses the ```threading.Thread``` module to divide the workload into chunks (determined by ```num_threads```). While this manages multiple threads, it is still restricted by Python's **Global Interpreter Lock (GIL)**, meaning only one thread can execute Python bytecode at a time for this math-heavy task.
```
# Workload is split into chunks for each thread
for _ in range(num_threads):
    t = threading.Thread(target=worker)
    t.start()
```

**C. Parallel (Multiprocessing) Logic**
This is the most efficient method for this specific project. It uses multiprocessing.Pool to spawn separate processes, each with its own Python interpreter and memory space. This bypasses the GIL entirely, allowing the 8,000,000 transactions to be calculated truly simultaneously across multiple CPU cores.
```
# Uses starmap to distribute chunks across physical CPU cores
with multiprocessing.Pool(processes=num_procs) as pool:
    pool.starmap(parallel_worker_helper, args)
```
🔗 Source Code Files
The complete implementation can be found in the following file within this repository:
* [**importmultiprocessing.py**](importmultiprocessing.py)

### 💡 Conclusion for Auditor Report
The data confirms that for a real-world E-Wallet system, **Parallel Architecture** is the only viable solution for processing millions of transactions. Using standard Sequential loops would cause significant system lag and delay audit generation.
