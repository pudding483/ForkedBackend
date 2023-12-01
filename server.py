from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.settings import Settings
from router import account, shop

app = FastAPI(
    title="NFT API",
    description="NTUT furniture trading API",
    version="0.0.1",
    docs_url=Settings["api_docs"],
    openapi_url=Settings["api_prefix"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account.router, prefix=Settings["api_prefix"])
app.include_router(shop.router, prefix=Settings["api_prefix"])