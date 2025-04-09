# pysolarmanproxy

## Introduction
`pysolarmanproxy` is a small proxy to provide a usual modbus rtu-over-tcp access to a device using the solarman modbus dialect. It uses the [pysolarmanv5](https://github.com/jmccrohan/pysolarmanv5) library for communication with the device.

## Installation
```
pip install git+https://github.com/tlmnb/pysolarmanproxy
```

## Usage

### Command Line
#### Parameters
```
  --server_address TEXT   The IP address of the proxy server (e.g., 127.0.0.1). [required]
  --server_port INTEGER   The port number of the proxy server (e.g., 5020). [required]
  --address TEXT          The IP address of the Solarman device.  [required]
  --port INTEGER          The port number of the Solarman device (e.g., 8899). [required]
  --loggerserial INTEGER  The logger serial number of the Solarman device. [required]
  --slave_id INTEGER      The Modbus slave ID of the Solarman device. Usuall set to 1.  [required]
  --verbose               Enable verbose logging for debugging.
  --help                  Show this message and exit.
```

#### Example
```bash
$ pysolarmanproxy --server_address=localhost \
    --server_port=5020 \
    --address=192.168.10.20 \
    --port=8899 \
    --loggerserial 1234567890 \
    --slave_id 1
```


### Docker Compose
```yaml
pysolarman_proxy:
  image: ghcr.io/tlmnb/pysolarmanproxy:latest
  container_name: pysolarman_proxy
  environment:
    - SOLARMAN_SERVER_ADDRESS=0.0.0.0
    - SOLARMAN_SERVER_PORT=5020
    - SOLARMAN_ADDRESS=192.168.10.99
    - SOLARMAN_PORT=8899
    - SOLARMAN_LOGGERSERIAL=123456780
    - SOLARMAN_SLAVE_ID=1
    - SOLARMAN_VERBOSE=1
  restart: unless-stopped
```
