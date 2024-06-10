Pytest + GitHub Actions
Pytest + GitHub Actions
Demo of the use of ============================= test session starts ==============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.1, pluggy-0.13.1
rootdir: /Users/blondeau/Downloads/Carberra/pytest-github-actions
plugins: Faker-8.10.0, pep8-1.0.6
collected 0 items / 1 error

==================================== ERRORS ====================================
____________________ ERROR collecting tests/test_person.py _____________________
ImportError while importing test module '/Users/blondeau/Downloads/Carberra/pytest-github-actions/tests/test_person.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
tests/test_person.py:5: in <module>
    from beings import Person
E   ModuleNotFoundError: No module named 'beings'
=========================== short test summary info ============================
ERROR tests/test_person.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.28s =============================== module + 
