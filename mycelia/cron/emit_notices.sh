WORKON_HOME=/home/user/virtualenvs
PROJECT_ROOT=/path/to/project

# activate virtual environment
source $WORKON_HOME/pinax-env/bin/activate

cd $PROJECT_ROOT
python manage.py emit_notices >> $PROJECT_ROOT/logs/cron_notices.log 2>&1
