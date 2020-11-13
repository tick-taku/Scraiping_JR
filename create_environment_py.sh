#!/usr/bin/env bash

# pyenv を github からクローン
sudo yum install git -y
git clone https://github.com/yyuu/pyenv.git ~/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile

pyenv -v

# 依存関係のインストール
sudo yum install gcc zlib-devel bzip2 bzip2-devel readline readline-devel sqlite sqlite-devel openssl openssl-devel -y

echo ""
read -p "install python: " version
pyenv install ${version}

pyenv global ${version}
pyenv rehash

python --version
