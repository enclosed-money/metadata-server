from app.models.metadata import Metadata
from app import config
from fastapi import APIRouter
from urllib.parse import urljoin

router = APIRouter()


@router.get("/{token_id}", response_model=Metadata)
async def get_token_metadata(token_id: str) -> Metadata:
    # Deconstructing the token ID into it's representative components
    deposited_token_address = token_id[:42]
    deposited_value = token_id[42:]

    metadata_json = {
        'image': urljoin(config.API_BASE_URI, f'api/image/{token_id}'),
        'external_url': 'https://www.enclosed.money',
        'description': 'Your tokens wrapped up.',
        'name': 'Enclosed Money',
        'attributes': [
            {'trait_type': 'Token',
             'value': deposited_token_address},
            {'trait_type': 'Value',
             'value': deposited_value}
        ],
        'background_color': 'ffffff'
    }

    return metadata_json
