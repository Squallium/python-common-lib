import fire

from main import MainDefaultTest


class TestMain:

    def test_hi(self, capsys):
        """
        Just checking the test framework is working.

        :param capsys:
        :return:
        """
        fire.Fire(MainDefaultTest, ['test'])
        out, err = capsys.readouterr()
        assert out == "Hi, test\n"
