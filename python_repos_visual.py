#python_repos_visual.py
from plotly.graph_objs import Bar
from plotly import offline
import requests

#Make an api call and store the response
url = ('https://api.github.com/search'
'/repositories?q=language:python&sort=stars')
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Make visualization.
data = [{
    'type': 'bar',
    'x': repo_names,
    'y:': stars,
}]

my_layout = {
    'title': 'Most starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
#print(f":Total repositories: {response_dict['total_count']}")

#Explore information about the repositories.

#print(f"Repositories returned: {len(repo_dicts)}")

#Examine the first repository.
#repo_dict = repo_dicts[0]

#Process results

#print("\nSelected information about each repository:")

    

