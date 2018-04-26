"""
Provides tests for the Task Runner
"""
from TaskRunner import TaskRunner


def test_basic_task_runner():
    """
    Tests the basic task runner
    :return:
    """
    # pylint: disable=unused-variable, missing-docstring
    runner = TaskRunner()

    results = []

    @runner.task
    def first_task():
        results.append(1)

    @runner.task
    def second_task():
        results.append(2)

    @runner.task
    def third_task():
        results.append(3)

    runner.run_tasks()
    assert results == [1, 2, 3]


def test_async_task_runner():
    """
    Tests the async task runner when it's written
    :return:
    """
    pass
