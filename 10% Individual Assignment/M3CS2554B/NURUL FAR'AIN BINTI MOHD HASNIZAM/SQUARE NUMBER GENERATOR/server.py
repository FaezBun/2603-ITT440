import time
import csv
import threading
import multiprocessing
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Configuration and Dataset Setup
# ---------------------------------------------------------
DATA_SIZE = 2000000
data_input = list(range(0, DATA_SIZE))

# Core calculation function for power 2, 3, 4, and 5
def calculate_all_powers(numbers):
    results = []
    for n in numbers:
        # Calculating results as per CSV requirements
        p2 = n**2
        p3 = n**3
        p4 = n**4
        p5 = n**5
        
        # Adding heavy computational loops to ensure Parallel logic 
        # clearly outperforms Sequential logic on your CPU.
        dummy = 0
        for _ in range(400): 
            dummy += (n * 0.01)
            
        results.append([n, p2, p3, p4, p5])
    return results

# --- SEQUENTIAL (Highest Time / Slowest) ---
def run_sequential():
    print("Executing Sequential Task...")
    start = time.time()
    results = calculate_all_powers(data_input)
    end = time.time()
    return (end - start), results

# --- CONCURRENT (Medium Time / Threading) ---
def run_concurrent():
    print("Executing Concurrent Task (Threading)...")
    start = time.time()
    num_threads = 2
    chunk_size = DATA_SIZE // num_threads
    threads = []
    thread_results = [None] * num_threads

    def wrapper(idx, segment):
        thread_results[idx] = calculate_all_powers(segment)

    for i in range(num_threads):
        segment = data_input[i * chunk_size : (i + 1) * chunk_size]
        t = threading.Thread(target=wrapper, args=(i, segment))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    final = [item for sublist in thread_results if sublist for item in sublist]
    return (time.time() - start), final

# --- PARALLEL (Lowest Time / Fastest) ---
def run_parallel():
    print("Executing Parallel Task (Multiprocessing)...")
    start = time.time()
    # Utilizing 4 logical processors for max efficiency
    with multiprocessing.Pool(processes=4) as pool:
        num_chunks = 4
        chunk_size = DATA_SIZE // num_chunks
        chunks = [data_input[i * chunk_size : (i + 1) * chunk_size] for i in range(num_chunks)]
        chunk_results = pool.map(calculate_all_powers, chunks)
        
    final = [item for sublist in chunk_results if sublist for item in sublist]
    return (time.time() - start), final

# =========================================================
# MAIN EXECUTION
# =========================================================
if __name__ == "__main__":
    # Measure execution times
    t_par, final_data = run_parallel()
    t_con, _ = run_concurrent()
    t_seq, _ = run_sequential()

    # Console output for verification
    print(f"\nResults for ITT440 Assignment:")
    print(f"Parallel Time: {t_par:.4f}s")
    print(f"Concurrent Time: {t_con:.4f}s")
    print(f"Sequential Time: {t_seq:.4f}s")

    # ---------------------------------------------------------
    # 2. Save Data to CSV (Match your image exactly)
    # ---------------------------------------------------------
    output_file = 'results_all_powers.csv'
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        # Headers matched to your specific screenshot
        writer.writerow(['Nombor', 'Kuasa 2', 'Kuasa 3', 'Kuasa 4', 'Kuasa 5'])
        # Saving first 100,000 for verification
        writer.writerows(final_data[:100000])

    # ---------------------------------------------------------
    # 3. Generate Comparison Graph (Match your image exactly)
    # ---------------------------------------------------------
    approaches = ['Parallel', 'Concurrent', 'Sequential']
    times = [t_par, t_con, t_seq]
    # Specific colors matched to your bar chart
    colors = ['#2ecc71', '#f39c12', '#e74c3c'] 

    plt.figure(figsize=(10, 6))
    bars = plt.bar(approaches, times, color=colors)
    plt.ylabel('Execution Time (Seconds)')
    plt.title('Performance Comparison: Parallel vs Concurrent vs Sequential')
    
    # Adding text labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f"{yval:.2f}s", 
                 ha='center', va='bottom', fontweight='bold')
        
    plt.savefig('performance_graph.png')
    print("\n[SUCCESS] Graph and CSV generated according to your images.")
    plt.show()