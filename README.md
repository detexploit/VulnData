# VulnData

## About

Vulnerability data generator (converter) for [DetExploit](https://github.com/moppoi5168/DetExploit).

## Setup

1. Open task scheduler on Windows OS (taskschd.msc)
2. Create the folder named 'VulnData' under the Task Scheduler Library
3. Create the new task under the 'VulnData' with the settings below. 

```
Name: VulnData Daily Execution
Description: Task to exec VulnData (NVD.py) everyday
[x] Even user is not logged-on, execute it

Trigger: Everyday (00:00)

Manipulation: 
PROGRAM_OR_SCRIPT = PATH_TO_PYTHON.EXE
ARG = PATH_TO_nvd.py
```

## Requirements

Just run nvd.py and t&e.

## License

GPLv2 License

