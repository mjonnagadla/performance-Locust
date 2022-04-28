# pw-locust

- Make sure you're running python version 3 or above
- In admin powershell run `pip3 install locust`

# Provided some sample examples on python to understand the things

## To run the locust


- In vs code terminal you need to run `locust -f <filename with extension .py>`
- In your browser enter `http://localhost:8089/`
- You need to enter number of users you want to run
- You need to enter spawn rate (number of users started per sec)
- Host URL will be generated automatically and if you're not seeing the host URL enter it manually
- Hit Start swarming

## Alernate way to run the locust in headless mode

- In vs code terminal you need to run `locust -f <filename with extension> -r <spawn rate> -u <number of users> -t <time in secs> --headless --only-summary`
