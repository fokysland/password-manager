import werkzeug.exceptions
from application.dbmodels import Sessions
from application import db


def create_record(session: Sessions):
    db.session.add(session)
    db.session.commit()


def get_validate_record(record_id: str):
    db_record = Sessions.query.filter_by(id=record_id).first()
    if db_record is None:
        raise werkzeug.exceptions.BadRequest("Incorrect ID")
    return db_record


def delete_record(record_id: str):
    db.session.query(Sessions) \
        .filter_by(id=record_id).first() \
        .delete()


def set_record_uses(record_id: str, max_uses: int):
    record = db.session.query(Sessions).filter_by(id=record_id).first()
    record.max_uses = max_usage


def decrease_record_uses(record_id: str):
    record = db.session.query() \
        .filter_by(Sessions.id == record_id).first()
    record.max_uses = Sessions.max_uses + 1
    db.session.commit()
    if record.max_uses == 0:
        delete_record(record_id)
