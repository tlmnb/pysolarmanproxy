import logging
import socketserver
from typing import Any, Tuple

import click
from pysolarmanv5 import PySolarmanV5

logging.basicConfig()
logger = logging.getLogger("pysolarmanproxy")


class ModbusProxyHandler(socketserver.StreamRequestHandler):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def handle(self) -> None:
        logger.debug(f"client connected: {self.client_address[0]}:{self.client_address[1]}")
        request: bytes = self.request.recv(1024)
        logger.debug("request: {data}".format(data=" ".join(f"{byte:02X}" for byte in request)))
        response = self.server.solarman.send_raw_modbus_frame(request)
        self.wfile.write(response)


class ModbusProxyServer(socketserver.TCPServer):

    def __init__(
        self,
        server_address: Tuple[str, int],
        RequestHandlerClass: socketserver.BaseRequestHandler,
        solarman: PySolarmanV5,
        bind_and_activate: bool = True,
    ) -> None:
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        self._solarman = solarman

    def finish_request(self, request, client_address) -> None:
        self.RequestHandlerClass(request, client_address, self)

    @property
    def solarman(self):
        return self._solarman


@click.command()
@click.option("--server_address", required=True, type=str)
@click.option("--server_port", required=True, type=int)
@click.option("--address", required=True, type=str)
@click.option("--port", required=True, type=int)
@click.option("--loggerserial", required=True, type=int)
@click.option("--slave_id", required=True, type=int)
@click.option("--verbose", is_flag=True, default=False, type=bool)
def run(
    server_address: str,
    server_port: int,
    address: str,
    port: int,
    loggerserial: int,
    slave_id: int,
    verbose: bool,
):
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    solarman = PySolarmanV5(
        address, loggerserial, port=port, mb_slave_id=slave_id, verbose=verbose, auto_reconnect=True, logger=logger
    )
    with ModbusProxyServer((server_address, server_port), ModbusProxyHandler, solarman) as server:
        try:
            logger.info("starting server")
            server.serve_forever()
        finally:
            server.server_close()

def main():
    run(auto_envvar_prefix="SOLARMAN")

if __name__ == "__main__":
    main()
