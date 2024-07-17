from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def root():
    return {
            "hostname": "server1",
            "datetime": "YYMMDDHHmm",
            "version": "version"
            }