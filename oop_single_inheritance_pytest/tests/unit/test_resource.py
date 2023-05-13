"""
Tests for Resource class
Command line: python -m pytest tests/unit/test_resource.py 
"""

import pytest 

from app.models import inventory 


@pytest.fixture   # make a common resource , this is a decorator
def resource_values():
    return {
        'name': 'Parrot', 
        'manufacturer': 'Pirates A-Hoy',
        'total': 30,
        'allocated': 2
    }

@pytest.fixture  
def resource(resource_values):
    return inventory.Resource(**resource_values)

def test_create_resource(resource_values, resource):
    # resource = inventory.Resource('Parrot', 'Pirates A-Hoy', 100, 20)
    # assert resource.name == 'Parrot'
    # assert resource.manufacturer == 'Pirates A-Hoy'
    # assert resource.total == 100
    # assert resource.allocated == 20
    # use fixture 

    # assert resource.name == resource_values['name']
    # assert resource.manufacturer == resource_values['manufacturer']
    # assert resource.total == resource_values['total']
    # assert resource.allocated == resource_values['allocated']

    # use loop and attributes to simplify codes
    for attr_name in resource_values:
        assert getattr(resource, attr_name) == resource_values.get(attr_name)

def test_create_invalid_total_type():
    with pytest.raises(TypeError):
        inventory.Resource('Parrot', 'Pirates A-Hoy', 10.5, 5)

def test_create_invalid_allocated_type():
    with pytest.raises(TypeError):
        inventory.Resource('name', 'manu', 10.5, 5)

def test_create_invalid_total_value():
    with pytest.raises(ValueError):
        inventory.Resource('name', 'manu', -10, 5)

@pytest.mark.parametrize('total, allocated', [(10, -5), (10, 20)])    # allow to test twice
def test_create_invalid_allocated_value(total, allocated):
    with pytest.raises(ValueError):
        inventory.Resource('name', 'manu', total, allocated)

def test_total(resource):
    assert resource.total == resource._total  

def test_allocated(resource):
    assert resource.allocated == resource._allocated 

def test_available(resource, resource_values):
    assert resource.available == resource.total - resource.allocated

def test_category(resource):
    assert resource.category == 'resource'

def test_str_repr(resource):
    assert str(resource.name) == resource.name 

def test_repr_repr(resource):
    assert repr(resource) == '{}, {} - {}: total={}, allocated={}'.format( 
        resource.name, resource.category, resource.manufacturer, resource.total,
        resource.allocated 
    )

        # return (f'{self.name}, {self.category} - {self.manufacturer}: '
        #         f'{self.total = }, {self.allocated = }')

def test_claim(resource):
    n = 2
    original_total = resource.total 
    original_allocated = resource.allocated 
    resource.claim(n)
    assert resource.total == original_total 
    assert resource.allocated == original_allocated + n     

@pytest.mark.parametrize('value', [-1, 0, 1_000])    # 3 tests 
def test_claim_invalid(resource, value):    # from resource fixture 
    with pytest.raises(ValueError):    # should throw 3 values 
        resource.claim(value)

def test_freeup(resource):
    n = 2 
    original_total = resource.total 
    original_allocated = resource.allocated
    resource.freeup(n)
    assert resource.allocated == original_allocated - n 
    assert resource.total == original_total 

@pytest.mark.parametrize('value', [-1, 0, 1_000])
def test_freeup_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.freeup(value)

def test_died(resource):
    n = 2 
    original_total = resource.total 
    original_allocated = resource.allocated 
    resource.died(n) 
    assert resource.total == original_total - n
    assert resource.allocated == original_allocated - n  

@pytest.mark.parametrize('value', [-1, 0, 30])
def test_died_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.died(value)

def test_purchased(resource):
    n = 2 
    original_total = resource.total 
    original_allocated = resource.allocated 
    resource.purchased(n)
    assert resource.total == original_total + n 
    assert resource.allocated == original_allocated 

@pytest.mark.parametrize('value', [-1, 0])
def test_purchased_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.purchased(value)