from app.calculator.repl import CalculatorREPL


def test_show_history_empty(capsys):

    repl = CalculatorREPL()
    repl.show_history()

    out = capsys.readouterr().out

    assert "No calculations" in out


def test_show_history_with_data(capsys):

    repl = CalculatorREPL()

    repl.history.append("1 add 2 = 3")

    repl.show_history()

    out = capsys.readouterr().out

    assert "1 add 2 = 3" in out


def test_show_help(capsys):

    repl = CalculatorREPL()

    repl.show_help()

    out = capsys.readouterr().out

    assert "Commands" in out


def test_get_number_valid(monkeypatch):

    repl = CalculatorREPL()

    monkeypatch.setattr("builtins.input", lambda _: "5")

    assert repl.get_number(">") == 5.0


def test_get_number_invalid(monkeypatch):

    repl = CalculatorREPL()

    monkeypatch.setattr("builtins.input", lambda _: "abc")

    try:
        repl.get_number(">")
        assert False
    except ValueError:
        assert True


def test_run_add(monkeypatch, capsys):

    inputs = iter([
        "add",
        "2",
        "3",
        "exit"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repl = CalculatorREPL()

    repl.run()

    out = capsys.readouterr().out

    assert "Result" in out


def test_run_invalid_command(monkeypatch, capsys):

    inputs = iter([
        "bad",
        "2",
        "3",
        "exit"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repl = CalculatorREPL()

    repl.run()

    out = capsys.readouterr().out

    assert "Error" in out
