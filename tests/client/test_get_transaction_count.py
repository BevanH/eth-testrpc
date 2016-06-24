def test_get_transaction_count(client, accounts):
    for _ in range(3):
        client.send_transaction(_from=accounts[0], to=accounts[1], value=1)

    for _ in range(5):
        client.send_transaction(_from=accounts[1], to=accounts[0], value=1)

    account_0_txn_count = client.get_transaction_count(accounts[0])
    assert account_0_txn_count == 3

    account_1_txn_count = client.get_transaction_count(accounts[1])
    assert account_1_txn_count == 5
