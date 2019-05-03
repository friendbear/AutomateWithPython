import re

# sub
agent_name_regex = re.compile(r'Agent (\w)\w*')
print(agent_name_regex.sub(r'\1*****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
