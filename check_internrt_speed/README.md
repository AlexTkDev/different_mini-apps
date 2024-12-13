# Project: Internet Speed Test
This project provides a simple way to measure internet connection speed with a progress bar displayed during the test. The project outputs download speed, upload speed, and ping.

## Functionality
- Measures **Download speed**, **Upload speed**, and **Ping** using the `speedtest` library.
- Displays an animated progress bar that lasts throughout the measurement and automatically completes at 100% when the test finishes.

## Installation

### Requirements
- Python version 3.7 or above
- Required libraries:
  - `speedtest-cli` - to measure internet speed
  - `tqdm` - to display the progress bar

### Installing Dependencies
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # for Linux and macOS
   .venv\Scripts\activate     # for Windows
   ```

2.Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the script, execute the following command in the terminal:
```bash
python main.py
```

The script will start the measurement process and display results:
- **Download speed**: speed in Mbps
- **Upload speed**: speed in Mbps
- **Ping**: latency in milliseconds

Example output:
```
Testing download speed: 100%|███████████████████████████████████████████| 100/100 [00:10<00:00,  9.50it/s]
Testing upload speed: 100%|█████████████████████████████████████████████| 100/100 [00:10<00:00,  9.70it/s]

Download speed: 93.68 Mbps
Upload speed: 91.67 Mbps
Ping: 2.9 ms
```

## Code Structure
- **`show_progress_bar(description, stop_event)`**: Displays a progress bar with the provided description. Uses an `Event` object to complete at the end of the measurement and sets the bar to 100% once finished.
- **`perform_speedtest()`**: Runs the speed test using the `speedtest` library. `show_progress_bar` is called in separate threads for download and upload measurements.
- **`display_results(down_speed, up_speed, ping)`**: Formats and prints the results.
- **`main()`**: Main function that calls the speed test process and displays the results.

## Error Handling
- In case of errors, such as an unavailable internet connection or issues with the `speedtest` library, an error message will be displayed.

## Notes
This project can be further developed for automatic internet speed testing or real-time connection quality monitoring.

## License
This project is distributed under the MIT License.
