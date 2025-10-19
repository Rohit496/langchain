from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator("age")
    def check_age(cls, v):
        if v < 18:
            raise ValueError("User must be at least 18 years old.")
        return v


# Example````
user = User(name="Rohit", email="rohit@example.com", age=30)
print(user)


def validate_email(email):
    # check if email ends with hdfc.com or icici.com
    allowed_domains = ("@hdfc.com", "@icici.com")

    if not isinstance(email, str):
        raise ValueError("Email must be a string.")

    if not any(email.endswith(domain) for domain in allowed_domains):
        raise ValueError(
            "❌ Invalid email domain. Only @hdfc.com or @icici.com allowed."
        )

    print("✅ Email is valid!")


# Example usage
validate_email("rohit@hdfc.com")  # ✅ valid
validate_email("user@icici.com")  # ✅ valid
# validate_email("someone@gmail.com")  # ❌ raises ValueError
