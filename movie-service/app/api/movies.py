from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import MovieOut, MovieIn, MovieUpdate
from app.api import db_manager
from app.api.service import is_cast_present

import pandas as pd

movies = APIRouter()

@movies.post('/', response_model=MovieOut, status_code=201)
async def create_movie(payload: MovieIn):
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(status_code=404, detail=f"Cast with given id:{cast_id} not found")

    movie_id = await db_manager.add_movie(payload)
    response = {
        'id': movie_id,
        **payload.dict()
    }

    return response

@movies.get('/', response_model=List[MovieOut])
async def get_movies():
    return await db_manager.get_all_movies()

@movies.get('/{id}/', response_model=MovieOut)
async def get_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@movies.put('/{id}/', response_model=MovieOut)
async def update_movie(id: int, payload: MovieUpdate):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = payload.dict(exclude_unset=True)

    if 'casts_id' in update_data:
        for cast_id in payload.casts_id:
            if not is_cast_present(cast_id):
                raise HTTPException(status_code=404, detail=f"Cast with given id:{cast_id} not found")

    movie_in_db = MovieIn(**movie)

    updated_movie = movie_in_db.copy(update=update_data)

    return await db_manager.update_movie(id, updated_movie)

@movies.delete('/{id}/', response_model=None)
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return await db_manager.delete_movie(id)

@movies.get('/by_plot/{plot}/', response_model=List[MovieOut])
async def get_movies_by_plot(plot: str):
    all_movies = await db_manager.get_all_movies()

    # Convert the movies to a Pandas DataFrame for easier manipulation
    movies_df = pd.DataFrame(all_movies)

    # Filter movies by the plot
    filtered_movies_df = movies_df[movies_df['plot'].str.contains(plot, case=False)]

    # Convert the filtered DataFrame back to a list of dictionaries
    filtered_movies = filtered_movies_df.to_dict(orient='records')

    if not filtered_movies:
        raise HTTPException(status_code=404, detail=f"No movies found with plot containing: {plot}")

    return filtered_movies
