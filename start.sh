if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning Repo, Please Wait..."
  git clone -b master https://github.com/Naveen-TG/Rashmika.git /Rashmika
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Rashmika
fi
cd /Rashmika
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
