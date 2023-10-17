import edgedb

from dotenv import load_dotenv
import os

load_dotenv()

client = edgedb.create_async_client()

EDGEDB_HOST=os.getenv('EDGEDB_HOST')
EDGEDB_PORT=os.getenv('EDGEDB_PORT')
EDGEDB_USER=os.getenv('EDGEDB_USER')
EDGEDB_PASSWORD=os.getenv('EDGEDB_PASSWORD')
EDGEDB_DB=os.getenv('EDGEDB_DB')
EDGEDB_TLS_CA=os.getenv('EDGEDB_TLS_CA')


async def setup_edgedb(app):
    global client
    client = edgedb.create_async_client(
        host=EDGEDB_HOST,
        port=EDGEDB_PORT,
        user=EDGEDB_USER,
        password=EDGEDB_PASSWORD,
        database=EDGEDB_DB,
        tls_ca=EDGEDB_TLS_CA,
        tls_security="default",
    )
    await client.ensure_connected()
    return client


async def shutdown_edgedb(app):
    await client.aclose()
