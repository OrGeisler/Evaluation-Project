from fastapi import APIRouter,HTTPException,status
import requests
from . import first_router_utils
from ..db_utils import querys
from ..db_utils.db_proxy import db_proxy

firstRoute = APIRouter()


@firstRoute.get('/players',status_code=status.HTTP_200_OK)
def root(teamName,year):

    ## put the http call in the utils to catc the error

    try:
        players_data= requests.get(f'http://data.nba.net/10s/prod/v1/{year}/players.json').json()['league']
        players_list = first_router_utils.fillterByteam(players_data,teamName)
        return players_list 
    except:
        raise HTTPException(status_code=404, detail="Team stats does not exist")
