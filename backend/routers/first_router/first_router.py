from fastapi import APIRouter,HTTPException,status,Response
import requests
from . import first_router_utils
from ..db_utils import querys
from ..db_utils.db_proxy import db_proxy
from fastapi.responses import JSONResponse

firstRoute = APIRouter()


@firstRoute.get('/players',status_code=status.HTTP_200_OK , response_class= JSONResponse)
def root(teamName,year,response:Response):

    ## put the http call in the utils to catc the error

    try:
        players_data= requests.get(f'http://data.nba.net/10s/prod/v1/{year}/players.json').json()['league']
        players_list = first_router_utils.fillterByteam(players_data,teamName)
        return players_list 
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=404, detail="Team stats does not exist")
