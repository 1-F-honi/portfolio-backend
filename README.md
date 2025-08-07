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