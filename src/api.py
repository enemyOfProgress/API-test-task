from fastapi import FastAPI
from src.workflow.router import router as wf_routers
from src.node.router import router as n_routers

app = FastAPI()

app.include_router(wf_routers)
app.include_router(n_routers)
