import httpx


def create_httpx_client() -> httpx.AsyncClient:
    timeout = httpx.Timeout(timeout=10)
    return httpx.AsyncClient(timeout=timeout, http2=True)
