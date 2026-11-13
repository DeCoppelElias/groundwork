@echo off
rem Runs the checker over the current project, or over the folder given.
where python >nul 2>nul && (
    python "%~dp0..\scripts\docs_check.py" %*
    exit /b %errorlevel%
)
py -3 "%~dp0..\scripts\docs_check.py" %*
