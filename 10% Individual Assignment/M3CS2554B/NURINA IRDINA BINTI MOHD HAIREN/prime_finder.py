import time
import math
from threading import Thread
from multiprocessing import Pool, cpu_count
import os

# -------------------------------
# Check if number is prime 
# -------------------------------
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# -------------------------------
# Sequential Method
# -------------------------------
def find_primes_sequential(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

# -------------------------------
# Threading Method 
# -------------------------------
def find_primes_threading(start, end):
    num_threads = 6  # match your 6‑core CPU
    result = []
    threads = []

    total = end - start + 1
    if total < num_threads:
        num_threads = total

    chunk_size = total // num_threads

    for i in range(num_threads):
        s = start + i * chunk_size
        e = (start + (i + 1) * chunk_size - 1) if i != num_threads - 1 else end
        if s > end:
            continue

        t = Thread(
            target=lambda q, w, r: r.extend([n for n in range(q, w + 1) if is_prime(n)]),
            args=(s, e, result),
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return result

# -------------------------------
# Multiprocessing Method
# -------------------------------
def is_prime_wrapper(n):
    return n, is_prime(n)

def find_primes_multiprocessing(start, end):
    num_processes = cpu_count()
    numbers = range(start, end + 1)

    with Pool(processes=num_processes) as pool:
        results = pool.map(is_prime_wrapper, numbers)

    primes = [n for n, is_p in results if is_p]
    return primes

# -------------------------------
# TEXT CHART FUNCTION 
# -------------------------------
def print_timing_chart(seq_time, thread_time, mp_time, start, end):
    print("\n📊 PERFORMANCE COMPARISON CHART")
    print("=" * 70)
    
    times = [seq_time, thread_time, mp_time]
    max_time = max(times)
    methods = ['Sequential', 'Threading', 'Multiprocessing']
    colors = ['🔴', '🟢', '🔵']
    
    for i, (method, time, color) in enumerate(zip(methods, times, colors)):
        bar_length = int((time / max_time) * 50)
        bar = '█' * bar_length + '░' * (50 - bar_length)
        speed_up = seq_time / time if time > 0 else 0
        print(f"{color} {method:<12} | {bar} | {time:7.4f}s | {speed_up:5.1f}x")
    
    print("=" * 70)
    fastest = min(times)
    winner = methods[times.index(fastest)]
    print(f"🏆 FASTEST: {winner} ({fastest:.4f}s)")
    print(f"📈 Total speedup vs Sequential: {seq_time/fastest:.1f}x")
    print(f"🔢 Range {start:,}-{end:,} → {len(primes_mp):,} primes found")

# -------------------------------
# MAIN PROGRAM
# -------------------------------
def main():
    print("\n=== PRIME NUMBER FINDER COMPARISON ===")
    try:
        start = int(input("\nEnter start of range: "))
        end = int(input("Enter end of range: "))
        if start < 1:
            print("Start should be at least 1.")
            return
        if end < start:
            print("End should be >= start.")
            return
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    print(f"\nProcessing range {start} to {end}...\n")

    # 1. Sequential
    t1 = time.time()
    primes_seq = find_primes_sequential(start, end)
    dummy = sum(1 for num in range(start, end + 1) if is_prime(num))
    t2 = time.time()
    seq_time = t2 - t1
    print("✅ Sequential finished.")

    # 2. Threading
    t3 = time.time()
    primes_thread = find_primes_threading(start, end)
    primes_thread.sort()
    t4 = time.time()
    thread_time = t4 - t3
    print("✅ Threading finished.")

    # 3. Multiprocessing
    t5 = time.time()
    global primes_mp  # Make global for chart
    primes_mp = find_primes_multiprocessing(start, end)
    primes_mp.sort()
    t6 = time.time()
    mp_time = t6 - t5
    print("✅ Multiprocessing finished.")

    # Terminal table
    print("\n" + "=" * 45)
    print(f"{'METHOD':<20} | {'TIME (seconds)':<15}")
    print("-" * 45)
    print(f"{'Sequential':<20} | {seq_time:.4f}s")
    print(f"{'Threading':<20} | {thread_time:.4f}s")
    print(f"{'Multiprocessing':<20} | {mp_time:.4f}s")
    print("=" * 45)

    # TEXT BAR CHART
    print_timing_chart(seq_time, thread_time, mp_time, start, end)

    # File output
    filename = "primes_output.txt"
    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Primes between {start}-{end}\nTotal: {len(primes_mp)}\n\n")
        for i in range(0, len(primes_mp), 10):
            f.write(", ".join(map(str, primes_mp[i:i + 10])) + "\n")

    print(f"\n💾 Full list saved to: {filename}")

if __name__ == "__main__":
    main()
