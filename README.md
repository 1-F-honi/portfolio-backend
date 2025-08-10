### Manual Deploy

create sam project
```shell
sam init --name portfolio-backend \
  --runtime python3.11 \
  --apps-template hello-world \
  --dependency-manager pip
```

debug
```shell
sam local start-api --debug-port 5890
```

### Setup Env

#### pipx openai install

```shell
brew install pipx
pipx ensurepath
pipx install openai
openai --help
```


#### path setting

```shell
echo 'export PATH=$PATH:$HOME/.local/bin' >> ~/.zshrc
source ~/.zshrc
```

#### add install in pipx

```shell
pipx runpip openai install 'openai[datalib]'
```

