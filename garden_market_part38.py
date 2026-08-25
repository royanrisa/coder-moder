# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: GardenMarket
def test_edge_cases():
    # Test 1: Order with zero quantity
    order = Order('Test', 0, 0)
    assert order.quantity == 0
    assert order.total_amount == 0.0
    assert order.is_valid() == True

    # Test 2: Order with negative quantity
    order = Order('Test', -1, 0)
    assert order.quantity == -1
    assert order.total_amount == 0.0
    assert order.is_valid() == False

    # Test 3: Order with negative price
    order = Order('Test', 1, -100)
    assert order.quantity == 1
    assert order.total_amount == -100.0
    assert order.is_valid() == False

    # Test 4: Order with no items
    order = Order('Test', 1, 0)
    assert order.quantity == 1
    assert order.total_amount == 0.0
    assert order.is_valid() == False

    # Test 5: Order with too many items (exceeds max)
    order = Order('Test', 50, 0)
    assert order.quantity == 50
    assert order.total_amount == 0.0
    assert order.is_valid() == False

    # Test 6: Order with non-numeric quantity
    order = Order('Test', 'abc', 0)
    assert order.quantity == 'abc'
    assert order.total_amount == 0.0
    assert order.is_valid() == False

    # Test 7: Order with non-numeric price
    order = Order('Test', 1, 'abc')
    assert order.quantity == 1
    assert order.total_amount == 0.0
    assert order.is_valid() == False

    # Test 8: Order with empty name
    order = Order('', 1, 100)
    assert order.name == ''
    assert order.total_amount == 100.0
    assert order.is_valid() == False

    # Test 9: Order with very large quantity
    order = Order('Test', 1000000, 0)
    assert order.quantity == 1000000
    assert order.total_amount == 0.0
    assert order.is_valid() == False

    # Test 10: Order with very large price
    order = Order('Test', 1, 1000000)
    assert order.quantity == 1
    assert order.total_amount == 1000000.0
    assert order.is_valid() == False

    print("All edge case tests completed successfully!")
