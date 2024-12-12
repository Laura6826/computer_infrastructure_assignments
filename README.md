# Computer Infrastructure Assignments,24-25: 8645

## Assignments submitted as part of the module Computer Infrastructure 24-25: 8645, Higher Diploma in Science, Data Analytics

## *Author: Laura Lyons*

***

This README file was written using the [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) as a guidance document
***

  &#x26a0;&#xfe0f; **DISCLAIMER**

  Microsoft Co-Pilot was used to generate ideas of the content of the following notebook. That said, the notebook is mainly my own work, as I had to re-work the code the text in generated to meet my own needs (*The warning icon was sourced from [Stackoverflow](https://stackoverflow.com/questions/50544499/how-to-make-a-styled-markdown-admonition-box-in-a-github-gist)*).

## **Table of contents**

1. [Introduction.](#1-introduction).
1. [The purpose of this project.](#2-the-purpose-of-this-project)
1. [How to get started.](#3-how-to-get-started)
1. [How to get help.](#4-how-to-get-help)
1. [How to contribute.](#5-how-to-contribute)
1. [Weekly Tasks.](#6-weekly-tasks)

    1. [Task 01- Create Directory Structure](#task-01---create-directory-structure)
    2. [Task 02- Timestamps](#task-02---timestamps)
    3. [Task 03- Formatting Timestamps](#task-03---formatting-timestamps)
    4. [Task 04- Creating Timestamped Files](#task-04---creating-timestamped-files)
    5. [Task 05- Download Todays Weather Data](#task-05---download-todays-weather-data)
    6. [Task 06- Timestamp the Data](#task-06---timestamp-the-data)
    7. [Task 07- Write the Script](#task-07---write-the-script)
    8. [Task 08- Notebook](#task-08---notebook)
    9. [Task 09- Pandas](#task-09---pandas)

## 1. Introduction

This project was created to fulfill an assessment requirement of Computer Infrastructure 24-25: 8645, as part of the H.Dip in Science in Data Analytics.

Each week, following a series of lectures, a task was assigned to demonstrate both learning and additional reading/research on the topics discussed in the lectures.

This repository is collection of my weekly tasks, including some additional guidance and instruction in how to run each task/program.

***

## 2. The purpose of this project

As noted on the [assignment instructions](https://github.com/ianmcloughlin/2425_computer_infrastructure),

The purpose of the assessment is to ensure students can demonstrate the following:

1. Use, configure, and script in a command line interface environment.
1. Manipulate and move data and code using the command line.
1. Compare commonly available software infrastructures and architectures.
1. Select appropriate infrastructure for a given computational task.

***

## 3. How to get started

### Necessary software

In order to run the included files, you will need to ensure that you have access to the correct software. I would recommend downloading the following applications (ensuring sufficient space on your hard drive prior to installation):

1. [Anaconda](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf) (if Anaconda is too large, mini-conda would also suffice).
2. [Visual Studio Code](https://code.visualstudio.com/Download) (this is a code editor).

**Additions to** *.gitignore*

A number of [additional files](https://github.com/github/gitignore/tree/main/Global) were added to my *.gitignore* prior to running the programmes:

  1. python.gitignore
  2. macOS..gitignore
  3. VisualStudioCode.gitignore
  4. Linux.gitignore
  5. TeX.gitignore
  6. Vim.gitignore
  7. Windows.gitignore

## How to run the Notebook

### Using Visual Studio Code & Anaconda or GitHub Codespaces

1. **Clone the Repository**:

```ruby
   git clone https://github.com/Laura6826/computer_infrastructure_assignments.git
```

2. **Install the required packages**:

For a seamless execution, I would also recommend you have access to the below libraries prior to running the files. The libraries required to run this file (as noted below), can be installed with the following code:

```ruby
pip install -r requirements.txt
```

,or you can manually install each of the libraries below.+

```ruby
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  import seaborn as sns
  import scipy
```

***

### Open the notebook in Visual Studio Code

- Open Visual Studio Code.
- Open the `computer_infrastructure_assignments` folder.
- Open the `weather.ipynb` file.

OR

## Open the repository in Github Codespaces,

- Navigate to your repository on GitHub.
- Click on the `Code` button and select `Open with Codespaces`.
- If you don't have a Codespace set up, create a new one.
- Open a terminal in the Codespace.
- Run the following command.

```ruby
pip install -r requirements.txt
```

- Open the `weather.ipynb` file.

***

## 4. How to get help

I have attached a number of helpful links below, should you wish to extrapolate on any of the methods used within this project.

1. [Anaconda](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf)
1. [Visual Studio Code](https://code.visualstudio.com/Download)
1. [w3schools](https://www.w3schools.com/)
1. [Pandas](https://pandas.pydata.org/)
1. [Numpy](https://numpy.org/)
1. [Matplotlib.py](https://matplotlib.org/)
1. [Seaborn](https://seaborn.pydata.org/)

Additionally, a number of links are embedded within the code, in areas that i found confusing/difficult, that should help should there be any difficulty.

## 5. How to contribute

As this project was created to fulfill an assessment requirement of the module Computer Infrastructure 24-25, as part of the H.Dip in Science in Data Analytics, no contributions will be allowed, in order to comply with ATU Policy on [Plagiarism](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf) and the [Student Code of Conduct](https://www.atu.ie/sites/default/files/2022-08/Student%20Code_Final_August_2022.pdf).

Should you find any errors or have any recommendations , please submit a pull request on Github. or just wish to contact that author, you can do so at <maxwell6826@gmail.com>.

***

## **6. Weekly Tasks**

This is a brief description of the tasks that were to be completed as part of the assessment for Computer Infrastructure 24-25: 8645.

- Task01- Task07 were complete to demonstrate our ability to navigate in terminal format.
- Task08 contains a brief report explaining how you completed Tasks 1 to 7.
- Task09 expanded on what we had previously learned.

## **Task 01** - Create Directory Structure

### **Assignment Instructions:**

Using the command line, create a directory (that is, a folder) named data at the root of your repository. Inside data, create two subdirectories: timestamps and weather.

*[Task 08](weather.ipynb) contains a brief report explaining how you completed Tasks 1 to 7.*

## **Task 02** - Timestamps

### **Assignment Instructions: 02**

Navigate to the data/timestamps directory. Use the date command to output the current date and time, appending the output to a file named now.txt. Make sure to use the >> operator to append (not overwrite) the file. Repeat this step ten times, then use the more command to verify that now.txt has the expected content.

*[Task 08](weather.ipynb) contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 03** - Formatting Timestamps

### **Assignment Instructions: 03**

Run the date command again, but this time format the output using YYYYmmdd_HHMMSS (e.g., 20261114_130003 for 1:00:03 PM on November 14, 2026). Refer to the date man page (using man date) for more formatting options. (Press q to exit the man page). Append the formatted output to a file named formatted.txt.

*[Task 08](weather.ipynb) contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 04** - Creating Timestamped Files

### **Assignment Instructions: 04**

Use the touch command to create an empty file with a name in the YYYYmmdd_HHMMSS.txt format. You can achieve this by embedding your date command in backticks ` into the touch command. You should no longer use redirection (>>) in this step.

*[Task 08](weather.ipynb) contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 05** - Download Todays Weather Data

### **Assignment Instructions: 05**

Change to the data/weather directory. Download the latest weather data for the Athenry weather station from Met Eireann using wget. Use the -O filename option to save the file as weather.json. The data can be found at this URL:
<https://prodapi.metweb.ie/observations/athenry/today>.

*[Task 08](weather.ipynb) contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 06** - Timestamp the Data

### **Assignment Instructions: 06**

Modify the command from Task 5 to save the downloaded file with a timestamped name in the format YYYYmmdd_HHMMSS.json.

*[Task 08](weather.ipynb) contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 07** - Write the Script

### **Assignment Instructions: 07**

Write a bash script called weather.sh in the root of your repository. This script should automate the process from Task 6, saving the weather data to the data/weather directory. Make the script executable and test it by running it.

*[Task 08](weather.ipynb)Task 08 contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 08** - Notebook

### **Assignment Instructions: 08**

Create a notebook called weather.ipynb at the root of your repository. In this notebook, write a brief report explaining how you completed Tasks 1 to 7. Provide short descriptions of the commands used in each task and explain their role in completing the tasks.

Task 08 can be viewed in [weather.ipynb](C:\Users\Laura\OneDrive\ATU_DA\24-25\computer_infrastructure_assignments\weather.ipynb)

***

## **Task 09** - Pandas

### **Assignment Instructions: 09**

In your weather.ipynb notebook, use the pandas function read_json() to load in any one of the weather data files you have downloaded with your script. Examine and summarize the data. Use the information provided data.gov.ie to write a short explanation of what the data set contains.

Task 09 can be viewed in [weather.ipynb](C:\Users\Laura\OneDrive\ATU_DA\24-25\computer_infrastructure_assignments\weather.ipynb)

***

## **Final Project**

The final project required the `weather.sh` file (created as part of Task 07, to down load the daily, hourly weather file, for Athenry, from Met Éireann), to be automatically run at 10am each day, and for the downloaded data to be automatically pushed and saved to a GitHub repository.

### **Project Instructions**

In this project, you will automate your `weather.sh` script to run daily and push the new data to your repository.

1. *Create a GitHub Actions Workflow: In your repository, create a folder called .github/workflows/ (if it doesn't already exist). Inside this folder, create a file called weather-data.yml. This file will define the GitHub Actions workflow.*
1. *Run Daily at 10am: Use the schedule event with 'cron' to set the script to run once a day at 10am. Include also the workflow_dispatch event so you can test the workflow.*
1. *Use a Linux Virtual Machine In the workflow file, specify that a Ubuntu virtual machine should be used to run the action.*
1. *Clone the Repository Have the workflow clone your repository.*
1. *Execute the weather.sh Script Add a step that runs your weather.sh script.*
1. *Commit and Push Changes Back to the Repository Finally, configure the workflow to commit the new weather data and push those changes back to your repository.*

#### **How to run the final project**

1. The final project can be run from my [GitHub respository](https://github.com/Laura6826/computer_infrastructure_assignments/tree/main).
2. Ensure you have followed the instruction above including, downloading the recommended libraries/ or running the `requirements.txt' files in a terminal.
3. Open GitHub Actions, located in the toolbar.

![GitHub Actions](https://github.com/Laura6826/computer_infrastructure_assignments/blob/main/images/projectactions.JPG)

4. Under the heading 'Actions', select, 'Daily `weather.sh` script execution'

![executive weather.sh](https://github.com/Laura6826/computer_infrastructure_assignments/blob/main/images/execution.JPG)

5. Once open, you can manually call the script to run by selecting the green button `Run Workflow`,

![Run workflow](https://github.com/Laura6826/computer_infrastructure_assignments/blob/main/images/runworkflow.JPG)

,or you can allow the script to run and the prescribed time of 9.45am each day.

6. You can access/ check that the data has been downloaded at `data\project`, with my repository.


#### **Updates/ Improvements**

***

- The assigned required us to run the bash script `weather.sh`, previously created in weekly Task 07 and not a modified python file, and,
- The 'work flow' also failed when there was a large call to the Met Éireann site, as more students started to automate their scripts.

The amendments made to make the project more effective/appliable to the project requirements included:

1. Creating a new `weatherdata.yml` file, to call `weather.sh` (and not `weather.py`).

- The data originally downloaded using the python file can be differentiated from the data downloading using the bash script, as the data was downloaded by both scripts using different file names.
- Those downloaded with the .py file have a `csv` extension and the file name in the format `20241124_184726.csv`, 
- but the data downloaded via the bash script has the file extention `.json` and was formatted as follows `20241211_120357_athenry.json`.

2. Update the schedule event on 'cron. from:

- 10am = `'0 10 * * *'`, to
- 9am = `'45 9 * * *'`, to avoid overburdening Met Éireann with the mass requests due to the class all calling for the data at 10am.

3. Amend the `weather.sh`, previously created in weekly Task 07 to save the data in the `project` folder, and not the `weather` folder, as required in Task 07.

### End