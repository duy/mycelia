WORKON_HOME=/home/julia/pinax-development2
PROJECT_ROOT=/home/julia/pinax-development2/mycelia

# activate virtual environment
source $WORKON_HOME/pinax-env/bin/activate

cd $PROJECT_ROOT
python manage.py send_mail >> $PROJECT_ROOT/logs/cron_mail.log 2>&1
