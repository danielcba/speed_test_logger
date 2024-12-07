# Speed Test Logger

This project uses the `speedtest` library to measure Internet speed and save the results in a CSV file. It is ideal for monitoring your connection's performance over time.

## Features

- Performs tests for download speed, upload speed, and latency (ping).
- Automatically selects the server with the best latency.
- Saves results in a structured CSV file.

## Requirements

- Python 3.7 or higher
- Required libraries:
  - `speedtest`
  - `csv` (included with Python)
  - `os` (included with Python)

To install the `speedtest` library, run:

```bash
pip install speedtest-cli
```

## Usage

1. Download or clone this repository.
2. Run the script:

```bash
python speed_test_logger.py
```

3. The results will be automatically saved in the `speedtest_results.csv` file.

## CSV File Structure

The file contains the following columns:

| Column            | Description                                           |
|-------------------|-------------------------------------------------------|
| Server ID         | Unique identifier of the server                      |
| Sponsor           | Name of the server's sponsor                         |
| Server Name       | Name of the server                                   |
| Timestamp         | Date and time of the test                            |
| Distance          | Distance to the server (in km)                       |
| Ping              | Latency in milliseconds (ms)                         |
| Download          | Download speed (in bits/s)                           |
| Upload            | Upload speed (in bits/s)                             |
| Share             | URL to share the results                             |
| IP Address        | Client's IP address                                  |

## Contributions

Contributions are welcome! If you have suggestions or improvements, please open an issue or a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
