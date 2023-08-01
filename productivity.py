import requests
import constants
import json
import matplotlib.pyplot as plt

print("Welcome to the Productivity Analyzer! \nYou can visualize the effect of your organization's increased productivity due to your investment in tooling.\nYour options for the type of stats to view are either 'privileges' or 'activity'. The 'privileges' stats type will reveal general information and verify settings on the organization's repo to make sure there are appropriat permissions to measure engagement and productivity.\nThe 'activity' type will focus on measurable metrics with some metadata around the repo.\nEnjoy your statistical endeavors!")

# tmpOwner = input("Please enter the github organization or repo owner's name: ")
# tmpRepo = input("Please enter the name of the repo you want to analyze: ")
# while True:
#     tmpStatsType = input("What type of stats are you interested in? Please enter either productivity or activity: ")
#     if tmpStatsType == 'productivity' or tmpStatsType == 'activity':
#        break
#     else:
#         print("Please enter a valid type of statistics to view.")

#Take input on the repo owner, the name of the repo, and the type of stats you want to see.
#Get activity data on the company's repo using REST, this call is not available on Github's GraphQL API
#Could use this in future version to see who the main people who been making commits to public repo from another angle. This takes a hit in efficiency due to pulling irrelevant stats
#responseREST = requests.get("https://api.github.com/repos/jenkinsci/ec2-plugin/activity")

'''
Get specific data on the specific stats of the repo for analyzing usage of the tools made available using GraphQL for a more efficient API call.
Get information for objects about the organization repo. Get these for accuracy of data over time and to make sure certain permissions are still active for pulled data so as to not determine stats based off of blocked permissions:
    createdAt, forkingAllowed, hasDiscussionsEnabled, etc. 
'''
serviceKey = constants.gitHubAPItkn

#Fetch the stats that are ensuring accuracy of data
#repoStats(repoOwner, repoName, {'privileges' | 'activity'})
statsForAccuracy = constants.repoStats("jenkinsci", "ec2-plugin", "privileges")
if statsForAccuracy != ValueError:
    responseGraphQL = requests.post(url=constants.gitHubGraphQLAPI, json={"query": statsForAccuracy}, headers={"Authorization": "Bearer " + serviceKey})
    print(f"GraphQL response status code: {responseGraphQL.status_code}")
    #Manipulate JSON from GraphQL Response, remove problematic Values in JSON response and replace them, then load the resulting string into JSON object and make it a pretty report (in json at least) 
    tmp = str(responseGraphQL.json())
    tmp = tmp.replace("\'", "\"")
    tmp = tmp.replace("None", "null")
    tmp = tmp.replace("True", "true")
    tmp = tmp.replace("False", "false")
    dictionary = json.loads(tmp)
    responseGraphQL = json.dumps(dictionary, indent=2)
    print(responseGraphQL)
else:
    print("Please enter a valid input. The arguments to assess repo metricsa are 3 strings (Repo Owner, Repo Name, and either 'privileges' for verifying accuracy or 'activity' for contributor stats)")

#Fetch stats to measure productivity of contributors
statsForProductivity = constants.repoStats("jenkinsci", "ec2-plugin", "activity")
if statsForProductivity != ValueError:
    responseGraphQL = requests.post(url=constants.gitHubGraphQLAPI, json={"query": statsForProductivity}, headers={"Authorization": "Bearer " + serviceKey})
    print(f"GraphQL response status code: {responseGraphQL.status_code}")
    #Replace incompatible characters in GraphQL response json object
    tmp = str(responseGraphQL.json())
    tmp = tmp.replace("\'", "\"")
    tmp = tmp.replace("None", "null")
    dictionary = json.loads(tmp)
    responseGraphQL = json.dumps(dictionary, indent=2)
    #Produce json viewable report of graph components
    print(responseGraphQL)
    #initialize array for bar graph for easy readability for non-technical customers
    xAxis = []
    yAxis = []
    #extract the nested key, value pairs from GraphQL response
    xAxis = constants.collect_nested_keys(dictionary, xAxis)
    yAxis = constants.collect_nested_values(dictionary, yAxis)
    #Plot the bar graph with data from API call
    plt.figure(figsize=(100, 20))
    plt.grid(axis='x')
    plt.barh(xAxis, yAxis, height=0.2, color='maroon')
    # Add labels to bar graph
    plt.xlabel('Total Count')
    plt.ylabel('Repo Stats')
    plt.title('Developer Productivity', loc='left')
    #Keep graph open until
    plt.show(block=True)
else:
    print("Oops! There was an error along the way.\nHints: The arguments to assess repo metricsa are 3 words \(Repo Owner, Repo Name, and either 'privileges' for verifying accuracy or 'activity' for contributor stats)")

