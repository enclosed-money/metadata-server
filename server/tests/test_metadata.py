from app.models.metadata import Metadata, _Attribute
import pytest


def test_model_dict():
    m = Metadata(image='123456.png',
                 external_url='https://www.enclosed.money/123456.png',
                 description='100 $USDT wrapped in an NFT',
                 name='Enclosed.Money',
                 attributes=[
                     _Attribute(trait_type='Token',
                                value='USDT'),
                     _Attribute(trait_type='Amount',
                                value='100')],
                 background_color='ffffff')

    obj_json = m.dict()
    assert list(obj_json['attributes'][0].keys()) == ['trait_type', 'value']


def test_hexadecimal():
    m = Metadata(image='123456.png',
                 external_url='https://www.enclosed.money/123456.png',
                 description='100 $USDT wrapped in an NFT',
                 name='Enclosed.Money',
                 attributes=[
                     _Attribute(trait_type='Token',
                                value='USDT'),
                     _Attribute(trait_type='Amount',
                                value='100')],
                 background_color='#ffffff')

    assert m.dict()['background_color'] == 'ffffff'

    with pytest.raises(Exception):
        m = Metadata(image='123456.png',
                     external_url='https://www.enclosed.money/123456.png',
                     description='100 $USDT wrapped in an NFT',
                     name='Enclosed.Money',
                     attributes=[
                         _Attribute(trait_type='Token',
                                    value='USDT'),
                         _Attribute(trait_type='Amount',
                                    value='100')],
                     background_color='123')
