import random
import MessageTemplates

def getRandomTemplate():
    return random.choice(MessageTemplates.messageTemplates)

def getMessage(assignee,repo_name,issue_number,issue_url):
    template=getRandomTemplate()
    message=template.replace("assignee",assignee)
    message=message.replace("repo_name",repo_name)
    message=message.replace("issue_number",issue_number)
    message=message.replace("issue_url",issue_url)
    return message
