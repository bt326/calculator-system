from app.main import main


def test_main(monkeypatch):

    # Fake input to exit immediately
    inputs = iter(["exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
