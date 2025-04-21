from notes import Note, TableManager

import pytest
from tinydb import TinyDB


@pytest.fixture
def temp_db(tmp_path, monkeypatch):
    db_path = tmp_path / "test_db.json"
    db = TinyDB(db_path, indent=4)

    # Patch the database in both classes
    monkeypatch.setattr(Note, "database", db)
    monkeypatch.setattr(TableManager, "database", db)
    
    return db

@pytest.fixture
def note(temp_db):
    TableManager(table_name="Films").create()
    note = Note(table_name="Films", content="Craizy Love")
    note.save()
    return note

@pytest.fixture
def table_manager(temp_db):
    table = TableManager(table_name="Drama")
    table.create()
    return table

def test_note_save_and_exists(temp_db):
    TableManager("Films").create()
    note = Note(table_name="Films", content="Xmen")
    assert note.save(validate_content=True) is True
    assert note.exists() is True

def test_note_duplicate_save(temp_db):
    TableManager("Films").create()
    note = Note(table_name="Films", content="Xmen")
    assert note.save() is True
    assert note.save() is False

def test_note_save_without_content(temp_db):
    TableManager(table_name="Films").create()
    note = Note(table_name="Films", content="")
    with pytest.raises(ValueError) as err:
        note.save(validate_content=True)
    assert "Content is required." in str(err.value)

def test_note_update_content(note):
    test_note = Note(table_name="Films", content="Xmen")
    assert test_note.exists() is False
    assert test_note.update("Speeder Man") is False
    assert note.update(new_content="Speeder Man", validate_content=True) is True

def test_note_update_duplicate_content(note):
    test_note = Note("Films", "Xmen")
    test_note.save()
    assert test_note.update("Craizy Love") is False

def test_note_delete(note):
    assert note.delete() is True
    assert note.exists() is False

def test_delete_table(temp_db):
    manager = TableManager("Films")
    manager.create()
    assert manager.delete() is True
    assert "Films" not in manager.get_all_table_names()

def test_exists_table(table_manager):
    manager = TableManager("Films")
    assert manager.exists() is False
    assert table_manager.exists() is True

def test_get_all_table_names(table_manager):
    assert len(table_manager.get_all_table_names()) == 1
    assert table_manager.get_all_table_names()[0] == "Drama"

def test_get_all_contents(table_manager):
    assert not table_manager.get_all_contents()

def test_create_valid_table(temp_db):
    manager = TableManager("Drama")
    assert manager.create(validate_name=True) is True
    assert "Drama" in manager.get_all_table_names()

def test_create_duplicate_table(temp_db):
    manager = TableManager("Drama")
    manager.create()
    assert manager.create() is False

def test_create_invalidate_table_name(temp_db):
    invalid_table = TableManager("Mus1$")
    with pytest.raises(ValueError) as err:
        invalid_table._validate_table_name() 
    assert "Invalid table name" in str(err.value)
