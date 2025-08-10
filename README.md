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

### How To Fine tune

#### data into data.jsonl
reference by data.jsonl

#### fmt check data.jsonl
it's collect fmt if it returns empty
```shell
jq empty data.jsonl
```

#### data.jsonl upload to open ai api
it's collect upload if it returns **id**
```shell
./fine_tunes_data_upload.sh
```

#### 