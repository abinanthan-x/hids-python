import requests
from requests.auth import HTTPBasicAuth
import json

def create_jira_issue(summary, description):
    """
    Function to create a JIRA issue.

    :param summary: The short summary of the issue
    :param description: The detailed description of the issue
    :return: The response from the JIRA API (JSON)
    """
    print(summary)
    print(description)
    # Hardcoded values for email, API token, project, and issue type
    email = "abi.rajendran.ar@gmail.com"  # Your JIRA email
    api_token = "ATATT3xFfGF0-BdK35iQaXAE-287k-i8V3T--CGWM842Sgc0ZPl2MOJlyseMHVDPR9vdNftJo-7vEGOwQPIg3-qiwG69zr-WQtO0bj8F6Anl1NFxL7JGhHQ09tlJRQHP93HvO2cvy5TQABtb5gRLHOb43lmO3xrgEtcrWVW40Smsmw0B0qC-bmQ=6415B827"  # Your JIRA API token
    project_key = "KAN"  # The project key
    issue_type = "Task"  # The type of issue (Bug, Task, etc.)

    # JIRA API URL
    url = "https://abirajendranar.atlassian.net/rest/api/3/issue"

    # Authentication
    auth = HTTPBasicAuth(email, api_token)

    # Headers
    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }

    # Payload with dynamic summary and description, hardcoded email, api_token, project, and issue type
    payload = json.dumps({
    "fields": {
        "project": {
            "key": "KAN"  # Replace with your project key
        },
        "summary": summary,
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": description
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Task"  # Change to the desired issue type
        }
    }
})

    # Send POST request to JIRA API
    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )

    # Return the JSON response from JIRA
    return response.json()
