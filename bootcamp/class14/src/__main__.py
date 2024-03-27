import schedule
import time
from lib.classes.CsvSource import CsvSource
from lib.classes.JsonSource import JsonSource
from lib.classes.TxtSource import TxtSource

# Function to check for new files
def check_for_new_files():
    csv_source.check_for_new_files()  # Call the check_for_new_files method of the instance
    txt_source.check_for_new_files()
    json_source.check_for_new_files()

# Schedule the execution of check_for_new_files() every 10 seconds
schedule.every(10).seconds.do(check_for_new_files)

csv_source = CsvSource()
txt_source = TxtSource()
json_source = JsonSource()

# Execute the main loop
while True:
    schedule.run_pending()
    time.sleep(1)  # Wait for 1 second to avoid excessive processing in the loop