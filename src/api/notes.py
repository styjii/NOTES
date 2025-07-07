import string
from pathlib import Path
from typing import Optional, List

from tinydb import TinyDB, where, table


class Note:
    
    database = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

    def __init__(self, table_name: str, content: str) -> None:
        self.content = content
        self.table_name = table_name
        self._set_active_table()

    def _set_active_table(self) -> None:
        if self.table_name not in Note.database.tables():
            raise ValueError(f"Table '{self.table_name}' does not exist.")
        
        Note.database.default_table_name = self.table_name

    def _validate_content(self) -> None:
        if not self.content:
            raise ValueError("Content is required.")

    def _find_note(self) -> Optional[table.Document]:
        return Note.database.get(where("content") == self.content)

    def exists(self) -> bool:
        """Check if the note exists.

        Returns:
            bool: True if the note exists, False otherwise.
        """
        return bool(self._find_note())

    def save(self, validate_content: Optional[bool] = False) -> bool:
        """Save the note.

        Args:
            validate_content (Optional[bool]): Whether to validate the note content.

        Returns:
            bool: True if saved, False otherwise.
        """
        if validate_content:
            self._validate_content()

        if self.exists():
            return False
        
        Note.database.insert({"content": self.content})
        return True
    
    def update(self, new_content: str, validate_content: Optional[bool] = False) -> bool:
        """Update the note's content.

        Args:
            new_content (str): New content for the note.
            validate_content (Optional[bool]): Whether to validate the new content.

        Returns:
            bool: True if updated, False otherwise.
        """
        updated_note = Note(table_name=self.table_name, content=new_content)
        if validate_content:
            updated_note._validate_content()

        if self.exists() and not updated_note.exists():
            Note.database.update({"content": updated_note.content}, where("content") == self.content)
            return True
        return False

    def delete(self) -> bool:
        """Delete the note.

        Returns:
            bool: True if deleted, False otherwise.
        """
        existing_note = self._find_note()
        if existing_note:
            Note.database.remove(doc_ids=[existing_note.doc_id])
            return True
        return False


class TableManager:

    database = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

    def __init__(self, table_name: str = "") -> None:
        self.table_name = table_name
        self._set_active_table()

    def _set_active_table(self) -> None:
        TableManager.database.default_table_name = self.table_name

    def _validate_table_name(self) -> None:
        if not self.table_name:
            raise ValueError("Category is required.")

        invalid_chars = string.digits + string.punctuation
        if any(char in self.table_name for char in invalid_chars):
            raise ValueError(f"Invalid table name: '{self.table_name}'")

    def get_all_table_names(self) -> List[str]:
        """Get all custom table names.

        Returns:
            List[str]: List of table names.
        """
        return [name for name in TableManager.database.tables() if name != "_default"]

    def exists(self) -> bool:
        """Check if the table exists.

        Returns:
            bool: True if table exists, False otherwise.
        """
        return self.table_name in self.get_all_table_names()

    def create(self, validate_name: Optional[bool] = False) -> bool:
        """Create a new table.

        Args:
            validate_name (Optional[bool]): Whether to validate the table name.

        Returns:
            bool: True if created, False otherwise.
        """
        if validate_name:
            self._validate_table_name()

        if self.exists():
            return False
        
        dummy_id = TableManager.database.insert({})
        TableManager.database.remove(doc_ids=[dummy_id])
        return True

    def delete(self) -> bool:
        """Delete the table.

        Returns:
            bool: True if deleted, False otherwise.
        """
        if self.exists():
            TableManager.database.drop_table(self.table_name)
            return True
        return False
    
    def get_all_contents(self) -> List[str]:
        """Get all contents inside the active table.

        Returns:
            List[str]: List of note contents.
        """
        return [record.get("content") for record in TableManager.database.all()]


if __name__ == "__main__":
    table_manager = TableManager()
    note1 = Note("DRAMA", "My Demon")
    note2 = Note("DRAMA", "Love in the Red Sky")

    response = note1.save()
    print(response)
