from sqlalchemy.orm import Session

from application.tests.factories import RAMInfoFactory


def test_create_ram_info_with_factory(db_session: Session):
    """
    Test RAMInfo creation using the RAMInfoFactory.
    """
    # Given
    ram_info = RAMInfoFactory.build()  # Build a new instance without attaching to any session

    # When
    db_session.add(ram_info)  # Add the new instance to the session
    db_session.commit()       # Commit the transaction to the database

    # Refresh to get the updated state from the database
    db_session.refresh(ram_info)

    # Then
    assert ram_info.total is not None
    assert ram_info.free is not None
    assert ram_info.used == ram_info.total - ram_info.free
    assert ram_info.timestamp is not None
