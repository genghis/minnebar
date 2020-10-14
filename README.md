# Zappa / Flask Minnebar Demo

## Before Starting
 * Create or be a member of a Slack Workspace (https://slack.com/create)
 * Create AWS account (https://aws.amazon.com/free)
 * Download and install Python3 (https://www.python.org/downloads/)
 * Install AWS CLI
   * Generally (https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
   * Specific commands for Mac:

   `curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"`
   
   `sudo installer -pkg AWSCLIV2.pkg -target /`

## Python stuff during the talk
 * Create Credentials (https://console.aws.amazon.com/iam/home?region=us-east-2#/security_credentials)
   * Access keys (access key ID and secret access key) -> Create New Access Key
 * Install Credentials (`aws configure`)
 * Create Python virtual environment (`python3 -m venv ./`)
 * Get into that virtual environment (`source ./bin/activate`)

Write your code!!

 * Install Zappa (`pip3 install zappa`)
 * Install other dependencies
   * `pip3 install requests`
   * `pip3 install flask`
 * Comment out slack specific code, add a print or something to verify payload, save as `testing.py`
 * Make sure the app works
   * `export FLASK_APP=testing.py`
   * `flask run`
 * Open a new terminal, throw a curl command at it
   * `curl -d 'response_url=OhHai' http://127.0.0.1:5000`
 * Employ Zappa Sorcery (`zappa init`)
   * Name environment 'prod'
   * If you used my link above to create your credentials, set region to `us-east-2`
   * Everything else default
 * DEPLOY! (`zappa deploy prod`)
 * COPY AND SAVE THE URL WHEN IT'S SUCCESSFUL

## Slack app nonsense during the talk
 * Create the Slack App (https://api.slack.com/apps)
   * `Create an App` -> Name It -> `Create App`
 * Click `Slash Commands` under `Features` on the left
 * Click `Create New Command`
 * Name your command, add the URL Zappa you saved earlier, put in a brief description, and click `Save`
 * Click `Install App` under `Settings` on the left
 * Click `Install App to Workspace`
 * Click `Allow`
 * Go to Slack and type in your command
 * Brush. That. Dirt off your shoulder.

## Notes
 * You can find a demonstration slack payload in the file `payloads/slackpayload`.
 * You can find a demonstration payload from my fake Taylor Swift endpoint in the file `payloads/endpointpayload`.
 * You can find the ugly ugly code for that endpoint in `endpoint/swiftserver.py`.
 * The file `skeleton.py` is a minimal bit of code you can use as a template for your own app. It's not technically the least amount of code necessary, but close and it's readable.
 * The file `taylorswift.py` is a heavily commented version of the code we walk through in the presentation, while `taylorswift_clean.py` is the code I actually use on-screen (since I'm there to talk, here's hoping the comments are unnecessary).
 * The file `testing.py` is a slightly modified version of the app that prints the appropriate results instead of trying to post them back to Slack. 