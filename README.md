# Github Repo Stat Generator


This repo is a made to the display a means for tracking repo activity. The scope for this project is to gather data with publicly available repos and display them in a digestible manner for both technical and non-technical audiences.

## How to build and run program
The constants.py program will need to be updated with your valid API token for GitHub in order to not be automatically throttled by the GitHub GraphQL API. The program can be run on any terminal that has python3 installed or as a bash script. These will vary based on OS but the order is:

1. install python3
2. install pip
3. install requests module
4. install matplotlib
5. navigate to the directory where both files are together
6. type 'python3 productivity.py'

Alternatively the program will run if you download the files after step 1-4 and double-click on 'productivity.py'

7. Verify the Github Actions workflow by clicking 'Actions' at the top of the repo

### Technical Design Aspects:
This program utilizes python's requests and matplotlib libraries in order to take the API calls and make them visuals, and within that I had to use a recursive function in order to get the key.inner_key.inner_inner_key nomenclature separated for the graph generation. It also was aided using Postman to help with GitHub's GraphQL instrospection and for modifying the query. All of the code was developed using VScode with security and defensive programming principles in mind.




