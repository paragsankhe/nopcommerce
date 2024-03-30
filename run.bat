@echo off
call venv\scripts\activate
pytest -s -v -m "sanity" --html .\reports\test_report_chrome.html --browser chrome
rem pytest -s -v -m "sanity" --html .\reports\test_report_firefox.html --browser firefox
rem pytest -s -v -m "regression" --html .\reports\test_report_chrome.html --browser chrome
rem pytest -s -v -m "sanity and regression" --html .\reports\test_report_chrome.html --browser chrome
rem pytest -s -v -m "sanity or regression" --html .\reports\test_report_chrome.html --browser chrome
pause
