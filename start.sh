if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Agsbotsyt/Wednesday.git /WednesdayBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /WednesdayBot
fi
cd /Wednesday
pip3 install -U -r requirements.txt
echo "Starting Wednesday...."
python3 bot.py


