# Developer_Productivity_proj
GResearch Challenge - 

This repo is a response to the need for tracking how the different tools made available to the internal developer community effects productivity and is meant to provide the data necessary to draw proper conclusions and is a starting point. The scope for this project is to gather data with publicly available repos and display them in a digestible manner for both technical and non-technical audiences.

## How to build and run program
The program can be run on any terminal that has python3 installed or as a bash script. These will vary based on OS but the order is:

1. install python3
2. install pip
3. install requests module
4. install matplotlib
5. navigate to the directory where both files are together
6. type 'python3 productivity.py'

Alternatively the program will run if you download the files after step 1-4 and double-click on 'productivity.py'

7. Verify the Github Actions workflow by clicking 'Actions' at the top of the repo

## How can the data be efficitently collected?
I was first stumped by the general question of what constitutes productivity and how would you measure that for a developer. My first thought was to brainstorm with my wife, who is a manager who actually reviews metrics for her employees, so I figured she would have some insight. After talking to her, she described how her company generally generates metrics, by looking at certain objective indicators of productivity such as call time, tasks completed, and other things that are givven to them in a daily spreadsheet. After I was more clear about indicators, the rest was history. I thought about efficiently gathering the data fairly briefly, and immediately thought APIs, either REST or GraphQL. I re-read the prompt and queried the github API both ways, aand of course GraphQL is known for being the more efficient of the two if you want specific data and not to return everything the API has to offer at that endpoint, so I decided GraphQL would be best for this exercise. The only drawback is that the REST API on github seems to offer more data with a simpler query, but I was able to get several relevant indicators using GraphQL without adding fluff, though the exact equivalent of the REST call does not appear to be available yet (if there is even plans for feature parity). 

As I developed my query, I had to take in security considerations as it became clear to me what I needed to do. For queries I generated a temporary token for use on the challenge which is read-only for public-repos and valid for 7 days.

### Future Iterations:
I currently have the data collect various pieces of incoformation such as issues. forks, stargazers (bookmarkings), discussions, etc. I wouldn't really be able to increase the efficiency of the call due to not finding the appropriate query in Github's GraphQL schema, but I would integrate key' values from the REST API call to isolate the contributions of individual engineers/contributors. A simple API call using requests.get("https://api.github.com/repos/jenkinsci/ec2-plugin/activity") returns results for all of the contributors in the repo, including key stats such as commits, while the GraphQL call blocks calls for the contributors object for repos you are not on as an admin or collaborator. Assuming the actual repo is my organization's I would be able to access that data on the repo and generate reports for each individual engineer even using GraphQL, and include every relevant metric. I would also be able to track the dates individual contributors made contributions via their last commit etc. In production environment I would also not include any token in the script and utilize secrets management and environment variables.

## How do you ensure accuracy of data over time?
To ensure the accuracy of the data over time I figured the best way would be to ensure that the conclusions are being drawn from reliable data, so this can be verified by checking wether the appropriate permissions are in place by the rep admin in order to be able to count on the data being generated. I do this by implementing a repoStats function that accepts either an input of 'privileges' or 'activity' to determine whether the query is just to see the permissions and metadata on the repo or activity of the repo respectively, for drawing coonclusions as to whether the organization's increase in tools had the desired effect on the repo's productivity. That way if a forkCount is always returning 0, for example, one can use the 'privileges' input to see if forks are even allowed on the repo, and if not the admin can make sure to enable it. In addition in a future iteration, I would separate the 'privileges' API call into two: 'privileges' and 'metadata'

### Future Iterations:
The current program pulls this information at the time of request, and on Github Actions I have the program running once a day everyday at 12AM, but a future much more robust implementation could potentially leverage Github Actions to take the data and do some comparison over time of each metric, and saving them as JSON outputs to a file to be used to create another graph to plot the trend of the data over a period of time, or output into an Excel spreadsheet.

## . What you can do to make the output useable by an audience of non-technical consumers. What would make a viable MVP?
For this i immediately thought graphs and charts, so I generated a chart of the data I was able to pull.

### Future Iterations:
I would add number labels to the value of the chart to show the exact value of the metric. The privileges API call outputs the primary languages in use in the repo, and since we are tracking both productivity and usage of our new tools, I would also generate a pie chart for the languages and tools being added over time.

### Technical Design Aspects:
I utilized python's requests and matplotlib libraries in order to take the API calls and make them visuals, and within that I had to use a recursive function in order to get the key.inner_key.inner_inner_key nomenclature separated for the graph generation. I utilized Postman to help me with GitHub's GraphQL instrospection and modified the query. All of the code was developed using VScode with security and defensive programming principles in mind.




