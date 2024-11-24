# computer_infrastructure_assignments

## Assignments submitted as part of the module Computer Infrastructure 24-25: 8645, Higher Diploma in Science, Data Analytics

## *Author: Laura Lyons*

***

This README file was written using the [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) as a guidance document
***

  &#x26a0;&#xfe0f; **DISCLAIMER**

  Microsoft Co-Pilot was used to generate ideas of the content of the following notebook. That said, the notebook is mainly my own work, as I had to re-work the code the text in generated to meet my own needs.(*The warning icon was sourced from [Stackoverflow](https://stackoverflow.com/questions/50544499/how-to-make-a-styled-markdown-admonition-box-in-a-github-gist)*)

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
    5. [Task 05- Download Today;s Weather Data](#task-05---download-todays-weather-data)
    6. [Task 06- Timestamp the Data](#task-06---timestamp-the-data)
    7. [Task 07- Write the Script](#task-07---write-the-script)
    8. [Task 08- Notebook](#task-08---notebook)
    9. [Task 09- Pandas](#task-09---pandas)

## 1. Introduction

This project was created to fufill an assessment requirement of Computer Infrastructure 24-25: 8645, as part of the H.Dip in Science in Data Analytics.

Each week, following a series of lectures, a task was assigned, to demonstrate both learning and additional reading/research on the topics discussed in the lectures.

This repository is collection of my weekly tasks, including some additional guidance and instruction in how to run each task/program.

***

## 2. The purpose of this project

As noted on the [assignment instructions](https://github.com/ianmcloughlin/2425_computer_infrastructure),

The purpose of the assessment is to ensure students can demonstrate the following:

1. Use, configure, and script in a command line interface environment.
1. Manipulate and move data and code using the command line.
1. Compare commonly available software infrastructures and architectures.
1. Select appropriate infrastructure for a given computational task.

## 3. How to get started

Necessary software

In order to run the included files, you will need to ensure that you have access to the correct softwear. I would recommend downloading the following applications (ensuring sufficent space on your hard drive prior to installation):

1. [Anaconda](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf) (if Anaconda is too large, miniconda would also suffice).
2. [Visual Studio Code](https://code.visualstudio.com/Download) (this is a code editor).

Recommended libraries

For a seamless excutition, I would also recommend you have access to the below libraries prior to running the files:

```ruby
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  import seaborn as sns
  import scipy
```

**Additions to** *.gitignore*

A number of [additional files](https://github.com/github/gitignore/tree/main/Global) were added to my *.gitignore* prior to running the programmes:

  1. python.gitignore
  2. macOS..gitignore
  3. VisualStudioCode.gitignore
  4. Linux.gitignore
  5. TeX.gitignore
  6. Vim.gitignore
  7. Windows.gitignore

## 4. How to get help

I have attached below,a number of helpful links, should you wish to extrapolate on any of the methods used within this project.

1. [Anaconda](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf)
1. [Visual Studio Code](https://code.visualstudio.com/Download)
1. [w3schools](https://www.w3schools.com/)
1. [Pandas](https://pandas.pydata.org/)
1. [Numpy](https://numpy.org/)
1. [Matplotlib.py](https://matplotlib.org/)
1. [Seaborn](https://seaborn.pydata.org/)

Additionally, a number of links are embedded within the code, in areas that i found confussing/difficult, that should help should there be any difficulty.

## 5. How to contribute

As this project was created to fufill an assessment requirement of the Principles of Data Analytics, as part of the H.Dip in Science in Data Analytics, no contributions will be allowed, in order to comply with ATU Policy on [Plagiarism](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf) and the [Student Code of Conduct](https://www.atu.ie/sites/default/files/2022-08/Student%20Code_Final_August_2022.pdf).

Should you find any errors or have any recommendations , please submit a pull request on Github. or just wish to contact that author, you can do so at <maxwell6826@gmail.com>.

***

## **6. Weekly Tasks**

This is a brief description of the tasks that were to be completed as part of the assessment for Computer Infrastructure 24-25: 8645.

- Task01- Task07 were complete to demonstrate our ability ot navigate in terminal format.
- Task08 contains a brief report explaining how you completed Tasks 1 to 7.
- Task09 expanded on what we had previously learned, and 

## **Task 01** - Create Directory Structure

### **Assignment Instructions:**

Using the command line, create a directory (that is, a folder) named data at the root of your repository. Inside data, create two subdirectories: timestamps and weather.

*Task 08 contains a brief report explaining how you completed Tasks 1 to 7.*

## **Task 02** - Timestamps

### **Assignment Instructions: 02**

Navigate to the data/timestamps directory. Use the date command to output the current date and time, appending the output to a file named now.txt. Make sure to use the >> operator to append (not overwrite) the file. Repeat this step ten times, then use the more command to verify that now.txt has the expected content.

*Task 08 contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 03** - Formatting Timestamps

### **Assignment Instructions: 03**

Run the date command again, but this time format the output using YYYYmmdd_HHMMSS (e.g., 20261114_130003 for 1:00:03 PM on November 14, 2026). Refer to the date man page (using man date) for more formatting options. (Press q to exit the man page). Append the formatted output to a file named formatted.txt.

*Task 08 contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 04** - Creating Timestamped Files

### **Assignment Instructions: 04**

Use the touch command to create an empty file with a name in the YYYYmmdd_HHMMSS.txt format. You can achieve this by embedding your date command in backticks ` into the touch command. You should no longer use redirection (>>) in this step.

*Task 08 contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 05** - Download Today;s Weather Data

### **Assignment Instructions: 05**

Change to the data/weather directory. Download the latest weather data for the Athenry weather station from Met Eireann using wget. Use the -O filename option to save the file as weather.json. The data can be found at this URL:
<https://prodapi.metweb.ie/observations/athenry/today>.

*Task 08 contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 06** - Timestamp the Data

### **Assignment Instructions: 06**

Modify the command from Task 5 to save the downloaded file with a timestamped name in the format YYYYmmdd_HHMMSS.json.

*Task 08 contains a brief report explaining how you completed Tasks 1 to 7.*

***

## **Task 07** - Write the Script

### **Assignment Instructions: 07**

Write a bash script called weather.sh in the root of your repository. This script should automate the process from Task 6, saving the weather data to the data/weather directory. Make the script executable and test it by running it.

*Task 08 contains a brief report explaining how you completed Tasks 1 to 7.*`

***

## **Task 08** - Notebook

### **Assignment Instructions: 08**

Create a notebook called weather.ipynb at the root of your repository. In this notebook, write a brief report explaining how you completed Tasks 1 to 7. Provide short descriptions of the commands used in each task and explain their role in completing the tasks.

Task 08 can be viewed in[weather.ipynb](C:\Users\Laura\OneDrive\ATU_DA\24-25\computer_infrastructure_assignments\weather.ipynb)

***

## **Task 09** - Pandas

### **Assignment Instructions: 09**

In your weather.ipynb notebook, use the pandas function read_json() to load in any one of the weather data files you have downloaded with your script. Examine and summarize the data. Use the information provided data.gov.ie to write a short explanation of what the data set contains.

**My notes:**

**Associated Code:**

```ruby

```

***

### End
