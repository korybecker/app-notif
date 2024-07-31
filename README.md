# job application notifier

**Sends email notification 1 week after job application**
*Disclaimer: Tutorial for Unix based systems*

## How to use

### 1. Clone this repository in a server of your choosing (e.g., EC2)
 `git clone git@github.com:korybecker/app-notif.git`

### 2. Install Python and start Python virtual environment
  `sudo apt install python3 python3-pip`
  `python3 -m venv venv`
  `source venv/bin/activate`

### 3. Install requirements
`pip install -r requirements.txt`

### 4.  Create .env file and add environment variables
`SMTP_SERVER=<SMTP  server  of  your  choosing>`
`SMTP_PORT=587`
`FROM_EMAIL_ADDRESS=<Email from SMTP server>`
`FROM_EMAIL_PASSWORD=<Password of email from SMTP server>`
`TO_EMAIL_ADDRESS=<Address  you  want  notifications  sent  to>`

### 5. Create database
`python3 create_db.py`

### 6. Schedule cron job
1. Open crontab
`crontab -e`
2. Add command at the bottom of the file
*Runs send_notif.py every day at 9AM*
`0 0 * * * /bin/bash -c 'source /path/to/venv/bin/activate && python /path/to/send_notif.py'`


### 7. Add applications
`python3 add_app.py <company> <position> <date_applied> <job_url>`
