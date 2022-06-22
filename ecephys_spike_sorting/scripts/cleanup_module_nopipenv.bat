ECHO off
title Script to run cleaning using cleanup_module.py and an input session name
ECHO navigating to code directory
cd C:\Users\svc_neuropix\Documents\GitHub\ecephys_spike_sorting
ECHO THIS SCRIPT PROCESSES 3 PROBES, YOU MUST ALSO START PROCESSING ON THE OTHER PROCESSING COMPUTER
set /p session_name=Full session name from EXPERIMENT DAY 2: 
ECHO activating environment and starting ecephys_spike_sorting\scripts\cleanup_module.py
call "C:\Users\svc_neuropix\Anaconda3\Scripts\activate.bat" "C:\Users\svc_neuropix\Anaconda3"
call conda activate sorting
call python ecephys_spike_sorting\scripts\cleanup_module.py %session_name%
cmd \k



