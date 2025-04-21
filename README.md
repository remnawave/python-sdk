# Remnawave SDK

A Python SDK client for interacting with the [Remnawave API](https://remna.st).
This library simplifies working with the API by providing convenient controllers, Pydantic models for requests and responses, and fast serialization with `orjson`.

## ✨ Key Features

- **Controller-based design**: Split functionality into separate controllers for flexibility. Use only what you need!
- **Pydantic models**: Strongly-typed requests and responses for better reliability.
- **Fast serialization**: Powered by `orjson` for efficient JSON handling.
- **Modular usage**: Import individual controllers or the full SDK as needed.

## 📦 Installation

Currently, the SDK is available via Git. You can install it directly using `pip`:

```bash
pip install git+https://github.com/sm1ky/remnawave_api.git
```

---

### Dependencies
- `orjson` (>=3.10.15, <4.0.0)
- `rapid-api-client` (==0.6.0)

## 🚀 Usage

Here’s a quick example to get you started:

```python
import os
import asyncio

from remnawave import RemnawaveSDK
from remnawave.models import UsersResponseDto, UserResponseDto

async def main():
    # URL to your panel (ex. https://vpn.com or http://127.0.0.1:3000)
    base_url: str = os.getenv("REMNAWAVE_BASE_URL")
    # Bearer Token from panel (section: API Tokens) 
    token: str = os.getenv("REMNAWAVE_TOKEN")

    # Initialize the SDK
    remnawave = RemnawaveSDK(base_url=base_url, token=token)

    # Fetch all users
    response: UsersResponseDto = await remnawave.users.get_all_users_v2()
    total_users: int = response.total
    users: list[UserResponseDto] = response.users
    print("Total users: ", total_users)
    print("List of users: ", users)

    # Disable a specific user
    test_uuid: str = "e4d3f3d2-4f4f-4f4f-4f4f-4f4f4f4f4f4f"
    disabled_user: UserResponseDto = await remnawave.users.disable_user(test_uuid)
    print("Disabled user: ", disabled_user)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🧪 Running Tests

To run the test suite, use Poetry:

```bash
poetry run pytest
```

## ❤️ About

This SDK was originally developed by [@kesevone](https://github.com/kesevone) for integration with Remnawave's API.

Maintained and extended by [@sm1ky](https://github.com/sm1ky).