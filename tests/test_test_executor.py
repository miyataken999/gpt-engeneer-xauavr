from autoscriptest.test_executor import TestExecutor
import pytest

def test_test_executor():
    script_file = 'test_script.txt'
    executor = TestExecutor(script_file)
    executor.execute()
    assert True