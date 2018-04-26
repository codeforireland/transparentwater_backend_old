"""
The basic TaskRunner class
"""


class TaskRunner:
    """
    Provides a template for TaskRunner classes
    """
    def __init__(self):
        self.tasks = []

    def task(self, task):
        """
        Add a task to the list of tasks to run
        :param task:
        :return:
        """
        self.tasks.append(task)

    def run_tasks(self):
        """
        run the list of tasks
        :return:
        """
        for task in self.tasks:
            task()
