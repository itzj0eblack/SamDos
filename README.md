🛠️ SamyDoS – Simple DoS Attack Tool (for Educational Use Only)

SamyDoS is a lightweight Python-based Denial of Service (DoS) simulation tool designed for educational and network testing purposes. It demonstrates how a basic multithreaded TCP DoS attack works by repeatedly opening socket connections to a target server and sending HTTP GET requests.

🚀 Features
	•	Sends continuous HTTP requests using random User-Agent headers.
	•	Utilizes multithreading to increase traffic volume.
	•	Displays a real-time dashboard with:
	•	Packets sent
	•	Errors encountered
	•	Number of active threads
	•	Styled terminal output using the rich library for better visuals.
	•	ASCII art header for aesthetic touch.

⚙️ How It Works
	1.	The script prompts the user to input:
	•	Target IP or domain
	•	Target port
	•	Number of threads to use
	2.	It then starts multiple threads, each creating TCP socket connections to the target.
	3.	Each connection sends a forged HTTP GET request with a random User-Agent.
	4.	The script tracks the number of packets sent and errors in real-time using a synchronized dashboard.

📦 Requirements
	•	Python 3.6+
	•	rich library (pip install rich)
