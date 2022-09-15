from fastapi import FastAPI

# from . import crud, models, schemas
# from .database import SessionLocal, engine

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello World"}

# @app.post("/links", response_model=schemas.Link)
# def create_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
#     db_link = crud.create_link(db, link)
#     return db_link
#
# @app.get("/links/{link_id}", response_model=schemas.User)
# def get_link(link_id: int, db: Session = Depends(get_db)):
#     db_link = crud.get_link(db, link)
#     return db_link

