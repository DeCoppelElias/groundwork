@echo off
rem Runs the checker over the current project, or over the folder given.
python "%~dp0..\scripts\docs_check.py" %*
