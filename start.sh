if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning Repo, Please Wait..."
  git clone -b master https://github.com/Naveen-TG/Masterolic.git /Masterolic
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Masterolic
fi
cd /Masterolic
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
