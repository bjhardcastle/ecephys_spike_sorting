ECHO off
title Script to run sorting using full_from_kilosort.py and an input session name
ECHO navigating to code directory
cd C:\Users\svc_neuropix\Documents\GitHub\ecephys_spike_sorting
setlocal EnableDelayedExpansion
set session=%1
ECHO activating environment and starting ecephys_spike_sorting\scripts\full_from_kilosort.py
if "%~1" == "" set /p session=Full session name or just lims ID: 
call "C:\Users\svc_neuropix\Anaconda3\Scripts\activate.bat" "C:\Users\svc_neuropix\Anaconda3"
call conda activate sorting
call python ecephys_spike_sorting\scripts\download_session_to_acq_drives.py %session% "ABCDEF"
call python ecephys_spike_sorting\scripts\just_extraction.py %session%
call conda deactivate
if "%~1" == "" cmd /k
