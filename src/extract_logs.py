import sys
import os
import logging

# Setup logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, "extract_logs.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract_logs(date, log_file, output_dir="output"):
    """Extracts logs for a given date and saves them in output/output_YYYY-MM-DD.txt"""
    output_file = os.path.join(output_dir, f"output_{date}.txt")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    logging.info(f"Started extracting logs for date: {date}")

    try:
        with open(log_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            count = 0
            for line in infile:
                if line.startswith(date):  # Fast date filtering
                    outfile.write(line)
                    count += 1

        logging.info(f"Successfully extracted {count} log entries for {date}")
        print(f"✅ Logs for {date} saved to {output_file}")

    except FileNotFoundError:
        logging.error(f"Log file '{log_file}' not found.")
        print(f"❌ Error: Log file '{log_file}' not found.")
    except Exception as e:
        logging.exception(f"Unexpected error occurred: {e}")
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("⚠️ Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date = sys.argv[1]
    log_file = "src/logfile.text"  


    extract_logs(date, log_file, output_dir="output")  
