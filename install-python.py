sudo apt update -y

sudo apt install python3 python3-pip -y

python3 --version

#set  python3 as default

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo update-alternatives --config python
