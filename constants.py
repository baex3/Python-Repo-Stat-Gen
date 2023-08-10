def repoStats(owner:str, name:str, category:str) -> str:
    #owner represents github organization or repo owner
    #name is the name of the github repo
    #category accepts either privileges or activity
    repoOwner = owner
    repoName = name
    #If the category of stats desired is privileges and basic repo info regarding the data retriever and other basics, return this query string
    if category == "privileges":
        gql_privileges = '''
    {
    repository(owner: \"%s\", name: \"%s\") 
    
    {
        createdAt
        updatedAt
        description
        homepageUrl
        nameWithOwner
        pushedAt
        resourcePath
        shortDescriptionHTML
        url
        primaryLanguage {
            color
            id
            name
        }
        languages(first: 10) {
            nodes {
                name
            }
        }
        mentionableUsers(first: 20) {
            edges {
                node {
                    login
                }
            }
        }
        pullRequests(first: 100) {
            nodes {
                author {
                    login
                    resourcePath
                    url
                }
            }
        }
        forkingAllowed
        hasDiscussionsEnabled
        resourcePath
        visibility
        hasIssuesEnabled
        isArchived
        isDisabled
        isLocked
        viewerCanAdminister
        viewerCanCreateProjects
        viewerHasStarred
        viewerPermission

    }
}

'''%(repoOwner, repoName)
        
        return gql_privileges
    
    elif category == "activity":
        gql_activity = '''
    {
    repository(owner: \"%s\", name: \"%s\") 
    {
        forkCount
        stargazerCount
        commitComments {
            totalCount
        }
        discussions {
            totalCount
        }
        watchers {
            totalCount
        }
        projects {
            totalCount
        }
        recentProjects {
            totalCount
        }
        stargazers(first: 10) {
            totalCount
        }
        environments {
            totalCount
        }
        forks {
            totalCount
        }
        issues {
            totalCount
        }
        languages(first: 10) {
            totalCount
        }
        milestones {
            totalCount
        }
        mentionableUsers(first: 20) {
            totalCount
        }
        pullRequests(first: 100) {
            totalCount
        }     
    }
}

'''%(repoOwner, repoName)
                        
        return gql_activity

    else:
        return ValueError
    
def collect_nested_keys(data:dict, keys_list, current_key=""):
    for key, value in data.items():
        new_key = f"{current_key}.{key}" if current_key else key
        if isinstance(value, dict):
            collect_nested_keys(value, keys_list, current_key=new_key)
        else:
            keys_list.append(new_key)
    return keys_list

def collect_nested_values(data:dict, values_list, current_key=""):
    for key, value in data.items():
        new_key = f"{current_key}.{key}" if current_key else key
        if isinstance(value, dict):
            collect_nested_values(value, values_list, current_key=new_key)
        else:
            values_list.append(value)
    return values_list
        
    

#Would normally use this as an environment variable or store in a gitignore file
#Token best set for read-only permissions for public repos, following least privileged practices
gitHubAPItkn = "<insert user token>"
gitHubGraphQLAPI = "https://api.github.com/graphql"
