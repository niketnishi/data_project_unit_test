### Data Project with unit test

* Using python default unit test module as
```python
import unittest
```
#### For testing a particular function keep few things in mind

* Inherit `unittest.TestCase` to the class which has all the test functions
* Name of the function for each test class should start with `test_` to run
* One function can have several test cases
* Do not forget to give the test class a point of execution
```python
if __name__ == '__main__':
    unittest.main()
```
