#!/bin/bash

RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
BLUE=$(tput setaf 4)
RESET=$(tput sgr0)

AMASS_VERSION=3.8.2


logo(){}



echo ""
echo "${GREEN} Tools created by the best people in the InfoSec Community ${RESET}"
echo "${GREEN}                   Thanks to everyone!                     ${RESET}"
echo ""


echo "${GREEN} [+] Updating and installing dependencies ${RESET}"
echo ""

sudo apt-get -y update
sudo apt-get -y upgrade

sudo add-apt-repository -y ppa:apt-fast/stable < /dev/null
sudo echo debconf apt-fast/maxdownloads string 16 | debconf-set-selections
sudo echo debconf apt-fast/dlflag boolean true | debconf-set-selections
sudo echo debconf apt-fast/aptmanager string apt-get | debconf-set-selections
sudo apt install -y apt-fast

sudo apt-fast install -y apt-transport-https
sudo apt-fast install -y libcurl4-openssl-dev
sudo apt-fast install -y libssl-dev
sudo apt-fast install -y jq
sudo apt-fast install -y ruby-full
sudo apt-fast install -y libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby-dev build-essential libgmp-dev zlib1g-dev
sudo apt-fast install -y build-essential libssl-dev libffi-dev python-dev
sudo apt-fast install -y python-setuptools
sudo apt-fast install -y libldns-dev
sudo apt-fast install -y python3-pip
sudo apt-fast install -y python-dnspython
sudo apt-fast install -y git
sudo apt-fast install -y npm
sudo apt-fast install -y nmap phantomjs 
sudo apt-fast install -y gem
sudo apt-fast install -y perl 
sudo apt-fast install -y parallel
pip3 install jsbeautifier
echo ""
echo ""
sar 1 1 >/dev/null

#Setting shell functions/aliases
echo "${GREEN} [+] Setting bash_profile aliases ${RESET}"
curl https://raw.githubusercontent.com/unethicalnoob/aliases/master/bashprofile > ~/.bash_profile
echo "${BLUE} If it doesn't work, set it manually ${RESET}"
echo ""
echo ""
sar 1 1 >/dev/null 

echo "${GREEN} [+] Installing Golang ${RESET}"
if [ ! -f /usr/bin/go ];then
    cd ~
    wget -q -O - https://raw.githubusercontent.com/canha/golang-tools-install-script/master/goinstall.sh | bash
	export GOROOT=$HOME/.go
	export PATH=$GOROOT/bin:$PATH
	export GOPATH=$HOME/go
    echo 'export GOROOT=$HOME/.go' >> ~/.bash_profile
	
	echo 'export GOPATH=$HOME/go'	>> ~/.bash_profile			
	echo 'export PATH=$GOPATH/bin:$GOROOT/bin:$PATH' >> ~/.bash_profile
    source ~/.bash_profile 
else 
    echo "${BLUE} Golang is already installed${RESET}"
fi
    break
echo""
echo "${BLUE} Done Install Golang ${RESET}"
echo ""
echo ""
sar 1 1 >/dev/null

#Installing tools

echo "${RED} #################### ${RESET}"
echo "${RED} # Installing tools # ${RESET}"
echo "${RED} #################### ${RESET}"


echo "${GREEN} #### Basic Tools #### ${RESET}"

echo "${BLUE} installing nuclei${RESET}"
go get -u github.com/projectdiscovery/nuclei/v2/cmd/nuclei
echo "${BLUE} done${RESET}"
echo ""

echo "${GREEN} #### Downloading wordlists #### ${RESET}"
git clone  https://github.com/projectdiscovery/nuclei-templates.git ~/tools/nuclei-templates

echo "${GREEN} #### Downloading wordlists #### ${RESET}"
git clone  https://github.com/medbsq/vps.git ~/vps
sar 1 1 >/dev/null




echo "${GREEN} #### Installing tomnomnom tools #### ${RESET}"
echo "${GREEN}   check out his other tools as well  ${RESET}"

echo "${BLUE} installing meg${RESET}"
go get -u github.com/tomnomnom/anew
echo "${BLUE} done${RESET}"
echo ""



echo "${BLUE} installing meg${RESET}"
go get -u github.com/tomnomnom/gron
echo "${BLUE} done${RESET}"
echo ""


echo "${BLUE} installing assetfinder${RESET}"
go get -u github.com/tomnomnom/assetfinder
echo "${BLUE} done${RESET}"
echo ""

echo "${BLUE} installing waybackurls${RESET}"
go get -u github.com/tomnomnom/waybackurls
echo "${BLUE} done${RESET}"
echo ""

echo "${BLUE} installing gf${RESET}"
go get -u github.com/tomnomnom/gf
echo "${BLUE} done${RESET}"
echo ""

echo "${BLUE} installing httprobe${RESET}"
go get -u github.com/tomnomnom/httprobe
echo "${BLUE} done${RESET}"
echo ""
 


echo "${BLUE} installing unfurl${RESET}"
go get -u github.com/tomnomnom/unfurl
echo "${BLUE} done${RESET}"
echo ""

echo "${BLUE} installing kxss ${RESET}"
go get -u github.com/tomnomnom/hacks/kxss
echo "${BLUE} done${RESET}"
echo ""

go get -u github.com/tomnomnom/qsreplace
echo "${BLUE} done${RESET}"
echo ""
sar 1 1 >/dev/null




echo "${BLUE} installing amass${RESET}"
cd ~ && echo -e "Downloading amass version ${AMASS_VERSION} ..." && wget -q https://github.com/OWASP/Amass/releases/download/v${AMASS_VERSION}/amass_linux_amd64.zip && unzip amass_linux_amd64.zip && mv amass_linux_amd64/amass /usr/bin/

cd ~ && rm -rf amass_linux_amd64* amass_linux_amd64.zip*
echo "${BLUE} done${RESET}"
echo ""
unzip -q temp.zip &&




echo "${GREEN} #### Installing  projectdiscovery tools #### ${RESET}"


echo installing subfinder${RESET}"
go get -u github.com/projectdiscovery/subfinder/cmd/subfinder
echo "${BLUE} done${RESET}"
echo ""

echo "${BLUE} installing httpx${RESET}"
go get -u github.com/projectdiscovery/httpx/cmd/httpx
echo "${BLUE} done${RESET}"
echo ""

echo "${BLUE} installing shuffledns${RESET}"
go get -u github.com/projectdiscovery/shuffledns/cmd/shuffledns
echo "${BLUE} done${RESET}"
echo ""

echo "${BLUE} installing chaos-client${RESET}"
go get -u github.com/projectdiscovery/chaos-client/cmd/chaos
echo "${BLUE} done${RESET}"
echo ""
sar 1 1 >/dev/null

