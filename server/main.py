from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import uvicorn
from socket_manager import manager

import json
import requests

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def search_awards(params):
    clean = {}
    for key in params.keys():
        if params[key] != "":
            clean[key] = params[key]
    r = requests.get('http://api.nsf.gov/services/v1/awards.json', params=clean)
    response = r.json()
    if isinstance(response, dict):
        return json.dumps(response)
    else:
        return json.dumps({"error": "Unexpected response format", "data": response})


@app.get("/")
def read_root():
    return {"Hello": "GSA"}

@app.get("/search_awards")
async def search_awards_route(
    keyword: str = "",
    id: str = "",
    agency: str = "",
    awardeeCity: str = "",
    awardeeCountryCode: str = "",
    awardeeDistrictCode: str = "",
    awardeeName: str = "",
    awardeeStateCode: str = "",
    awardeeZipCode: str = "",
    cfdaNumber: str = "",
    coPDPI: str = "",
    dateStart: str = "",
    dateEnd: str = "",
    startDateStart: str = "",
    startDateEnd: str = "",
    expDateStart: str = "",
    expDateEnd: str = "",
    estimatedTotalAmtFrom: str = "",
    estimatedTotalAmtTo: str = "",
    fundsObligatedAmtFrom: str = "",
    fundsObligatedAmtTo: str = "",
    ueiNumber: str = "",
    fundProgramName: str = "",
    parentUeiNumber: str = "",
    pdPIName: str = "",
    perfCity: str = "",
    perfCountryCode: str = "",
    perfDistrictCode: str = "",
    perfLocation: str = "",
    perfStateCode: str = "",
    perfZipCode: str = "",
    poName: str = "",
    primaryProgram: str = "",
    transType: str = ""
):
    params = locals()
    return json.loads(search_awards(params))

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, client_id: Optional[str] = None):
    if client_id is None:
        client_id = websocket.query_params.get("client_id")

    if client_id is None:
        await websocket.close(code=4001)
        return
    # save this client into server memory
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_json()
            event = data["event"]
            print(event)
            

    except WebSocketDisconnect:
        print("Disconnecting...", client_id)
        await manager.disconnect(client_id)
    except Exception as e:
        print("Error:", str(e))
        await manager.disconnect(client_id)


if __name__ == "__main__":
    # uvicorn main:app --reload
    # ws://localhost:8000/ws?client_id=123
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Example of how to call the search_awards route:
# GET http://127.0.0.1:8000/search_awards?keyword=machine+learning&agency=NSF&dateStart=01/01/2022&dateEnd=12/31/2022