import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import urllib.parse as uri_encoder
import httpx
import os

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "https://eagle-eye-navigation.netlify.app"
]
api_key = os.getenv("API_KEY")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/api/geocode")
async def get_geocode(q: str) -> dict:
    encode_q = uri_encoder.quote(q)
    open_cage_url = f"https://api.opencagedata.com/geocode/v1/json?q={encode_q}&key={api_key}&limit=1"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(open_cage_url)
    except httpx.RequestError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={
            "success": False,
            "error": "An error  occurred at the server level"
        })
    except httpx.NetworkError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
            "success": False,
            "error": "Check your network connection"
        })
    except httpx.ReadTimeout:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
            "success": False,
            "error": "Request timeout, refresh and try again"
        })

    data = response.json()
    if (data["status"]["code"] != 200 or data["status"]["code"] == 200) and not data["results"]:
        open_street_url = f'https://nominatim.openstreetmap.org/search?q={encode_q}&format=json&limit=1'
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(open_street_url)
        except httpx.NetworkError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
                "success": False,
                "error": "Check your network connection"
            })
        except httpx.ReadTimeout:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
                "success": False,
                "error": "Request timeout, refresh and try again"
            })
        except httpx.RequestError:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={
                "success": False,
                "error": "An error occurred at the server side"
            })

        data = response.json()
        if not data or data["error"]["code"] != 200:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                "success": True,
                "response": "location not found"
            })
        results = {
            "lat": data[0]["lat"],
            "lng": data[0]["lon"]
        }
        return {
            "success": True,
            "response": results,
            "source": "nominatim.openstreetmap.org"
        }

    results = data["results"][0]["geometry"]
    return {
        "success": True,
        "response": results,
        "source": "opencagedata.com"
    }

if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)