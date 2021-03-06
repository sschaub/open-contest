# OpenContest
OpenContest is an open-source programming contest management system written in Python. It allows judges to write problems and contest participants to submit solutions to those problems. 

## Basic Usage
To run OpenContest,
1. Install [Docker](https://store.docker.com/search?type=edition&offering=community) on a Unix-based machine and start the daemon
2. Run `docker pull nathantheinventor/open-contest`
3. Create a directory to hold the contest database (ex. mkdir ~/db)
4. Run `docker run -v /tmp:/tmp -v [db-path]:/db -v /var/run/docker.sock:/var/run/docker.sock -p 0.0.0.0:8000:8000/tcp nathantheinventor/open-contest`, substituting the contest database location for `[db-path]`.
5. Navigate to [localhost:8000](http://localhost:8000) and enter `Admin` as the username and enter the password generated by OpenContest (visible in the command prompt)
6. Create problems, a contest to hold them, and users to participate

For example, run the following
```
$> sudo apt install docker.io
Reading package lists... Done
Building dependency tree
Reading state information... Done
. . . 

$> docker pull nathantheinventor/open-contest
Using default tag: latest
latest: Pulling from nathantheinventor/open-contest
Digest: sha256:9f65996f196f8780956cd08b9ed53d84f4e26c5e8456fe50c6487e8a5f316948
Status: Image is up to date for nathantheinventor/open-contest:latest

$> docker run -v /tmp:/tmp -v ~/db:/db -v /var/run/docker.sock:/var/run/docker.sock -p 0.0.0.0:
8000:8000/tcp nathantheinventor/open-contest
INFO:root:saving Admin
INFO:root:Admin username is 'Admin'
INFO:root:Admin password is 'presently description kirk died'
INFO:root:Starting server...

```

## Detailed Usage
OpenContest runs inside a Docker container and starts other containers on the host machine to run submissions. The explanation for the Docker flags used above is shown below:
```bash
docker run
    -v /tmp:/tmp # Maps the /tmp directory on the Docker image to the /tmp directory on the real machine
                 # This is needed for running the submitted code, since submissions are processed
                 # in the /tmp directory.
    -v /<db-path>:/db # Maps the path that you want to hold the database on the physical machine
                      # to the /db directory on the container.
                      # Allows the database to persist between runs of the container.
    -v /var/run/docker.sock:/var/run/docker.sock # Maps the Docker daemon socket to the image,
                                                 # allowing OpenContest to run submissions
                                                 # in Docker containers.
    -p 0.0.0.0:8000:8000/tcp # Maps port 8000 inside the container to port 8000 outside the container.
                             # You can change the IP so that OpenContest listens only on a particular
                             # network interface, and you can also change the port 
                             # on which OpenContest listens.
    nathantheinventor/open-contest # DockerHub address of the production version
    "<Yourname>" # The name of the first admin user. This user will be given admin rights,
                 # and a password will be generated and printed at the beginning of the log.
    8000 # Port number inside the container.
```

## How to Create a Problem
To create a problem, follow these steps:
1. Log in to OpenContest at localhost:8000 with the username and password provided when you started the server.
2. Choose *Setup* in the menu.
![](https://contests-dev.nathantheinventor.com/images/setup.png)
3. Choose *Problems*.
![](https://contests-dev.nathantheinventor.com/images/problems.png)
4. Click *Create Problem*.
![](https://contests-dev.nathantheinventor.com/images/createproblem.png)
5. Enter the details of the problem. You may use Markdown formatting for the Problem Statement, Input Format, Output Format, and Constraints.  
![](https://contests-dev.nathantheinventor.com/images/problemdata.png)
    **Note**: The Description is the text shown under the problem title in the list of all problems.
6. After saving the problem details, create test data.
    - Click *Create Test Data*
![](https://contests-dev.nathantheinventor.com/images/createtestdata.png)
    - Enter input and output data
![](https://contests-dev.nathantheinventor.com/images/testio.png)
    - Click *Add Test Data*.
![](https://contests-dev.nathantheinventor.com/images/addtestdata.png)
7. After creating the test data, set the number of sample cases and save the problem.
![](https://contests-dev.nathantheinventor.com/images/samplecases.png)

## Contest Information
OpenContest allows you to create multiple contests that run at different times. The most common use case for this feature is to allow for a practice round before an actual contest. To create a contest, go to Setup > Contest > Create Contest and enter the contest details. 
![](https://contests-dev.nathantheinventor.com/images/contestdetails.png)

After creating the contest, you can choose problems to go into the contest.
![](https://contests-dev.nathantheinventor.com/images/chooseproblem.png)

Before the contest begins, the home page will show a countdown to the beginning of the contest.
![](https://contests-dev.nathantheinventor.com/images/countdown.png)
During the contest, the home page will show a list of problems in the contest.
![](https://contests-dev.nathantheinventor.com/images/homepageproblems.png)
After the contest ends, the final leaderboard for the most recent contest will be visible.
![](https://contests-dev.nathantheinventor.com/images/leaderboard.png)

## How To Print a Problem
OpenContest formats problems for printing so that you can print and distribute problem statement packets to contestants. To print a problem, go to the edit page for the problem, click *View Problem*, and print the page with Ctrl+P.
![](https://contests-dev.nathantheinventor.com/images/printproblem.png)

## How To Print the User Login Information
From the user list page, you can print the page with Ctrl+P for a list of usernames and passwords. You can then cut the paper and deliver these sheets to the contestants.
![](https://contests-dev.nathantheinventor.com/images/printusers.png)

## Development Information
See the [Wiki](https://github.com/nathantheinventor/open-contest/wiki) for more information about how OpenContest works and how to add features.
