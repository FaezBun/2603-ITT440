# NAME : NURUL FAR'AIN BINTI MOHD HASNIZAM
# STUDENT ID : 2024214892
# GROUP : M3CS2554B
# TITLE : SQUARE NUMBER GENERATOR

<img width="1132" height="489" alt="image" src="https://github.com/user-attachments/assets/c4b8fc4f-04e3-4d6e-86be-d97fb967bfb3" />

# Requirements
- Python 3.13
- VS Code

# Files
- server.py : The server-side script that listens for connections and performs the calculation.
- client.py : The client.py script that sends a number to the server and displays the result.

# Introduction
This project demonstrates a high-performance network application using Python's socket programming to handle large-scale data processing. The system implements a Square Number Generator designed to process 1,000,000 data entries by integrating Concurrent Threading for multiple client connections and Parellel Multiprocessing to distribute workloads across CPU cores. By combining these tecniques, the application ensures maximum computational efficiency and scalability, fulfilling the core requirements of the ITT440 individual task whileshowcasing practical data handling at the Transport Layer.

# Objectives
- Implement High-Performance Socket Programming
  - to develop a robust client-server application capable of handling high-volume data transmission via TCP/IP.
- Demonstrate Corcurrency with Multi-threading
  - To use threading techniques so the server can accept and manage multiple client connections simultaneously without blocking.
- Execute Parellel Computing
  - To utilize multiprocessing to distribute a heavy workload of 1,000,000 data entries across multiple CPU cores for faster calculation.
- Optimize System Efficiency
  - To reduce overall processing time and maximize hardware utilization compared to traditional sequantial execution.
- Analyze Performance Metrics
  - To monitor and report the exact time taken to process large datasets, proving the effectiveness of parallel and corcurrent techniques.

# System Design
The system follows a standard Client-Server architecture. We use TCP because it is connection-oriented, ensuring that the data is delivered reliably and in the correct order.
- Data Volume Specification
  To fulfil the requirement of processing a large volume of data, the system is designed to :
  - input : A trigger command from the client.
  - Process : The Server generates a list of 1,000,000 integers.
  - Workload : Using multiprocessing. Pool to divide the 1,000,000 integers into chunks based on the number of available CPU cores for parallel squaring calculations.

# Source Code Implementation
Server Side (server.py)
~~~
import socket
import threading
import multiprocessing
import time

# Function for Parallel Processing (Parallel Technique)
def calculate_square_batch(numbers):
    return [n * n for n in numbers]

def handle_client(conn, addr):
    print(f"\n[NEW CONNECTION] {addr} connected.")
    try:
        # Wait for command from client
        command = conn.recv(1024).decode()
        
        if command == "START_HEAVY_TASK":
            total_numbers = 1000000  # One Million Data Points (Large Volume)
            data = list(range(total_numbers))
            
            print(f"[PROCESS] Processing {total_numbers} square numbers for {addr}...")
            
            # Divide data into chunks based on CPU Core count (Parallelism)
            start_time = time.time()
            num_cores = multiprocessing.cpu_count()
            chunk_size = total_numbers // num_cores
            chunks = [data[i:i + chunk_size] for i in range(0, total_numbers, chunk_size)]
            
            # Using Multiprocessing Pool for parallel execution
            with multiprocessing.Pool(processes=num_cores) as pool:
                pool.map(calculate_square_batch, chunks)
            
            end_time = time.time()
            duration = end_time - start_time
            
            # Send result report back to the client
            response = f"SUCCESS: Generated {total_numbers} square numbers in {duration:.4f} seconds using {num_cores} CPU cores."
            conn.send(response.encode())
            print(f"[COMPLETE] Task finished for {addr} in {duration:.4f}s")
            
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        conn.close()

def start_server():
    # Setup Server Socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 65432))
    server.listen(5)
    print("--- SERVER HIGH-PERFORMANCE SQUARE GENERATOR ACTIVE ---")
    print("Waiting for client connections...")
    
    while True:
        conn, addr = server.accept()
        # Using Threading (Concurrent Technique)
        # Allows the server to accept new clients without waiting for heavy tasks to finish
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
~~~



Client Side (client.py)
~~~
import socket

def run_client():
    # Setup Client Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server's IP and Port
        client_socket.connect(('127.0.0.1', 65432))
        print("Connected to the High-Performance Server.")
        
        # Send command to trigger the large volume task
        client_socket.send("START_HEAVY_TASK".encode())
        
        # Receive the processing report from the server
        print("Waiting for server to process 1,000,000 data entries...")
        result = client_socket.recv(1024).decode()
        print(f"\nSERVER RESPONSE: \n{result}")
        
    except ConnectionRefusedError:
        print("Error: Could not connect to server. Ensure server.py is running.")
    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    run_client()
~~~

# How to run
1. Run the server first :
   ~~~
   python server.py
   ~~~
   The server will enter a "Listening" state, waiting for client connections using Multi-threading.
2. Open a second terminal and run the client :
   ~~~
   python client.py
   ~~~
   The client will establish a TCP connection to server at 127.0.0.1 65432.
3. Execution and Results
   - The client automatically sends the START_HEAVY_TASK command.
   - The server performs Parallel Processing to calculate 1,000,000 square numbers.
   - Once complete, the server sends a performance report (time and CPU usage) back to the client terminal.


# Results and Discussion
Execution Process
~~~
server.py
~~~
Output:
<img width="1543" height="912" alt="image" src="https://github.com/user-attachments/assets/46b84cde-6397-44d3-b279-8ba3faf1c5d7" />



Execution Process
~~~
client.py
~~~
Output:
<img width="1545" height="859" alt="image" src="https://github.com/user-attachments/assets/bab29f7c-62d2-44e3-84e9-dfebe5920088" />

- The system succesfully processed a data set of 1,000,000 numbers.
  - Total records : 1,000,000
  - Execution Time (Parallel) : 0.9289 s
  - CPU Cores Used : 4 Cores

# Conclusion
This project successfully demonstrates a high-performance network application that integrates Multi-threading (Concurrency) and Multiprocessing (Parellelism) to efficiently process a large volume of 1,000,000 square numbers over a TCP/IP connection. By utilizing multiple CPU cores to distribute the mathematical workload, the system significantly enhances computational efficiency and scalability compared to traditional sequential processing, while threading ensures the server remains responsive to multiple simultaneous client connections. This implementation not only fulfils all the tecnical requirements of the ITT440 individual assignment but also strengthens the practical understanding of the Transport Layer within the OSI Model and the optimization of socket programming for high-performance computing tasks.

# Demostration Video
