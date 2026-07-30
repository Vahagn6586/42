from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def contact_validator(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with \"AC\" "
                             "(Alien Contact)")

        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type is ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at least 3 "
                             "witnesses")

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should include received"
                             "messages")

        return self


def main() -> None:
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Hello from Zeta Reticuli."
        )
        print("Alien Contact Log Validation")
        print("=" * 40)
        print("Valid contact report:")
        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type.value}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'")
        print()
        print("=" * 40)
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    try:
        invalid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Hello from Zeta Reticuli."
        )
        print("Alien Contact Log Validation")
        print("=" * 40)
        print("Valid contact report:")
        print(f"ID: {invalid_contact.contact_id}")
        print(f"Type: {invalid_contact.contact_type.value}")
        print(f"Location: {invalid_contact.location}")
        print(f"Signal: {invalid_contact.signal_strength}/10")
        print(f"Duration: {invalid_contact.duration_minutes} minutes")
        print(f"Witnesses: {invalid_contact.witness_count}")
        print(f"Message: '{invalid_contact.message_received}'")
        print("=" * 40)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
