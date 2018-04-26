"""
Fetch service fetches data from APIs

APIs are registered similar to the functions below to the Task Runner

Each of these functions are run in sequence. When multiple APIs are being
fetched then future work will make the TaskRunner asynchronous

This file is for running the FetchService as a standalone
"""
from TaskRunner import TaskRunner

from .apis import fetch_irish_water

if __name__ == "__main__":
    # add all the FetchService functions and run them
    runner = TaskRunner()  # pylint: disable-msg=invalid-name
    runner.task(fetch_irish_water)
    runner.run_tasks()
