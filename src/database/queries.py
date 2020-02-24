from sqlalchemy import func
from sqlalchemy.orm import Session

from src.database import replica_session, master_session
from src.database.models import History
from src.database.models.history import Album


def get_all(session: Session):
    return session.query(History.album).distinct().all()


def get_count(session: Session):
    return session.query(History.album, func.count(History.album)).group_by(History.album).all()


def save(album: Album):
    with master_session() as session:
        history = History()
        history.album = album
        session.merge(history)
